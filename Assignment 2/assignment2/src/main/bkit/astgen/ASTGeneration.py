from BKITVisitor import BKITVisitor
from BKITParser import BKITParser
from AST import *
from functools import reduce

from main.bkit.utils.AST import FuncDecl, VarDecl

class ASTGeneration(BKITVisitor):
    # program  : (global_var_declare)* function_declare* EOF;
    def visitProgram(self, ctx:BKITParser.ProgramContext):
        lstVarDecl = []
        lstFuncDecl = []
        if ctx.global_var_declare():
            lstVarDecl = reduce(lambda x, y: x + self.visit(y) ,ctx.global_var_declare()[1:],self.visit(ctx.global_var_declare(0)))
        if ctx.function_declare():
            lstFuncDecl = reduce(lambda x, y: x + self.visit(y) ,ctx.function_declare()[1:],self.visit(ctx.function_declare(0)))
        return Program(lstVarDecl + lstFuncDecl)


    # global_var_declare: VAR COLON var_list SEMI;
    def visitGlobal_var_declare(self, ctx:BKITParser.Global_var_declareContext):
        return self.visit(ctx.var_list())

    # var_list: var_def (COMMA var_def)*;
    def visitVar_list(self, ctx:BKITParser.Var_listContext):
        return [self.visit(x) for x in ctx.var_def()]


    # var_def: variable (ASSIGN init_value)?; // variable = initial-value
    def visitVar_def(self, ctx:BKITParser.Var_defContext):
        id = self.visit(ctx.variable())[0]
        dimension = self.visit(ctx.variable())[1]
        return VarDecl(Id(id), dimension, self.visit(ctx.init_value()) if ctx.init_value() else None)


    # variable: (scalar_var | composite_var); // 2 type scalar and composite
    def visitVariable(self, ctx:BKITParser.VariableContext):
        if ctx.scalar_var():
            return self.visit(ctx.scalar_var())
        else:
            return self.visit(ctx.composite_var())


    # scalar_var: ID;
    def visitScalar_var(self, ctx:BKITParser.Scalar_varContext):
        return (ctx.ID().getText(), [])


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
            return IntLiteral(int(ctx.INT_LIT().getText()))
        elif ctx.FLOAT_LIT():
            return FloatLiteral(float(ctx.FLOAT_LIT().getText()))
        elif ctx.STRING_LIT():
            return StringLiteral(ctx.STRING_LIT().getText())
        elif ctx.bool_literal():
            return BooleanLiteral(bool(self.visit(ctx.bool_literal())))
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
            return ctx.TRUE().getText()
        else:
            return ctx.FALSE().getText()


    # function_declare: FUNCTION COLON ID (PARAMETER COLON parameter_list)? BODY COLON statement_list END_BODY DOT;
    def visitFunction_declare(self, ctx:BKITParser.Function_declareContext):
        param = self.visit(ctx.parameter_list)
        return FuncDecl(ctx.ID().getText(), param if param else [], self.visit(ctx.statement_list()))


    # parameter_list: parameter (COMMA parameter)*;
    def visitParameter_list(self, ctx:BKITParser.Parameter_listContext):
        return [self.visit(x) for x in ctx.parameter()]


    # parameter: variable; // 'variable' in Global variable declaration part
    def visitParameter(self, ctx:BKITParser.ParameterContext):
        id = self.visit(ctx.variable())[0]
        dimension = self.visit(ctx.variable())[1]
        return VarDecl(Id(id), dimension, None)


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
        lstVarDeclStm = self.loadLst(ctx.local_var_declare())
        # lstAssignmentStm = [self.visit(x) for x in ctx.assignment_statement()] if ctx.assignment_statement() else []
        # lstIfStm = self.visit(ctx.if_statement()) if ctx.if_statement() else []
        # lstForStm = self.visit(ctx.for_statement()) if ctx.for_statement() else []
        # lstWhileStm = self.visit(ctx.while_statement()) if ctx.while_statement() else []
        # lstDoWhileStm = self.visit(ctx.do_while_statement()) if ctx.do_while_statement() else []
        # lstBreakStm = self.visit(ctx.break_statement()) if ctx.break_statement() else []
        # lstContinueStm = [self.visit(x) for x in ctx.continue_statement()] if ctx.continue_statement() else []
        # lstCallStm = self.visit(ctx.call_statement())
        # lstReturnStm = self.visit(ctx.return_statement())
        return (lstVarDeclStm, [])


    # local_var_declare: global_var_declare;
    def visitLocal_var_declare(self, ctx:BKITParser.Local_var_declareContext):
        return self.visitChildren(ctx)


    # assignment_statement: (scalar_var index_operator?) ASSIGN expression SEMI;
    def visitAssignment_statement(self, ctx:BKITParser.Assignment_statementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKITParser#if_statement.
    def visitIf_statement(self, ctx:BKITParser.If_statementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKITParser#for_statement.
    def visitFor_statement(self, ctx:BKITParser.For_statementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKITParser#initExpr.
    def visitInitExpr(self, ctx:BKITParser.InitExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKITParser#conditionExpr.
    def visitConditionExpr(self, ctx:BKITParser.ConditionExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKITParser#updateExpr.
    def visitUpdateExpr(self, ctx:BKITParser.UpdateExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKITParser#while_statement.
    def visitWhile_statement(self, ctx:BKITParser.While_statementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKITParser#do_while_statement.
    def visitDo_while_statement(self, ctx:BKITParser.Do_while_statementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKITParser#break_statement.
    def visitBreak_statement(self, ctx:BKITParser.Break_statementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKITParser#continue_statement.
    def visitContinue_statement(self, ctx:BKITParser.Continue_statementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKITParser#call_statement.
    def visitCall_statement(self, ctx:BKITParser.Call_statementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKITParser#return_statement.
    def visitReturn_statement(self, ctx:BKITParser.Return_statementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKITParser#expression.
    def visitExpression(self, ctx:BKITParser.ExpressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKITParser#exp1.
    def visitExp1(self, ctx:BKITParser.Exp1Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKITParser#exp2.
    def visitExp2(self, ctx:BKITParser.Exp2Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKITParser#exp3.
    def visitExp3(self, ctx:BKITParser.Exp3Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKITParser#exp4.
    def visitExp4(self, ctx:BKITParser.Exp4Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKITParser#exp5.
    def visitExp5(self, ctx:BKITParser.Exp5Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKITParser#exp6.
    def visitExp6(self, ctx:BKITParser.Exp6Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKITParser#exp7.
    def visitExp7(self, ctx:BKITParser.Exp7Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKITParser#exp8.
    def visitExp8(self, ctx:BKITParser.Exp8Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKITParser#operand.
    def visitOperand(self, ctx:BKITParser.OperandContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKITParser#adding.
    def visitAdding(self, ctx:BKITParser.AddingContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKITParser#multiplying.
    def visitMultiplying(self, ctx:BKITParser.MultiplyingContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKITParser#relational_operator.
    def visitRelational_operator(self, ctx:BKITParser.Relational_operatorContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKITParser#sign.
    def visitSign(self, ctx:BKITParser.SignContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKITParser#index_operator.
    def visitIndex_operator(self, ctx:BKITParser.Index_operatorContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKITParser#function_call.
    def visitFunction_call(self, ctx:BKITParser.Function_callContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKITParser#argument_list.
    def visitArgument_list(self, ctx:BKITParser.Argument_listContext):
        return self.visitChildren(ctx)
    
