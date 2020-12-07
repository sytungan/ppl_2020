import unittest
from TestUtils import TestChecker
from StaticError import *
from AST import *

class CheckSuite(unittest.TestCase):

    def test_undeclared_function1(self):
        """Simple program: main"""
        input = """
        Var: a;
        Function: main
            Body:
                a = foo();
            EndBody.

        Function: foo
            Body:
                Return 1;
            EndBody.
                """
        expect = str(Undeclared(Function(),"foo"))
        self.assertTrue(TestChecker.test(input,expect,400))
   
    # def test_undeclared_function2(self):
    #     """Simple program: main"""
    #     input = """
    #         Function: foo
    #             Body:
    #                 Var: x[5];
    #                 Return x;
    #             EndBody.

    #         Function: main
    #             Body:
    #                 Var: y[5] = {1, 2, 4, 5};
    #                 foo()[2] = 2;
    #                 y = foo();
    #             EndBody.
    #             """
    #     expect = str(Undeclared(Function(),"foo"))
    #     self.assertTrue(TestChecker.test(input,expect,406))

    # def test_diff_numofparam_stmt(self):
    #     """Complex program"""
    #     input = """Function: main  
    #                Body:
    #                     printStrLn();
    #                 EndBody."""
    #     expect = str(TypeMismatchInStatement(CallStmt(Id("printStrLn"),[])))
    #     self.assertTrue(TestChecker.test(input,expect,401))
    
    # def test_diff_numofparam_expr(self):
    #     """More complex program"""
    #     input = """Function: main 
    #                 Body:
    #                     printStrLn(read(4));
    #                 EndBody."""
    #     expect = str(TypeMismatchInExpression(CallExpr(Id("read"),[IntLiteral(4)])))
    #     self.assertTrue(TestChecker.test(input,expect,402))

    # def test_undeclared_function_use_ast(self):
    #     """Simple program: main """
    #     input = Program([FuncDecl(Id("main"),[],([],[
    #         CallExpr(Id("foo"),[])]))])
    #     expect = str(Undeclared(Function(),"foo"))
    #     self.assertTrue(TestChecker.test(input,expect,403))

    # def test_diff_numofparam_expr_use_ast(self):
    #     """More complex program"""
    #     input = Program([
    #             FuncDecl(Id("main"),[],([],[
    #                 CallStmt(Id("printStrLn"),[
    #                     CallExpr(Id("read"),[IntLiteral(4)])
    #                     ])]))])
    #     expect = str(TypeMismatchInExpression(CallExpr(Id("read"),[IntLiteral(4)])))
    #     self.assertTrue(TestChecker.test(input,expect,404))

    # def test_diff_numofparam_stmt_use_ast(self):
    #     """Complex program"""
    #     input = Program([
    #             FuncDecl(Id("main"),[],([],[
    #                 CallStmt(Id("printStrLn"),[])]))])
    #     expect = str(TypeMismatchInStatement(CallStmt(Id("printStrLn"),[])))
    #     self.assertTrue(TestChecker.test(input,expect,405))