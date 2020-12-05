
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
    
    def updateTypeInEnv(self, key, value, env):
        for x in env:
            if type(x.mtype) == MType:
                if x.name == key:
                    if type(x.mtype.restype) == ArrayType:
                        x.mtype.restype.eletype = key
                    else:
                        x.mtype.restype = key

            elif type(x.mtype) == ArrayType:
                if x.name == key:
                    x.mtype.eletype = value

            else:
                if x.name == key:
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
        else:
            if type(mtype) == ArrayType:
                if arrayTypeFlag:
                    return mtype
                return mtype.eletype
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

    # decl : List[Decl]
    def visitProgram(self, ast, o):
        innerEnv = [] + []
        programEnv = reduce(lambda env, ele: [self.visit(ele, env)] + env if isinstance(ele, VarDecl) else [self.traverseFunc(ele, env)] + env, ast.decl, innerEnv)
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
            typeInit = ArrayType(ast.varDimen, self.visit(ast.varInit, o) if ast.varInit else Unknown())
        else:
            typeInit = self.visit(ast.varInit, o) if ast.varInit else Unknown()

        return Symbol(varName, typeInit)
    
    # name: Id
    # param: List[VarDecl]
    # body: Tuple[List[VarDecl],List[Stmt]]
    def visitFuncDecl(self, ast, o):
        lstParam = reduce(lambda env, ele: env + [self.visit(ele, env)]  \
        if not self.matchNameInEnv('all', ele.variable.name, env) \
            else self.raise_(Redeclared(Parameter(), ele.variable.name)) ,\
                ast.param, [])

        lstVarDecl = reduce(lambda env, ele: [self.visit(ele, env)] + env, ast.body[0], [])
        innerEnv = lstParam + lstVarDecl
        funcEnv = self.createNewEnv(o, innerEnv)
        [self.visit(x, funcEnv) for x in ast.body[1]]

        self.updateOldEnv(lstParam, [], funcEnv) # Update param with func env
        lstParamType = [x.mtype for x in lstParam]
        self.updateParamInEnv(ast.name.name, lstParamType, o)
        self.updateOldEnv(o, innerEnv, funcEnv)
    
    # op:str
    # left:Expr
    # right:Expr
    def visitBinaryOp(self, ast, o):
        left = self.visit(ast.left, o)
        right = self.visit(ast.right, o)

        if ast.op in ['+','-','*','\\','%']:
            if type(left) == Unknown:
                left = IntType()
                self.updateTypeInEnv(self.getNameOfAst(ast.left), IntType, o)
            if type(right) == Unknown:
                right = IntType()
                self.updateTypeInEnv(self.getNameOfAst(ast.right), IntType, o)
            if type(left) != IntType or type(right) != IntType:
                raise TypeMismatchInExpression(ast)
            return IntType()

        elif ast.op in ['+.','-.','*.','\\.']:
            if type(left) == Unknown:
                left = FloatType()
                self.updateTypeInEnv(self.getNameOfAst(ast.left), FloatType, o)
            if type(right) == Unknown:
                right = FloatType()
                self.updateTypeInEnv(self.getNameOfAst(ast.right), FloatType, o)
            if type(left) != FloatType or type(right) != FloatType:
                raise TypeMismatchInExpression(ast)
            return FloatType()

        elif ast.op in ['&&','||']:
            if type(left) == Unknown:
                left = BoolType()
                self.updateTypeInEnv(self.getNameOfAst(ast.left), BoolType, o)
            if type(right) == Unknown:
                right = BoolType()
                self.updateTypeInEnv(self.getNameOfAst(ast.right), BoolType, o)
            if type(left) != BoolType or type(right) != BoolType:
                raise TypeMismatchInExpression(ast)
            return BoolType()

        elif ast.op in ['==','!=','<','>','<=','>=']:
            if type(left) == Unknown:
                left = IntType()
                self.updateTypeInEnv(self.getNameOfAst(ast.left), IntType, o)
            if type(right) == Unknown:
                right = IntType()
                self.updateTypeInEnv(self.getNameOfAst(ast.right), IntType, o)
            if type(left) != IntType or type(right) != IntType:
                raise TypeMismatchInExpression(ast)
            return BoolType()

        elif ast.op in ['=/=','<.','>.','<=.','>=.']:
            if type(left) == Unknown:
                left = FloatType()
                self.updateTypeInEnv(self.getNameOfAst(ast.left), FloatType, o)
            if type(right) == Unknown:
                right = FloatType()
                self.updateTypeInEnv(self.getNameOfAst(ast.right), FloatType, o)
            if type(left) != FloatType or type(right) != FloatType:
                raise TypeMismatchInExpression(ast)
            return BoolType()
    
    # op:str
    # body:Expr    
    def visitUnaryOp(self, ast, o):
        body = ast.body
        if ast.op == '-':
            if type(body) == Unknown:
                body = IntType()
                self.updateTypeInEnv(self.getNameOfAst(ast.body), IntType, o)
            if type(body) != IntType:
                raise TypeMismatchInExpression(ast)
            return IntType()
        elif ast.op == '-.':
            if type(body) == Unknown:
                body = FloatType()
                self.updateTypeInEnv(self.getNameOfAst(ast.body), FloatType, o)
            if type(body) != FloatType:
                raise TypeMismatchInExpression(ast)
            return FloatType()
        elif ast.op == '!':
            if type(body) == Unknown:
                body = BoolType()
                self.updateTypeInEnv(self.getNameOfAst(ast.body), FloatType, o)
            if type(body) != BoolType:
                raise TypeMismatchInExpression(ast)
            return BoolType()
    
    # method:Id
    # param:List[Expr]
    def visitCallExpr(self, ast, o):
        funcName = ast.method.name
        if not self.matchNameInEnv('func', funcName, o):
            return Undeclared(Function(), funcName)

        lstArg = [self.visit(ele, o) for ele in ast.param]
        lstParam = [type(ele) for ele in self.lookup(funcName, o, lambda x: x.name).mtype.intype]

        if len(lstArg) != len(lstParam):
            raise TypeMismatchInExpression(ast)
        for i in range(len(lstArg)):
            if type(lstParam[i]) == Unknown() and type(lstArg[i]) != Unknown:
                lstParam[i] = lstArg[i]
            elif type(lstArg[i]) == Unknown and type(lstParam[i]) != Unknown():
                lstArg[i] = lstParam[i]
                self.updateTypeInEnv(self.getNameOfAst(ast.param[i]), lstParam[i], o)
            else:
                raise TypeCannotBeInferred(ast)
        self.updateParamInEnv(funcName, lstParam, o)
        
        return self.getTypeInEnv(funcName, o, True)
    
    # name : str
    def visitId(self, ast, o):
        varName = ast.name
        if not self.matchNameInEnv('var', varName, o):
            return Undeclared(Variable(), varName)
        return self.getTypeInEnv(varName, o, True)
    
    # arr:Expr
    # idx:List[Expr]
    def visitArrayCell(self, ast, o):
        return self.visit(ast.arr, o).eletype
    
    # lhs: LHS
    # rhs: Expr    
    def visitAssign(self, ast, o):
        lhs = self.visit(ast.lhs, o)
        rhs = self.visit(ast.rhs, o)
        if type(lhs) == Unknown and type(rhs) == Unknown:
            raise(TypeCannotBeInferred(ast))
        if type(lhs) == Unknown:
            lhs = rhs
            self.updateTypeInEnv(self.getNameOfAst(ast.lhs), rhs, o)
        elif type(rhs) == Unknown:
            rhs = lhs
            self.updateTypeInEnv(self.getNameOfAst(ast.rhs), lhs, o)
        if type(self.visit(ast.lhs, o)) != type(self.visit(ast.lhs, o)):
            raise TypeMismatchInStatement(ast)
    
    # ifthenStmt:List[Tuple[Expr,List[VarDecl],List[Stmt]]]
    # elseStmt:Tuple[List[VarDecl],List[Stmt]]
    def visitIf(self, ast, o):
        return None

    # idx1: Id
    # expr1:Expr
    # expr2:Expr
    # expr3:Expr
    # loop: Tuple[List[VarDecl],List[Stmt]]    
    def visitFor(self, ast, o):
        return None
    
    def visitContinue(self, ast, o):
        return None
    
    def visitBreak(self, ast, o):
        return None
    
    # expr:Expr
    def visitReturn(self, ast, o):
        if ast.expr:
            return self.visit(expr, o)
        return VoidType()
    
    # sl:Tuple[List[VarDecl],List[Stmt]]
    # exp: Expr
    def visitDowhile(self, ast, o):
        return None

    # exp: Expr
    # sl:Tuple[List[VarDecl],List[Stmt]]
    def visitWhile(self, ast, o):
        return None

    # method:Id
    # param:List[Expr]
    def visitCallStmt(self, ast, o):
        funcName = ast.method.name
        if not self.matchNameInEnv('func', funcName, o):
            return Undeclared(Function(), funcName)
        return self.getTypeInEnv(funcName, o, True)
    
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
        return self.visit(ast.value[0], ast) if ast.value else Unknown()