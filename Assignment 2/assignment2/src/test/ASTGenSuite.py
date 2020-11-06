import unittest
from TestUtils import TestAST
from AST import *

from main.bkit.utils.AST import ArrayLiteral, BooleanLiteral, FloatLiteral, IntLiteral, Program, StringLiteral

class ASTGenSuite(unittest.TestCase):
    def test_simple_program(self):
        input = """Var:x;"""
        expect = Program([VarDecl(Id("x"),[],None)])
        self.assertTrue(TestAST.checkASTGen(input,expect,300))

    def test_simple_program1(self):
        input = """Var:x =5 ;"""
        expect = Program([VarDecl(Id("x"),[],IntLiteral(5))])
        self.assertTrue(TestAST.checkASTGen(input,expect,301))
    
    def test_simple_program2(self):
        input = """Var:x[12];"""
        expect = Program([VarDecl(Id("x"),[12],None)])
        self.assertTrue(TestAST.checkASTGen(input,expect,302))
    
    def test_simple_program3(self):
        input = """Var:x[0x13];"""
        expect = Program([VarDecl(Id("x"),[19],None)])
        self.assertTrue(TestAST.checkASTGen(input,expect,303))
    
    def test_simple_program4(self):
        input = """Var:x[1][13][16]=5;"""
        expect = Program([VarDecl(Id("x"),[1,13,16],IntLiteral(5))])
        self.assertTrue(TestAST.checkASTGen(input,expect,304))
 
    def test_simple_program5(self):
        input = """Var: arr[5][6] = {1,2}, y[1];"""
        expect = Program([VarDecl(Id("arr"),[5,6],ArrayLiteral([IntLiteral(1),IntLiteral(2)])),VarDecl(Id("y"),[1],None)])
        self.assertTrue(TestAST.checkASTGen(input,expect,305))

    def test_simple_program6(self):
        input = """Var: x[5] = {1,2,"h",2.e56,""}, y = 12.;"""
        expect = Program([VarDecl(Id("x"),[5],ArrayLiteral([IntLiteral(1),IntLiteral(2),StringLiteral("h"),FloatLiteral(2.e56),StringLiteral("")])),VarDecl(Id("y"),[],FloatLiteral(12.))])
        self.assertTrue(TestAST.checkASTGen(input,expect,306))

    def test_simple_program7(self):
        input = """Var: b = True, c = False;"""
        expect = Program([VarDecl(Id("b"),[],BooleanLiteral(True)),VarDecl(Id("c"),[],BooleanLiteral(False))])
        self.assertTrue(TestAST.checkASTGen(input,expect,306))
    
    def test_func_declare1(self):
        input = """ Function: foo
                        Parameter: a
                        Body:
                        Var: x = 2;
                        EndBody.
                """
        expect = Program([FuncDecl(Id("foo"),[VarDecl(Id("a"),[],None)],(([VarDecl(Id("x"),[],IntLiteral(2))],[])))])
        self.assertTrue(TestAST.checkASTGen(input,expect,307))
 
    def test_func_declare2(self):
        input = """Function: foo 
        Parameter: n 
        Body: 
            Var: x[12]={12};
        EndBody."""
        expect = Program([FuncDecl(Id("foo"),[VarDecl(Id("n"),[],None)],([VarDecl(Id("x"),[12],ArrayLiteral([IntLiteral(12)]))],[]))])
        self.assertTrue(TestAST.checkASTGen(input,expect,308))

    def test_assign_statement1(self):
        input = """Function: foo 
        Parameter: n 
        Body: 
            n = (9 + 2\\2);
        EndBody."""
        expect = Program([FuncDecl(Id("foo"),[VarDecl(Id("n"),[],None)],([],[Assign(Id("n"),BinaryOp("+",IntLiteral(9),BinaryOp("\\",IntLiteral(2),IntLiteral(2))))]))])
        self.assertTrue(TestAST.checkASTGen(input,expect,309))

    def test_assign_statement2(self):
        input = """Function: foo 
        Parameter: n 
        Body: 
            n[3][4] = {1,2,{3,4,5}};
        EndBody."""
        expect = Program([FuncDecl(Id("foo"),[VarDecl(Id("n"),[],None)],([],[Assign(ArrayCell(Id("n"),[IntLiteral(3),IntLiteral(4)]),ArrayLiteral([IntLiteral(1),IntLiteral(2),ArrayLiteral([IntLiteral(3),IntLiteral(4),IntLiteral(5)])]))]))])
        self.assertTrue(TestAST.checkASTGen(input,expect,310))

    def test_assign_statement3(self):
        input = """Function: foo 
        Body:
            Var: a;
            a = foo(2, 2*3);
        EndBody."""
        expect = Program([FuncDecl(Id("foo"),[],([VarDecl(Id("a"),[],None)],[Assign(Id("a"),CallExpr(Id("foo"),[IntLiteral(2),BinaryOp("*",IntLiteral(2),IntLiteral(3))]))]))])
        self.assertTrue(TestAST.checkASTGen(input,expect,311))

    def test_assign_statement3(self):
        input = """Function: foo 
        Body:
            x = y[3];
        EndBody."""
        expect = Program([FuncDecl(Id("foo"),[],([VarDecl(Id("a"),[],None)],[Assign(Id("a"),CallExpr(Id("foo"),[IntLiteral(2),BinaryOp("*",IntLiteral(2),IntLiteral(3))]))]))])
        self.assertTrue(TestAST.checkASTGen(input,expect,311))

    def test_if_statement1(self):
        input = """Function: foo 
        Body:
            If True Then
                Var: a;
                Var: x;
                Var: y;
                x = 1;
                y = 2;
                z = 3;
            EndIf.
        EndBody."""
        expect = Program([FuncDecl(Id("foo"),[],([],[If([(BooleanLiteral(True),[VarDecl(Id("a"),[],None),VarDecl(Id("x"),[],None),VarDecl(Id("y"),[],None)],[Assign(Id("x"),IntLiteral(1)),Assign(Id("y"),IntLiteral(2)),Assign(Id("z"),IntLiteral(3))])],())]))])
        self.assertTrue(TestAST.checkASTGen(input,expect,312))

    def test_if_statement2(self):
        input = """Function: foo 
        Body:
            If True Then
                x = 3;
            Else 
                x = 2;
            EndIf.
        EndBody."""
        expect = Program([FuncDecl(Id("foo"),[],([],[If([(BooleanLiteral(True),[],[Assign(Id("x"),IntLiteral(3))])],([],[Assign(Id("x"),IntLiteral(2))]))]))])
        self.assertTrue(TestAST.checkASTGen(input,expect,313))

    def test_for_statement(self):
        input = """Function: foo 
        Parameter: n
        Body: 
        For (i = 0, i < 10, 2) Do
            writeln(i,1);
        EndFor.
        EndBody."""
        expect = Program([FuncDecl(Id("foo"),[VarDecl(Id("n"),[],None)],([],[For(Id("i"),IntLiteral(0),BinaryOp("<",Id("i"),IntLiteral(10)),IntLiteral(2),([],[CallStmt(Id("writeln"),[Id("i"),IntLiteral(1)])]))]))])
        self.assertTrue(TestAST.checkASTGen(input,expect,323))
    
    def test_for_statement1(self):
        input = """Function: foo 
        Parameter: n
        Body: 
        For (i = 6*9,True, i-1) Do
            Var:x=5;
            a=3;
        EndFor.
        EndBody."""

        expect = Program([FuncDecl(Id("foo"),[VarDecl(Id("n"),[],None)],([],[For(Id("i"),BinaryOp("*",IntLiteral(6),IntLiteral(9)),BooleanLiteral(True),BinaryOp("-",Id("i"),IntLiteral(1)),([VarDecl(Id("x"),[],IntLiteral(5))],[Assign(Id("a"),IntLiteral(3))]))]))])
        self.assertTrue(TestAST.checkASTGen(input,expect,324))
    
    def test_while_statement(self):
        input = """Function: foo 
        Parameter: n
        Body: 
            While i < 5 Do
                a = b +. 1.0;
            EndWhile.
        EndBody."""
        expect = Program([FuncDecl(Id("foo"),[VarDecl(Id("n"),[],None)],([],[While(BinaryOp("<",Id("i"),IntLiteral(5)),([],[Assign(Id("a"),BinaryOp("+.",Id("b"),FloatLiteral(1.0)))]))]))])
        self.assertTrue(TestAST.checkASTGen(input,expect,324))

    def test_break_statement(self):
        input = """Function: foo 
        Body: 
            Break;
        EndBody."""
        expect = Program([FuncDecl(Id("foo"),[],([],[Break()]))])
        self.assertTrue(TestAST.checkASTGen(input,expect,325))

    def test_continue_statement(self):
        input = """Function: foo 
        Body: 
            Continue;
        EndBody."""

        expect = Program([FuncDecl(Id("foo"),[],([],[Continue()]))])
        self.assertTrue(TestAST.checkASTGen(input,expect,326))

    def test_return_statement1(self):
        input = """Function: foo 
        Body: 
            Return;
        EndBody."""

        expect = Program([FuncDecl(Id("foo"),[],([],[Return(None)]))])
        self.assertTrue(TestAST.checkASTGen(input,expect,327))

    def test_return_statement2(self):
        input = """Function: foo 
        Body: 
            Return x + 2;
        EndBody."""
        expect = Program([FuncDecl(Id("foo"),[],([],[Return(BinaryOp("+",Id("x"),IntLiteral(2)))]))])
        self.assertTrue(TestAST.checkASTGen(input,expect,328))