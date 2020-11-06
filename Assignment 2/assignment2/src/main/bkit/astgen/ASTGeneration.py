from typing import BinaryIO
from BKITVisitor import BKITVisitor
from BKITParser import BKITParser
from AST import *
from main.bkit.utils.AST import BinaryOp, CallExpr, FuncDecl, VarDecl
# from test2string.ASTString import *
from functools import reduce

class ASTGeneration(BKITVisitor):
    # program  : (global_var_declare)* function_declare* EOF;
    def visitProgram(self, ctx:BKITParser.ProgramContext):
        lstVarDecl = []
        lstFuncDecl = []
        if ctx.global_var_declare(): # global_var_declare() is a list of list
            lstVarDecl = reduce(lambda x, y: x + self.visit(y) ,ctx.global_var_declare()[1:],self.visit(ctx.global_var_declare(0)))
        if ctx.function_declare():
            lstFuncDecl = [self.visit(x) for x in ctx.function_declare()]
        return Program(lstVarDecl + lstFuncDecl)


    # global_var_declare: VAR COLON var_list SEMI;
    def visitGlobal_var_declare(self, ctx:BKITParser.Global_var_declareContext):
        return self.visit(ctx.var_list())

    # var_list: var_def (COMMA var_def)*;
    def visitVar_list(self, ctx:BKITParser.Var_listContext):
        return [self.visit(x) for x in ctx.var_def()]


    # var_def: variable (ASSIGN init_value)?; // variable = initial-value
    def visitVar_def(self, ctx:BKITParser.Var_defContext):
        identify = self.visit(ctx.variable())[0]
        dimension = self.visit(ctx.variable())[1]
        return VarDecl(Id(identify), dimension, self.visit(ctx.init_value()) if ctx.init_value() else None)


    # variable: (scalar_var | composite_var); // 2 type scalar and composite
    def visitVariable(self, ctx:BKITParser.VariableContext):
        if ctx.scalar_var():
            return (self.visit(ctx.scalar_var()),[])
        else:
            return self.visit(ctx.composite_var())


    # scalar_var: ID;
    def visitScalar_var(self, ctx:BKITParser.Scalar_varContext):
        return ctx.ID().getText()


    # composite_var: ID dimension+;
    def visitComposite_var(self, ctx:BKITParser.Composite_varContext):
        return (ctx.ID().getText(), [self.visit(x) for x in ctx.dimension()])


    # dimension: (LSQUARE INT_LIT RSQUARE);
    def visitDimension(self, ctx:BKITParser.DimensionContext):
        return int(eval(ctx.INT_LIT().getText()))


    # init_value: literal;
    def visitInit_value(self, ctx:BKITParser.Init_valueContext):
        return self.visit(ctx.literal())


    # literal // literal type
    # : INT_LIT 
    # | FLOAT_LIT 
    # | STRING_LIT 
    # | bool_literal
    # | array_literal
    # ;
    def visitLiteral(self, ctx:BKITParser.LiteralContext):
        if ctx.INT_LIT():
            return IntLiteral(int(eval(ctx.INT_LIT().getText())))
        elif ctx.FLOAT_LIT():
            return FloatLiteral(float(ctx.FLOAT_LIT().getText()))
        elif ctx.STRING_LIT():
            return StringLiteral(ctx.STRING_LIT().getText())
        elif ctx.bool_literal():
            return BooleanLiteral(self.visit(ctx.bool_literal()))
        return self.visit(ctx.array_literal())


    # array_literal: LCURLY array_element_list? RCURLY;
    def visitArray_literal(self, ctx:BKITParser.Array_literalContext):
        if ctx.array_element_list():
            return ArrayLiteral(self.visit(ctx.array_element_list()))
        else:
            return ArrayLiteral([])


    # array_element_list: array_element (COMMA array_element)*;
    def visitArray_element_list(self, ctx:BKITParser.Array_element_listContext):
        return [self.visit(x) for x in ctx.array_element()]


    # array_element: literal;
    def visitArray_element(self, ctx:BKITParser.Array_elementContext):
        return self.visit(ctx.literal())


    # bool_literal: TRUE | FALSE;
    def visitBool_literal(self, ctx:BKITParser.Bool_literalContext):
        if ctx.TRUE():
            return True
        else:
            return False


    # function_declare: FUNCTION COLON ID (PARAMETER COLON parameter_list)? BODY COLON statement_list END_BODY DOT;
    def visitFunction_declare(self, ctx:BKITParser.Function_declareContext):
        if ctx.parameter_list():
            param = self.visit(ctx.parameter_list())
        else:
            param = []
        return FuncDecl(Id(ctx.ID().getText()), param, self.visit(ctx.statement_list()))


    # parameter_list: parameter (COMMA parameter)*;
    def visitParameter_list(self, ctx:BKITParser.Parameter_listContext):
        return [self.visit(x) for x in ctx.parameter()]


    # parameter: variable; // 'variable' in Global variable declaration part
    def visitParameter(self, ctx:BKITParser.ParameterContext):
        identify = self.visit(ctx.variable())[0]
        dimension = self.visit(ctx.variable())[1]
        return VarDecl(Id(identify), dimension, None)


    # statement_list
    #     : local_var_declare* 
    #     ( assignment_statement
    #     | if_statement 
    #     | for_statement 
    #     | while_statement
    #     | do_while_statement
    #     | break_statement
    #     | continue_statement
    #     | call_statement
    #     | return_statement
    #     )*
    # ;
    def loadLst(self, typeLst):
        return [self.visit(x) for x in typeLst] if typeLst else []


    def visitStatement_list(self, ctx:BKITParser.Statement_listContext):
        # VarDeclare statements
        lstVarDeclStm = []
        if ctx.local_var_declare(): # local_var_declare() is a list of list
            lstVarDeclStm = reduce(lambda x, y: x + self.visit(y) ,ctx.local_var_declare()[1:],self.visit(ctx.local_var_declare(0)))
        # And statements rest
        lstAssignmentStm = self.loadLst(ctx.assignment_statement())
        lstIfStm = self.loadLst(ctx.if_statement())
        lstForStm = self.loadLst(ctx.for_statement())
        lstWhileStm = self.loadLst(ctx.while_statement())
        lstDoWhileStm = self.loadLst(ctx.do_while_statement())
        lstBreakStm = self.loadLst(ctx.break_statement())
        lstContinueStm = self.loadLst(ctx.continue_statement())
        lstCallStm = self.loadLst(ctx.call_statement())
        lstReturnStm = self.loadLst(ctx.return_statement())
        return (lstVarDeclStm, lstAssignmentStm + lstIfStm + lstForStm + lstWhileStm + lstDoWhileStm + lstBreakStm + lstContinueStm + lstCallStm + lstReturnStm)


    # local_var_declare: global_var_declare;
    def visitLocal_var_declare(self, ctx:BKITParser.Local_var_declareContext):
        return self.visit(ctx.global_var_declare())


    # assignment_statement: (scalar_var | exp7 index_operator) ASSIGN expression SEMI;
    def visitAssignment_statement(self, ctx:BKITParser.Assignment_statementContext):
        if ctx.scalar_var():
            lhs = Id(self.visit(ctx.scalar_var()))
        else:
            lhs = ArrayCell(self.visit(ctx.exp7()), self.visit(ctx.index_operator()))
        expr = self.visit(ctx.expression())
        return Assign(lhs, expr)


    # if_statement
    # :
    #     IF expression THEN statement_list
    #     (ELSE_IF expression THEN statement_list)*
    #     (ELSE statement_list)?
    #     END_IF DOT
    # ;
    def visitIf_statement(self, ctx:BKITParser.If_statementContext):
        lstVarDecl = [self.visit(x)[0] for x in ctx.statement_list()]
        lstStm = [self.visit(x)[1] for x in ctx.statement_list()]
        lstExpr = [self.visit(x) for x in ctx.expression()]
        lstIfThenStm = list(zip(lstExpr, lstVarDecl, lstStm))
        if ctx.ELSE():
            lstElseStm = self.visit(ctx.statement_list()[-1])
        else:
            lstElseStm = ()
        return If(lstIfThenStm, lstElseStm)


    # for_statement
    # :
    #     FOR LPAREN scalar_var ASSIGN initExpr COMMA conditionExpr COMMA updateExpr RPAREN DO
    #         statement_list
    #     END_FOR DOT
    # ;
    def visitFor_statement(self, ctx:BKITParser.For_statementContext):
        identify = Id(self.visit(ctx.scalar_var()))
        init = self.visit(ctx.initExpr())
        condition = self.visit(ctx.conditionExpr())
        update =self.visit(ctx.updateExpr())
        stm = self.visit(ctx.statement_list())
        return For(identify, init, condition, update, stm)


    # initExpr: expression;
    def visitInitExpr(self, ctx:BKITParser.InitExprContext):
        return self.visit(ctx.expression())


    # conditionExpr: expression;
    def visitConditionExpr(self, ctx:BKITParser.ConditionExprContext):
        return self.visit(ctx.expression())

    # updateExpr: expression;
    def visitUpdateExpr(self, ctx:BKITParser.UpdateExprContext):
        return self.visit(ctx.expression())


    # while_statement: WHILE expression DO statement_list END_WHITE DOT;
    def visitWhile_statement(self, ctx:BKITParser.While_statementContext):
        return While(self.visit(ctx.expression()), self.visit(ctx.statement_list()))


    # do_while_statement: DO statement_list WHILE expression END_DO DOT;
    def visitDo_while_statement(self, ctx:BKITParser.Do_while_statementContext):
        return Dowhile(self.visit(ctx.statement_list()), self.visit(ctx.expression()))


    # break_statement: BREAK SEMI;
    def visitBreak_statement(self, ctx:BKITParser.Break_statementContext):
        return Break()


    # continue_statement: CONTINUTE SEMI;
    def visitContinue_statement(self, ctx:BKITParser.Continue_statementContext):
        return Continue()


    # call_statement: function_call SEMI;
    def visitCall_statement(self, ctx:BKITParser.Call_statementContext):
        identify = self.visit(ctx.function_call())[0]
        param = self.visit(ctx.function_call())[1]
        return CallStmt(identify, param)


    # return_statement: RETURN expression? SEMI;
    def visitReturn_statement(self, ctx:BKITParser.Return_statementContext):
        if ctx.expression():
            return Return(self.visit(ctx.expression()))
        else:
            return Return(None)


    # expression //lowest
    # : exp1 relational_operator exp1 
    # | exp1
    # ;
    def visitExpression(self, ctx:BKITParser.ExpressionContext):
        if ctx.getChildCount() == 3:
            return BinaryOp(
                self.visit(ctx.relational_operator()), \
                self.visit(ctx.exp1(0)), \
                self.visit(ctx.exp1(1))
            )
        else:
            return self.visit(ctx.exp1(0))


    # exp1
    # : exp1 (AND | OR) exp2 
    # | exp2
    # ;
    def visitExp1(self, ctx:BKITParser.Exp1Context):
        if ctx.getChildCount() == 3:
            return BinaryOp(
                ctx.AND().getText() if ctx.AND() else ctx.OR().getText(), \
                self.visit(ctx.exp1()), \
                self.visit(ctx.exp2())
            )    
        else:
            return self.visit(ctx.exp2())


    # exp2
    # : exp2 adding exp3 
    # | exp3
    # ;
    def visitExp2(self, ctx:BKITParser.Exp2Context):
        if ctx.getChildCount() == 3:
            return BinaryOp(
                self.visit(ctx.adding()), \
                self.visit(ctx.exp2()), \
                self.visit(ctx.exp3())
            )   
        else:
            return self.visit(ctx.exp3())


    # exp3
    # : exp3 multiplying exp4 
    # | exp4
    # ;
    def visitExp3(self, ctx:BKITParser.Exp3Context):
        if ctx.getChildCount() == 3:
            return BinaryOp(
                self.visit(ctx.multiplying()), \
                self.visit(ctx.exp3()), \
                self.visit(ctx.exp4())
            ) 
        else:
            return self.visit(ctx.exp4())

    # exp4
    # : NOT exp4 
    # | exp5
    # ;
    def visitExp4(self, ctx:BKITParser.Exp4Context):
        if ctx.getChildCount() == 2:
            return UnaryOp(
                ctx.NOT().getText(), \
                self.visit(ctx.exp4())
            )
        else:
            return self.visit(ctx.exp5())


    # exp5
    # : sign exp5
    # | exp6
    # ;
    def visitExp5(self, ctx:BKITParser.Exp5Context):
        if ctx.getChildCount() == 2:
            return UnaryOp(
                self.visit(ctx.sign()), \
                self.visit(ctx.exp5()) \
            )
        else:
            return self.visit(ctx.exp6())


    # exp6
    # : exp6 index_operator
    # | exp7
    # ;
    def visitExp6(self, ctx:BKITParser.Exp6Context):
        if ctx.getChildCount() == 2:
            return UnaryOp(
                self.visit(ctx.index_operator()), \
                self.visit(ctx.exp6())
            )   
        else:
            return self.visit(ctx.exp7())


    # exp7
    # : function_call
    # | exp8
    # ;
    def visitExp7(self, ctx:BKITParser.Exp7Context):
        if ctx.exp8():
            return self.visit(ctx.exp8())
        else:
            identify = self.visit(ctx.function_call())[0]
            param = self.visit(ctx.function_call())[1]
            return CallExpr(identify, param)


    # exp8
    # : LPAREN expression RPAREN
    # | operand
    # ;
    def visitExp8(self, ctx:BKITParser.Exp8Context):
        if ctx.getChildCount() == 3:
            return self.visit(ctx.expression())
        else:
            return self.visit(ctx.operand())


    # operand
    # : literal
    # | ID
    # ;
    def visitOperand(self, ctx:BKITParser.OperandContext):
        if ctx.literal():
            return self.visit(ctx.literal())
        else:
            return Id(ctx.ID().getText())


    # adding
    # : ADD
    # | SUB
    # | ADD_FLOAT
    # | SUB_FLOAT
    # ;
    def visitAdding(self, ctx:BKITParser.AddingContext):
        if ctx.ADD():
            return ctx.ADD().getText()
        elif ctx.SUB():
            return ctx.SUB().getText()
        elif ctx.ADD_FLOAT():
            return ctx.ADD_FLOAT().getText()
        else:
            return ctx.SUB_FLOAT().getText()

    # multiplying
    # : MUL
    # | DIV
    # | MOD
    # | MUL_FLOAT
    # | DIV_FLOAT
    # ;
    def visitMultiplying(self, ctx:BKITParser.MultiplyingContext):
        if ctx.MUL():
            return ctx.MUL().getText()
        elif ctx.DIV():
            return ctx.DIV().getText()
        elif ctx.MOD():
            return ctx.MOD().getText()
        elif ctx.MUL_FLOAT():
            return ctx.MUL_FLOAT().getText()
        else:
            return ctx.DIV_FLOAT().getText()



    # relational_operator
    # : EQUAL
    # | NOT_EQUAL
    # | LESS_THAN
    # | MORE_THAN
    # | LESS_THAN_EQUAL
    # | MORE_THAN_EQUAL
    # | NOT_EQUAL_FLOAT
    # | LESS_THAN_FLOAT
    # | MORE_THAN_FLOAT
    # | LESS_THAN_EQUAL_FLOAT
    # | MORE_THAN_EQUAL_FLOAT
    # ;
    def visitRelational_operator(self, ctx:BKITParser.Relational_operatorContext):
        if ctx.EQUAL():
            return ctx.EQUAL().getText()
        elif ctx.NOT_EQUAL():
            return ctx.NOT_EQUAL().getText()
        elif ctx.LESS_THAN():
            return ctx.LESS_THAN().getText()
        elif ctx.MORE_THAN():
            return ctx.MORE_THAN().getText()
        elif ctx.LESS_THAN_FLOAT():
            return ctx.LESS_THAN_FLOAT().getText()
        elif ctx.MORE_THAN_FLOAT():
            return ctx.MORE_THAN_FLOAT().getText()
        elif ctx.NOT_EQUAL_FLOAT():
            return ctx.NOT_EQUAL_FLOAT().getText()
        elif ctx.LESS_THAN_EQUAL():
            return ctx.LESS_THAN_EQUAL().getText()
        elif ctx.MORE_THAN_EQUAL():
            return ctx.MORE_THAN_EQUAL().getText()
        elif ctx.LESS_THAN_EQUAL_FLOAT():
            return ctx.LESS_THAN_EQUAL_FLOAT().getText()
        else:
            return ctx.MORE_THAN_EQUAL_FLOAT().getText()


    # sign
    # : SUB 
    # | SUB_FLOAT
    # ;
    def visitSign(self, ctx:BKITParser.SignContext):
        if ctx.SUB():
            return ctx.SUB().getText()
        else:
            return ctx.SUB_FLOAT().getText()


    # index_operator //6.4 Index operators
    # : (LSQUARE expression RSQUARE)+
    # ; 
    def visitIndex_operator(self, ctx:BKITParser.Index_operatorContext):
        return [self.visit(x) for x in ctx.expression()] 


    # function_call // 6.5 Function call
    # : ID LPAREN argument_list RPAREN
    # ;
    def visitFunction_call(self, ctx:BKITParser.Function_callContext):
        return (Id(ctx.ID().getText()), self.visit(ctx.argument_list()))


    # argument_list: expression? (COMMA expression)*;
    def visitArgument_list(self, ctx:BKITParser.Argument_listContext):
        if ctx.expression():
            return [self.visit(x) for x in ctx.expression()]
        else: 
            return []
    

