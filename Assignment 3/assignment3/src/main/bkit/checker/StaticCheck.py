
"""
 * @author nhphung
"""
from abc import ABC, abstractmethod, ABCMeta
from dataclasses import FrozenInstanceError, dataclass
from typing import List, Tuple
from AST import * 
from Visitor import *
from StaticError import *
from functools import *
from functools import reduce

class Type(ABC):
    __metaclass__ = ABCMeta
    pass
class Prim(Type):
    __metaclass__ = ABCMeta
    pass
class IntType(Prim):
    pass
class FloatType(Prim):
    pass
class StringType(Prim):
    pass
class BoolType(Prim):
    pass
class VoidType(Type):
    pass
class Unknown(Type):
    pass
class NotInfer(Type):
    pass

@dataclass
class ArrayType(Type):
    dimen:List[int]
    eletype: Type

@dataclass
class MType:
    intype:List[Type]
    restype:Type

@dataclass
class Symbol:
    name: str
    mtype:Type

class StaticChecker(BaseVisitor):
    def __init__(self,ast):
        self.ast = ast
        self.global_envi = [
Symbol("int_of_float",MType([FloatType()],IntType())),
Symbol("float_of_int",MType([IntType()],FloatType())),
Symbol("int_of_string",MType([StringType()],IntType())),
Symbol("string_of_int",MType([IntType()],StringType())),
Symbol("float_of_string",MType([StringType()],FloatType())),
Symbol("string_of_float",MType([FloatType()],StringType())),
Symbol("bool_of_string",MType([StringType()],BoolType())),
Symbol("string_of_bool",MType([BoolType()],StringType())),
Symbol("read",MType([],StringType())),
Symbol("printLn",MType([],VoidType())),
Symbol("printStr",MType([StringType()],VoidType())),
Symbol("printStrLn",MType([StringType()],VoidType()))]                           
   
    def check(self):
        return self.visit(self.ast,self.global_envi)

    def lookup(self, compare, lst, func):
        for x in lst:
            if compare == func(x):
                return x
        return None

    def raise_(self, ex): # To raise exception in lambda funcion
        raise ex

    def matchNameInEnv(self, kind, key, env):
        if kind == 'all':
            for x in env:
                if x.name == key:
                    return True
            return False

        elif kind == 'func':
            for x in env:
                if x.name == key and type(x.mtype) is MType:
                    return True
            return False

        elif kind == 'var':
            for x in env:
                if x.name == key and type(x.mtype) is not MType:
                    return True
            return False
    
    def updateTypeInEnv(self, key, value, env, arrayTypeFlag = False):
        for x in env:
            if x.name == key:
                if type(x.mtype) == MType:        
                    if arrayTypeFlag:
                        x.mtype.restype = value
                    elif type(x.mtype.restype) == ArrayType:
                        x.mtype.restype.eletype = value
                    else:
                        x.mtype.restype = value
                    
                elif type(x.mtype) == ArrayType:
                    if isinstance(env[-1].mtype, MType):
                        for i in range(len(env[-1].mtype.intype)):
                            if id(env[-1].mtype.intype[i]) == id(x.mtype):
                                x.mtype.eletype = value
                                env[-1].mtype.intype[i] = x.mtype
                    else:
                        x.mtype.eletype = value

                else:
                    if isinstance(env[-1].mtype, MType):
                        for i in range(len(env[-1].mtype.intype)):
                            if id(env[-1].mtype.intype[i]) == id(x.mtype):
                                env[-1].mtype.intype[i] = value
                    x.mtype = value

    def createNewEnv(self, envOuter, envInner):
        env = [] + envInner
        for x in envOuter:
            if not self.matchNameInEnv('all', x.name, envInner):
                env += [x]
        return env

    def updateOldEnv(self, envOld, envExcept, envNew):
        for x in envOld:
            if self.matchNameInEnv('all', x.name, envNew):
                if type(x.mtype) == MType and not self.matchNameInEnv('all', x.name, envExcept):
                    print(self.lookup(x.name, envNew, lambda ele: ele.name).mtype.intype)
                    x.mtype.intype = self.lookup(x.name, envNew, lambda ele: ele.name).mtype.intype
                if type(self.getTypeInEnv(x.name, envOld, False)) == Unknown and not self.matchNameInEnv('all', x.name, envExcept):
                    typeInEnvNew = self.getTypeInEnv(x.name ,envNew, False)
                    self.updateTypeInEnv(x.name, typeInEnvNew, envOld)

    def getTypeInEnv(self, key, env, arrayTypeFlag):
        """True flag if you want return an ArrayType"""
        mtype = self.lookup(key, env, lambda x: x.name).mtype
        if type(mtype) == MType:
            if type(mtype.restype) == ArrayType:
                if arrayTypeFlag:
                    return mtype.restype
                return mtype.restype.eletype
            return mtype.restype
        elif type(mtype) == ArrayType:
                if arrayTypeFlag:
                    return mtype
                return mtype.eletype
        else:       
            return mtype

    def traverseFunc(self, ast, o):
        funcName = ast.name.name
        if self.matchNameInEnv('all', funcName, o):
            raise Redeclared(Function(), funcName)

        # Raise exception follow by: https://stackoverflow.com/questions/8294618/define-a-lambda-expression-that-raises-an-exception
        lstParam = reduce(lambda env, ele: env + [self.visit(ele, env)] \
             if not self.matchNameInEnv('all', ele.variable.name, env) \
                 else self.raise_(Redeclared(Parameter(), ele.variable.name)) ,\
                      ast.param, [])

        lstParamType = list(map(lambda x: x.mtype, lstParam))
        retType = Unknown()
        return Symbol(funcName, MType(lstParamType, retType))

    def getNameOfAst(self, ast):
        if isinstance(ast, ArrayCell):
            if isinstance(ast.arr, CallExpr):
                return ast.arr.method.name
            else:
                return ast.arr.name

        elif isinstance(ast, CallExpr):
            return ast.method.name
        
        elif isinstance(ast, Id):
            return ast.name

    def updateParamInEnv(self, funcName, lstParamType, env):
        for x in env:
            if x.name == funcName:
                for i in range(len(x.mtype.intype)):
                    if type(x.mtype.intype[i]) == Unknown:
                        x.mtype.intype[i] = lstParamType[i]
                    elif type(x.mtype.intype[i]) == ArrayType:
                        if type(x.mtype.intype[i].eletype) == Unknown:
                            x.mtype.intype[i] = lstParamType[i]



    # decl : List[Decl]
    def visitProgram(self, ast, o):
        innerEnv = [] + []
        programEnv = reduce(lambda env, ele: env + [self.visit(ele, env)] if isinstance(ele, VarDecl) else env + [self.traverseFunc(ele, env)], ast.decl, innerEnv)
        # Compile all functions in program
        [self.visit(x, programEnv) for x in ast.decl if isinstance(x, FuncDecl)]
        # Check entry point ==> function 'main'
        if not self.matchNameInEnv('func', 'main', programEnv):
            raise NoEntryPoint()
    
    # variable : Id
    # varDimen : List[int]
    # varInit  : Literal 
    def visitVarDecl(self, ast, o):
        varName = ast.variable.name
        if self.matchNameInEnv('all', varName, o):
            raise Redeclared(Variable(), varName)
        if ast.varDimen:
            typeInit = ArrayType(ast.varDimen, self.visit(ast.varInit, o).eletype if ast.varInit else Unknown())
        else:
            typeInit = self.visit(ast.varInit, o) if ast.varInit else Unknown()
        return Symbol(varName, typeInit)
    
    # name: Id
    # param: List[VarDecl]
    # body: Tuple[List[VarDecl],List[Stmt]]
    def visitFuncDecl(self, ast, o):
        funcName = ast.name.name
        lstParam = reduce(lambda env, ele: env + [self.visit(ele, env)]  \
        if not self.matchNameInEnv('all', ele.variable.name, env) \
            else self.raise_(Redeclared(Parameter(), ele.variable.name)) ,\
                ast.param, [])
        lstParamTypeInEnv = self.lookup(funcName, o, lambda x: x.name).mtype.intype
        for i in range(len(lstParam)):
            lstParam[i].mtype = lstParamTypeInEnv[i]
        innerEnv = reduce(lambda env, ele: env + [self.visit(ele, env)], ast.body[0], lstParam)
        funcEnv = self.createNewEnv(o, innerEnv)
        # Move enclose function to end of env
        funcEnv.append(funcEnv.pop(funcEnv.index(self.lookup(funcName, funcEnv, lambda x: x.name))))
        [self.visit(x, funcEnv) for x in ast.body[1]]
        # self.updateOldEnv(lstParam, [], funcEnv) # Update param with func env
        # lstParamType = [x.mtype for x in lstParam]
        # self.updateParamInEnv(ast.name.name, lstParamType, o)
        self.updateOldEnv(o, innerEnv, funcEnv)
    
    # op:str
    # left:Expr
    # right:Expr
    def visitBinaryOp(self, ast, o):
        if type(ast.left) == NotInfer or type(ast.right):
            return NotInfer()
        if ast.op in ['+','-','*','\\','%']:
            if type(self.visit(ast.left, o)) == Unknown:
                self.updateTypeInEnv(self.getNameOfAst(ast.left), IntType(), o)
            if type(self.visit(ast.right, o)) == Unknown:
                self.updateTypeInEnv(self.getNameOfAst(ast.right), IntType(), o)
            if type(self.visit(ast.left, o)) != IntType or type(self.visit(ast.right, o)) != IntType:
                raise TypeMismatchInExpression(ast)
            return IntType()

        elif ast.op in ['+.','-.','*.','\\.']:
            if type(self.visit(ast.left, o)) == Unknown:
                self.updateTypeInEnv(self.getNameOfAst(ast.left), FloatType(), o)
            if type(self.visit(ast.right, o)) == Unknown:
                self.updateTypeInEnv(self.getNameOfAst(ast.right), FloatType(), o)
            if type(self.visit(ast.left, o)) != FloatType or type(self.visit(ast.right, o)) != FloatType:
                raise TypeMismatchInExpression(ast)
            return FloatType()

        elif ast.op in ['&&','||']:
            if type(self.visit(ast.left, o)) == Unknown:
                self.updateTypeInEnv(self.getNameOfAst(ast.left), BoolType(), o)
            if type(self.visit(ast.right, o)) == Unknown:
                self.updateTypeInEnv(self.getNameOfAst(ast.right), BoolType(), o)
            if type(self.visit(ast.left, o)) != BoolType or type(self.visit(ast.right, o)) != BoolType:
                raise TypeMismatchInExpression(ast)
            return BoolType()

        elif ast.op in ['==','!=','<','>','<=','>=']:
            if type(self.visit(ast.left, o)) == Unknown:
                self.updateTypeInEnv(self.getNameOfAst(ast.left), IntType(), o)
            if type(self.visit(ast.right, o)) == Unknown:
                self.updateTypeInEnv(self.getNameOfAst(ast.right), IntType(), o)
            if type(self.visit(ast.left, o)) != IntType or type(self.visit(ast.right, o)) != IntType:
                raise TypeMismatchInExpression(ast)
            return BoolType()

        elif ast.op in ['=/=','<.','>.','<=.','>=.']:
            if type(self.visit(ast.left, o)) == Unknown:
                self.updateTypeInEnv(self.getNameOfAst(ast.left), FloatType(), o)
            if type(self.visit(ast.right, o)) == Unknown:
                self.updateTypeInEnv(self.getNameOfAst(ast.right), FloatType(), o)
            if type(self.visit(ast.left, o)) != FloatType or type(self.visit(ast.right, o)) != FloatType:
                raise TypeMismatchInExpression(ast)
            return BoolType()
    
    # op:str
    # body:Expr    
    def visitUnaryOp(self, ast, o):
        if type(ast.body) == NotInfer:
            return NotInfer()
        if ast.op == '-':
            if type(self.visit(ast.body, o)) == Unknown:
                self.updateTypeInEnv(self.getNameOfAst(ast.body), IntType(), o)
            if type(self.visit(ast.body, o)) != IntType:
                raise TypeMismatchInExpression(ast)
            return IntType()
        elif ast.op == '-.':
            if type(self.visit(ast.body, o)) == Unknown:
                self.updateTypeInEnv(self.getNameOfAst(ast.body), FloatType(), o)
            if type(self.visit(ast.body, o)) != FloatType:
                raise TypeMismatchInExpression(ast)
            return FloatType()
        elif ast.op == '!':
            if type(self.visit(ast.body, o)) == Unknown:
                self.updateTypeInEnv(self.getNameOfAst(ast.body), FloatType(), o)
            if type(self.visit(ast.body, o)) != BoolType:
                raise TypeMismatchInExpression(ast)
            return BoolType()
    
    # method:Id
    # param:List[Expr]
    def visitCallExpr(self, ast, o):
        funcName = ast.method.name
        if not self.matchNameInEnv('func', funcName, o):
            raise Undeclared(Function(), funcName)
        lstArg = [self.visit(ele, o) for ele in ast.param]
        lstParam = self.lookup(funcName, o, lambda x: x.name).mtype.intype

        if len(lstArg) != len(lstParam):
            raise TypeMismatchInExpression(ast)
        for i in range(len(lstArg)):
            if type(lstArg[i]) == NotInfer or type(lstParam[i]) == NotInfer:
                return NotInfer()
            elif type(lstArg[i]) == Unknown and isinstance(ast.param[i], CallExpr) and type(lstParam[i]) == ArrayType:
                if lstParam[i].dimen and type(lstParam[i].eletype) != Unknown:
                    self.updateTypeInEnv(self.getNameOfAst(ast.param[i]), rhs, True)
                else:
                    return  NotInfer()
            elif type(lstArg[i]) not in [Unknown, ArrayType] and type(lstParam[i]) == Unknown:
                lstParam[i] = lstArg[i]
            elif type(lstParam[i]) not in [Unknown, ArrayType] and type(lstArg[i]) == Unknown:
                lstArg[i] = lstParam[i]
                self.updateTypeInEnv(self.getNameOfAst(ast.param[i]), lstParam[i], o)
            elif type(lstArg[i]) == Unknown and type(lstParam[i]) == Unknown:
                return NotInfer()
            elif (type(lstArg[i]) == ArrayType and type(lstParam[i]) == ArrayType):
                if lstArg[i].dimen == lstParam[i].dimen:
                    if type(lstArg[i].eletype) == Unknown and type(lstParam[i].eletype) == Unknown:
                        return NotInfer()
                    elif type(lstArg[i].eletype) == Unknown and type(lstParam[i].eletype) != Unknown:
                        lstArg[i]= lstParam[i]
                        self.updateTypeInEnv(self.getNameOfAst(ast.param[i]), lstParam[i].eletype, o)
                    elif type(lstParam[i].eletype) == Unknown and type(lstArg[i].eletype) != Unknown:
                        lstParam[i] = lstArg[i]
                    elif type(lstArg[i].eletype) != type(lstParam[i].eletype):
                        raise TypeMismatchInStatement(ast)
                else:
                    raise TypeMismatchInStatement(ast)
        
            elif type(lstArg[i]) != type(lstParam[i]):
                raise TypeMismatchInStatement(ast)
        self.updateParamInEnv(funcName, lstParam, o)
        return self.getTypeInEnv(funcName, o, True)
    
    # name : str
    def visitId(self, ast, o):
        varName = ast.name
        if not self.matchNameInEnv('var', varName, o):
            raise Undeclared(Identifier(), varName)
        return self.getTypeInEnv(varName, o, True)
    
    # arr:Expr
    # idx:List[Expr]
    def visitArrayCell(self, ast, o):
        if not ast.idx:
            raise TypeMismatchInExpression(ast)
        for x in ast.idx:
            if type(self.visit(x, o)) != IntType:
                raise TypeMismatchInExpression(ast)
        
        if type(self.visit(ast.arr, o)) == ArrayType:
            return self.visit(ast.arr, o).eletype  
        elif type(self.visit(ast.arr, o)) in [Unknown, NotInfer]:
            if isinstance(ast.arr. CallExpr):
                return NotInfer()
            else: # If it's Id
                raise TypeMismatchInExpression(ast)
    
    # lhs: LHS
    # rhs: Expr    
    def visitAssign(self, ast, o):
        lhs = self.visit(ast.lhs, o)
        rhs = self.visit(ast.rhs, o)
        if type(lhs) == NotInfer or type(rhs) == NotInfer:
            raise TypeCannotBeInferred(ast)
        elif type(lhs) == VoidType or type(rhs) == VoidType:
            raise TypeMismatchInStatement(ast)
        elif type(lhs) == Unknown and type(rhs) == Unknown:
            raise TypeCannotBeInferred(ast)
        elif type(lhs) == Unknown and isinstance(ast.lhs, CallExpr) and type(rhs) == ArrayType:
            if rhs.dimen and type(rhs.eletype) != Unknown:
                self.updateTypeInEnv(self.getNameOfAst(ast.lhs), rhs, True)
            else:
                raise TypeCannotBeInferred(ast)
        elif type(rhs) == Unknown and isinstance(ast.rhs, CallExpr) and type(lhs) == ArrayType:
            if lhs.dimen and type(lhs.eletype) != Unknown:
                self.updateTypeInEnv(self.getNameOfAst(ast.rhs), lhs, o, True)
            else:
                raise TypeCannotBeInferred(ast)
        elif type(lhs) == Unknown and type(rhs) not in [Unknown, ArrayType]:
            lhs = rhs
            self.updateTypeInEnv(self.getNameOfAst(ast.lhs), rhs, o)
        elif type(rhs) == Unknown and type(lhs) not in [Unknown, ArrayType]:
            rhs = lhs
            self.updateTypeInEnv(self.getNameOfAst(ast.rhs), lhs, o)
        elif (type(lhs) == ArrayType and type(rhs) == ArrayType):
            if lhs.dimen == rhs.dimen:
                if type(lhs.eletype) == Unknown and type(rhs.eletype) == Unknown:
                    raise TypeCannotBeInferred(ast)
                elif type(lhs.eletype) == Unknown and type(rhs.eletype) != Unknown:
                    lhs = rhs
                    self.updateTypeInEnv(self.getNameOfAst(ast.lhs), rhs.eletype, o)
                elif type(rhs.eletype) == Unknown and type(lhs.eletype) != Unknown:
                    rhs = lhs
                    self.updateTypeInEnv(self.getNameOfAst(ast.rhs), lhs.eletype, o)
                elif type(lhs.eletype) != type(rhs.eletype):
                    raise TypeMismatchInStatement(ast)
            else:
                raise TypeMismatchInStatement(ast)
        elif type(lhs) != type(rhs):
            raise TypeMismatchInStatement(ast)
    
    # ifthenStmt:List[Tuple[Expr,List[VarDecl],List[Stmt]]]
    # elseStmt:Tuple[List[VarDecl],List[Stmt]]
    def visitIf(self, ast, o):
        for ifThenStm in ast.ifthenStmt:
            exp = self.visit(ifThenStm[0], o)
            if type(exp) == Unknown:
                self.updateTypeInEnv(self.getNameOfAst(ifThenStm[0]), BoolType(), o)
            elif type(exp) == NotInfer:
                raise TypeCannotBeInferred(ast)
            elif type(self.visit(ifThenStm[0], o)) != BoolType:
                raise TypeMismatchInStatement(ast)
            innerEnv = reduce(lambda env, ele: env + [self.visit(ele, env)], ifThenStm[1], [])
            ifThenEnv = self.createNewEnv(o, innerEnv)
            [self.visit(x, ifThenEnv) for x in ifThenStm[2]]
            self.updateOldEnv(o, innerEnv, ifThenEnv)
        if ast.elseStmt:
            innerEnv = reduce(lambda env, ele: env + [self.visit(ele, env)], ast.elseStmt[0], [])
            elseEnv = self.createNewEnv(o, innerEnv)
            [self.visit(x, elseEnv) for x in ast.elseStmt[1]]
            self.updateOldEnv(o, innerEnv, elseEnv)

    # idx1: Id
    # expr1:Expr
    # expr2:Expr
    # expr3:Expr
    # loop: Tuple[List[VarDecl],List[Stmt]]    
    def visitFor(self, ast, o):
        if NotInfer in [type(self.visit(ast.idx1, o)), type(self.visit(ast.expr1, o)), type(self.visit(ast.expr2, o)), type(self.visit(ast.expr3, o))]:
            raise TypeCannotBeInferred(ast)
        # Infer and check for idx1 and expr1
        if type(self.visit(ast.idx1, o)) == Unknown:
            self.updateTypeInEnv(self.getNameOfAst(ast.idx1), IntType(), o)
        if type(self.visit(ast.expr1, o)) == Unknown:
            self.updateTypeInEnv(self.getNameOfAst(ast.expr1), IntType(), o)

        if type(self.visit(ast.idx1, o)) != IntType or type(self.visit(ast.expr1, o)) != IntType:
            raise TypeMismatchInStatement(ast)
        # Infer and check for expr2
        if type(self.visit(ast.expr2, o)) == Unknown:
            self.updateTypeInEnv(self.getNameOfAst(ast.idx1), BoolType(), o)
        elif type(self.visit(ast.expr2, o)) != BoolType: 
            raise TypeMismatchInStatement(ast)
        # Infer and check for expr3
        if type(self.visit(ast.expr3, o)) == Unknown:
            self.updateTypeInEnv(self.getNameOfAst(ast.idx1), IntType(), o)
        elif type(self.visit(ast.expr3, o)) != IntType: 
            raise TypeMismatchInStatement(ast) 
        innerEnv = reduce(lambda env, ele: env + [self.visit(ele, env)], ast.loop[0], [])
        whileDoEnv = self.createNewEnv(o, innerEnv)
        [self.visit(x, whileDoEnv) for x in ast.loop[1]]
        self.updateOldEnv(o, innerEnv, whileDoEnv)
    
    def visitContinue(self, ast, o):
        return None
    
    def visitBreak(self, ast, o):
        return None
    
    # expr:Expr
    def visitReturn(self, ast, o):
        # Enclose function at end of env
        if ast.expr:
            retType = self.visit(ast.expr, o)
        else:
            retType = VoidType()
        if type(o[-1].mtype.restype) == Unknown:
            self.updateTypeInEnv(o[-1].name, retType, o)
        elif type(o[-1].mtype.restype) == ArrayType and type(retType) == ArrayType:
            if not (o[-1].restype.mtype.dimen == retType.dimen and o[-1].mtype.restype.eletype == retType.eletype):
                raise TypeMismatchInStatement(ast)
        elif type(o[-1].mtype.restype) != type(retType):
            raise TypeMismatchInStatement(ast)
    
    # sl:Tuple[List[VarDecl],List[Stmt]]
    # exp: Expr
    def visitDowhile(self, ast, o):
        innerEnv = reduce(lambda env, ele: env + [self.visit(ele, env)], ast.sl[0], [])
        doWhileEnv = self.createNewEnv(o, innerEnv)
        [self.visit(x, doWhileEnv) for x in ast.sl[1]]
        exp = self.visit(ast.exp, o)
        if type(exp) == Unknown:
            self.updateTypeInEnv(self.getNameOfAst(ast.exp), BoolType(), o)
        elif type(exp) == NotInfer:
            raise TypeCannotBeInferred(ast)
        elif type(exp) != BoolType:
            raise TypeMismatchInStatement(ast)
        self.updateOldEnv(o, innerEnv, doWhileEnv)

    # exp: Expr
    # sl:Tuple[List[VarDecl],List[Stmt]]
    def visitWhile(self, ast, o):
        exp = self.visit(ast.exp, o)
        if type(exp) == Unknown:
            self.updateTypeInEnv(self.getNameOfAst(ast.exp), BoolType(), o)
        elif type(exp) == NotInfer:
            raise TypeCannotBeInferred(ast)
        elif type(exp) != BoolType:
            raise TypeMismatchInStatement(ast)
        innerEnv = reduce(lambda env, ele: env + [self.visit(ele, env)], ast.sl[0], [])
        whileDoEnv = self.createNewEnv(o, innerEnv)
        [self.visit(x, whileDoEnv) for x in ast.sl[1]]
        self.updateOldEnv(o, innerEnv, whileDoEnv)

    # method:Id
    # param:List[Expr]
    def visitCallStmt(self, ast, o):
        funcName = ast.method.name
        if not self.matchNameInEnv('func', funcName, o):
            raise Undeclared(Function(), funcName)
        retType = self.getTypeInEnv(funcName, o, True)
        if type(retType) == Unknown:
            self.updateTypeInEnv(funcName, VoidType(), o)
        elif type(retType) != VoidType:
            raise TypeMismatchInStatement(ast)
        lstArg = [self.visit(ele, o) for ele in ast.param]
        lstParam = [ele for ele in self.lookup(funcName, o, lambda x: x.name).mtype.intype]

        if len(lstArg) != len(lstParam):
            raise TypeMismatchInStatement(ast)
        for i in range(len(lstArg)):
            if type(lstArg[i]) == NotInfer or type(lstParam[i]) == NotInfer:
                raise TypeCannotBeInferred(ast)
            elif type(lstArg[i]) == Unknown and type(lstParam[i]) == Unknown:
                raise TypeCannotBeInferred(ast)
            elif type(lstArg[i]) == Unknown and isinstance(ast.param[i], CallExpr) and type(lstParam[i]) == ArrayType:
                if lstParam[i].dimen and type(lstParam[i].eletype) != Unknown:
                    self.updateTypeInEnv(self.getNameOfAst(ast.param[i]), rhs, True)
                else:
                    raise TypeCannotBeInferred(ast)
            elif type(lstArg[i]) not in [Unknown, ArrayType] and type(lstParam[i]) == Unknown:
                lstParam[i] = lstArg[i]
            elif type(lstParam[i]) not in [Unknown, ArrayType] and type(lstArg[i]) == Unknown:
                lstArg[i] = lstParam[i]
                self.updateTypeInEnv(self.getNameOfAst(ast.param[i]), lstParam[i], o)
            elif (type(lstArg[i]) == ArrayType and type(lstParam[i]) == ArrayType):
                if lstArg[i].dimen == lstParam[i].dimen:
                    if type(lstArg[i].eletype) == Unknown and type(lstParam[i].eletype) == Unknown:
                        raise TypeCannotBeInferred(ast)
                    elif type(lstArg[i].eletype) == Unknown and type(lstParam[i].eletype) != Unknown:
                        lstArg[i]= lstParam[i]
                        self.updateTypeInEnv(self.getNameOfAst(ast.param[i]), lstParam[i].eletype, o)
                    elif type(lstParam[i].eletype) == Unknown and type(lstArg[i].eletype) != Unknown:
                        lstParam[i] = lstArg[i]
                    elif type(lstArg[i].eletype) != type(lstParam[i].eletype):
                        raise TypeMismatchInStatement(ast)
                else:
                    raise TypeMismatchInStatement(ast)
                
            elif type(lstArg[i]) != type(lstParam[i]):
                raise TypeMismatchInStatement(ast)
        self.updateParamInEnv(funcName, lstParam, o)
    
    # value:int
    def visitIntLiteral(self, ast, o):
        return IntType()
    
    # value:float
    def visitFloatLiteral(self, ast, o):
        return FloatType()
    
    # value:bool
    def visitBooleanLiteral(self, ast, o):
        return BoolType()
    
    # value:str
    def visitStringLiteral(self, ast, o):
        return StringType()

    # value:List[Literal]
    def visitArrayLiteral(self, ast, o):
        dimen = []
        ele = ast.value
        astEle = ast.value
        while isinstance(ele, list):
            dimen += [len(ele)]
            astEle = ele
            ele = ele[0].value if ele else None
        else:
            eleType = self.visit(astEle[0], o) if ast.value and astEle else Unknown()
            return ArrayType(dimen, eleType) if dimen else ArrayType([0], eleType)