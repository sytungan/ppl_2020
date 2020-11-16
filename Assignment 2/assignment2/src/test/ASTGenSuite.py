import unittest
from TestUtils import TestAST
from AST import *
# from test2string.Test2String import TestAST
#from test2string.ASTString import *

class ASTGenSuite(unittest.TestCase):
    def test_assignment_statement_1(self):
        input = """Function: foo 
        Parameter: n 
        Body: 
            n = (9 + 2\\2);
        EndBody.""" 
        expect = Program([FuncDecl(Id("foo"),[VarDecl(Id("n"),[],None)],([],[Assign(Id("n"),BinaryOp("+",IntLiteral(9),BinaryOp("\\",IntLiteral(2),IntLiteral(2))))]))])
        self.assertTrue(TestAST.checkASTGen(input,expect,301))

    def test_assignment_statement_2(self):
        input = """Function: foo 
        Parameter: n 
        Body: 
            n[3][4] = {1,2,{3,4,5}};
        EndBody.""" 
        expect = Program([FuncDecl(Id("foo"),[VarDecl(Id("n"),[],None)],([],[Assign(ArrayCell(Id("n"),[IntLiteral(3),IntLiteral(4)]),ArrayLiteral([IntLiteral(1),IntLiteral(2),ArrayLiteral([IntLiteral(3),IntLiteral(4),IntLiteral(5)])]))]))])
        self.assertTrue(TestAST.checkASTGen(input,expect,302))

    def test_assignment_statement_3(self):
        input = """Function: foo 
        Body:
            Var: a;
            a = foo(2, 2*3);
        EndBody.""" 
        expect = Program([FuncDecl(Id("foo"),[],([VarDecl(Id("a"),[],None)],[Assign(Id("a"),CallExpr(Id("foo"),[IntLiteral(2),BinaryOp("*",IntLiteral(2),IntLiteral(3))]))]))])
        self.assertTrue(TestAST.checkASTGen(input,expect,303))

    def test_assignment_statement_4(self):
        input = """
        Var: a;
        Function: test
        Body:
            Var: r = 10., v;
            v = (4. \. 3.) *. 3.14 *. r *. r *. r;
        EndBody.
        """ 
        expect = Program([VarDecl(Id("a"),[],None),FuncDecl(Id("test"),[],([VarDecl(Id("r"),[],FloatLiteral(10.0)),VarDecl(Id("v"),[],None)],[Assign(Id("v"),BinaryOp("*.",BinaryOp("*.",BinaryOp("*.",BinaryOp("*.",BinaryOp("\.",FloatLiteral(4.0),FloatLiteral(3.0)),FloatLiteral(3.14)),Id("r")),Id("r")),Id("r")))]))])
        self.assertTrue(TestAST.checkASTGen(input,expect,304))

    def test_assignment_statement_5(self):
        input = """
        Function: test
        Body:
            Var: a, b, t;
            a = "RiaoKL#A8ip28Xqk";
            b = 12e5;
            t = a;
            a = b;
            b = t;
            t = !(a=="RiaoKL#A8ip28Xqk") && (b == 12e5);
        EndBody.
        """ 
        expect = Program([FuncDecl(Id("test"),[],([VarDecl(Id("a"),[],None),VarDecl(Id("b"),[],None),VarDecl(Id("t"),[],None)],[Assign(Id("a"),StringLiteral("RiaoKL#A8ip28Xqk")),Assign(Id("b"),FloatLiteral(1200000.0)),Assign(Id("t"),Id("a")),Assign(Id("a"),Id("b")),Assign(Id("b"),Id("t")),Assign(Id("t"),BinaryOp("&&",UnaryOp("!",BinaryOp("==",Id("a"),StringLiteral("RiaoKL#A8ip28Xqk"))),BinaryOp("==",Id("b"),FloatLiteral(1200000.0))))]))])
        self.assertTrue(TestAST.checkASTGen(input,expect,305))

    def test_assignment_statement_6(self):
        input = """
        Function: test
        Body:
            Var: a[100], x[3][4];
            x = {{{12,1}, {12., 12e3}},{23}, {13,32}};
        EndBody.
        """ 
        expect = Program([FuncDecl(Id("test"),[],([VarDecl(Id("a"),[100],None),VarDecl(Id("x"),[3,4],None)],[Assign(Id("x"),ArrayLiteral([ArrayLiteral([ArrayLiteral([IntLiteral(12),IntLiteral(1)]),ArrayLiteral([FloatLiteral(12.0),FloatLiteral(12000.0)])]),ArrayLiteral([IntLiteral(23)]),ArrayLiteral([IntLiteral(13),IntLiteral(32)])]))]))])
        self.assertTrue(TestAST.checkASTGen(input,expect,306))

    def test_assignment_statement_7(self):
        input = """
        Function: test
        Body:
            Var: r = 2, c = 9;
            foo(r,c)[1] = r + c;
            r = 9 - r;
            Return True;
        EndBody.
        """ 
        expect = Program([FuncDecl(Id("test"),[],([VarDecl(Id("r"),[],IntLiteral(2)),VarDecl(Id("c"),[],IntLiteral(9))],[Assign(ArrayCell(CallExpr(Id("foo"),[Id("r"),Id("c")]),[IntLiteral(1)]),BinaryOp("+",Id("r"),Id("c"))),Assign(Id("r"),BinaryOp("-",IntLiteral(9),Id("r"))),Return(BooleanLiteral(True))]))])
        self.assertTrue(TestAST.checkASTGen(input,expect,307))

    def test_assignment_statement_8(self):
        input = """
        Function: test
        Body:
            Var: r, d, t;
            r = 3.14;
            s = r*r + 2;
            t = s && !foo(2)[3][1] || r =/= 9. && (2+3)*.5.;
            t = t \. 3.;
            Return True;
        EndBody.
        """ 
        expect = Program([FuncDecl(Id("test"),[],([VarDecl(Id("r"),[],None),VarDecl(Id("d"),[],None),VarDecl(Id("t"),[],None)],[Assign(Id("r"),FloatLiteral(3.14)),Assign(Id("s"),BinaryOp("+",BinaryOp("*",Id("r"),Id("r")),IntLiteral(2))),Assign(Id("t"),BinaryOp("=/=",BinaryOp("||",BinaryOp("&&",Id("s"),UnaryOp("!",ArrayCell(CallExpr(Id("foo"),[IntLiteral(2)]),[IntLiteral(3),IntLiteral(1)]))),Id("r")),BinaryOp("&&",FloatLiteral(9.0),BinaryOp("*.",BinaryOp("+",IntLiteral(2),IntLiteral(3)),FloatLiteral(5.0))))),Assign(Id("t"),BinaryOp("\.",Id("t"),FloatLiteral(3.0))),Return(BooleanLiteral(True))]))])
        self.assertTrue(TestAST.checkASTGen(input,expect,308))

    def test_assignment_statement_9(self):
        input = """
        Var: x, y = 5e3, z;
        Function: test
        Body:
            z = (x*x*x*x*x*x*x)\.(2.*.y -. 2.3e12 + 23	 + 12%2) - test();
            x = x -. 10.;
            If x >=. 1. Then
                Return z;
            EndIf.
        EndBody.
        """ 
        expect = Program([VarDecl(Id("x"),[],None),VarDecl(Id("y"),[],FloatLiteral(5000.0)),VarDecl(Id("z"),[],None),FuncDecl(Id("test"),[],([],[Assign(Id("z"),BinaryOp("-",BinaryOp("\.",BinaryOp("*",BinaryOp("*",BinaryOp("*",BinaryOp("*",BinaryOp("*",BinaryOp("*",Id("x"),Id("x")),Id("x")),Id("x")),Id("x")),Id("x")),Id("x")),BinaryOp("+",BinaryOp("+",BinaryOp("-.",BinaryOp("*.",FloatLiteral(2.0),Id("y")),FloatLiteral(2300000000000.0)),IntLiteral(23)),BinaryOp("%",IntLiteral(12),IntLiteral(2)))),CallExpr(Id("test"),[]))),Assign(Id("x"),BinaryOp("-.",Id("x"),FloatLiteral(10.0))),If([(BinaryOp(">=.",Id("x"),FloatLiteral(1.0)),[],[Return(Id("z"))])],([],[]))]))])
        self.assertTrue(TestAST.checkASTGen(input,expect,309))

    def test_assignment_statement_10(self):
        input = """
        Function: test
        Body:
            Var: r = 3.14, t;
            r = r*r == (2*3);
            t[1] =  True;
            test(t[1],t[0][2])[3][12] = !t == !(r && False || 2-2); 
        EndBody.
        """ 
        expect = Program([FuncDecl(Id("test"),[],([VarDecl(Id("r"),[],FloatLiteral(3.14)),VarDecl(Id("t"),[],None)],[Assign(Id("r"),BinaryOp("==",BinaryOp("*",Id("r"),Id("r")),BinaryOp("*",IntLiteral(2),IntLiteral(3)))),Assign(ArrayCell(Id("t"),[IntLiteral(1)]),BooleanLiteral(True)),Assign(ArrayCell(CallExpr(Id("test"),[ArrayCell(Id("t"),[IntLiteral(1)]),ArrayCell(Id("t"),[IntLiteral(0),IntLiteral(2)])]),[IntLiteral(3),IntLiteral(12)]),BinaryOp("==",UnaryOp("!",Id("t")),UnaryOp("!",BinaryOp("||",BinaryOp("&&",Id("r"),BooleanLiteral(False)),BinaryOp("-",IntLiteral(2),IntLiteral(2))))))]))])
        self.assertTrue(TestAST.checkASTGen(input,expect,310))

    def test_assignment_statement_11(self):
        input = """
        Var: s = 0;
        Function: test
        Parameter: count
        Body:
            s[1][2][4] = foo(s)[test(foo(3,test(1),test(foo()))+0XFF)] + 3 - 15 \.-.2.;
            t = 2.e5 <=. 2.5 || (0xF21 >= 0XFF) && (0o124 < 0O171);
        EndBody.
        """ 
        expect = Program([VarDecl(Id("s"),[],IntLiteral(0)),FuncDecl(Id("test"),[VarDecl(Id("count"),[],None)],([],[Assign(ArrayCell(Id("s"),[IntLiteral(1),IntLiteral(2),IntLiteral(4)]),BinaryOp("-",BinaryOp("+",ArrayCell(CallExpr(Id("foo"),[Id("s")]),[CallExpr(Id("test"),[BinaryOp("+",CallExpr(Id("foo"),[IntLiteral(3),CallExpr(Id("test"),[IntLiteral(1)]),CallExpr(Id("test"),[CallExpr(Id("foo"),[])])]),IntLiteral(255))])]),IntLiteral(3)),BinaryOp("\.",IntLiteral(15),UnaryOp("-.",FloatLiteral(2.0))))),Assign(Id("t"),BinaryOp("<=.",FloatLiteral(200000.0),BinaryOp("&&",BinaryOp("||",FloatLiteral(2.5),BinaryOp(">=",IntLiteral(3873),IntLiteral(255))),BinaryOp("<",IntLiteral(84),IntLiteral(121)))))]))])
        self.assertTrue(TestAST.checkASTGen(input,expect,311))

    def test_assignment_statement_12(self):
        input = """
        Function: test
        Body:
            Var: s1, s2, s3;
            s1 = "Sk%%w7?1kYbOVV2s";
            s2 = "?m4W1##AiNGv&sqg";
            s3 = "oaD0W?@V2WjsFzFU";
            s3 = s1 + s2 - s3*s1;
        EndBody.
        """ 
        expect = Program([FuncDecl(Id("test"),[],([VarDecl(Id("s1"),[],None),VarDecl(Id("s2"),[],None),VarDecl(Id("s3"),[],None)],[Assign(Id("s1"),StringLiteral("Sk%%w7?1kYbOVV2s")),Assign(Id("s2"),StringLiteral("?m4W1##AiNGv&sqg")),Assign(Id("s3"),StringLiteral("oaD0W?@V2WjsFzFU")),Assign(Id("s3"),BinaryOp("-",BinaryOp("+",Id("s1"),Id("s2")),BinaryOp("*",Id("s3"),Id("s1"))))]))])
        self.assertTrue(TestAST.checkASTGen(input,expect,312))

    def test_assignment_statement_13(self):
        input = """
        Function: test
        Body:
            Var: a=1, b=2, c=3, d[2]={2e-1, 9e5}, z;
            b = d - a;
            c = d - c;
            a = b *. c;
            z =  a*a + b*b + c*c - 3*a*b -  4*a\.b - 5*c*c*.c + 1*1*1;
        EndBody.
        """ 
        expect = Program([FuncDecl(Id("test"),[],([VarDecl(Id("a"),[],IntLiteral(1)),VarDecl(Id("b"),[],IntLiteral(2)),VarDecl(Id("c"),[],IntLiteral(3)),VarDecl(Id("d"),[2],ArrayLiteral([FloatLiteral(0.2),FloatLiteral(900000.0)])),VarDecl(Id("z"),[],None)],[Assign(Id("b"),BinaryOp("-",Id("d"),Id("a"))),Assign(Id("c"),BinaryOp("-",Id("d"),Id("c"))),Assign(Id("a"),BinaryOp("*.",Id("b"),Id("c"))),Assign(Id("z"),BinaryOp("+",BinaryOp("-",BinaryOp("-",BinaryOp("-",BinaryOp("+",BinaryOp("+",BinaryOp("*",Id("a"),Id("a")),BinaryOp("*",Id("b"),Id("b"))),BinaryOp("*",Id("c"),Id("c"))),BinaryOp("*",BinaryOp("*",IntLiteral(3),Id("a")),Id("b"))),BinaryOp("\.",BinaryOp("*",IntLiteral(4),Id("a")),Id("b"))),BinaryOp("*.",BinaryOp("*",BinaryOp("*",IntLiteral(5),Id("c")),Id("c")),Id("c"))),BinaryOp("*",BinaryOp("*",IntLiteral(1),IntLiteral(1)),IntLiteral(1))))]))])
        self.assertTrue(TestAST.checkASTGen(input,expect,313))

    def test_break_statement_1(self):
        input = """
        Function: test
        Body:   
            For (i = 0, i < 10, 2) Do
                Break;
            EndFor.
            writeln(i);
        EndBody.
        """ 
        expect = Program([FuncDecl(Id("test"),[],([],[For(Id("i"),IntLiteral(0),BinaryOp("<",Id("i"),IntLiteral(10)),IntLiteral(2),([],[Break()])),CallStmt(Id("writeln"),[Id("i")])]))])
        self.assertTrue(TestAST.checkASTGen(input,expect,314))

    def test_break_statement_2(self):
        input = """
        Function: test
        Parameter: x
        Body:
            Var: x = 0;
            While i < 10 Do
                If i == x Then Break;
                EndIf.
                writeln(i);
                i = i + 1;
            EndWhile.
        EndBody.
        """ 
        expect = Program([FuncDecl(Id("test"),[VarDecl(Id("x"),[],None)],([VarDecl(Id("x"),[],IntLiteral(0))],[While(BinaryOp("<",Id("i"),IntLiteral(10)),([],[If([(BinaryOp("==",Id("i"),Id("x")),[],[Break()])],([],[])),CallStmt(Id("writeln"),[Id("i")]),Assign(Id("i"),BinaryOp("+",Id("i"),IntLiteral(1)))]))]))])
        self.assertTrue(TestAST.checkASTGen(input,expect,315))

    def test_break_statement_3(self):
        input = """
        Function: test
        Body:
            Var: a[2][3][4][5];
            Do 
                a = 2.e59;
                e = 0.e69;
                Break;
            While True EndDo.
            writeln(a -. e);
        EndBody.
        """ 
        expect = Program([FuncDecl(Id("test"),[],([VarDecl(Id("a"),[2,3,4,5],None)],[Dowhile(([],[Assign(Id("a"),FloatLiteral(2e+59)),Assign(Id("e"),FloatLiteral(0.0)),Break()]),BooleanLiteral(True)),CallStmt(Id("writeln"),[BinaryOp("-.",Id("a"),Id("e"))])]))])
        self.assertTrue(TestAST.checkASTGen(input,expect,316))

    def test_call_statement_1(self):
        input = """
        Function: test
        Body:
            foo (2 + x, 4. \. y);
        EndBody.
        Function: foo
        Parameter: a, b
        Body:
            writeln(a+.b);
        EndBody.
        """ 
        expect = Program([FuncDecl(Id("test"),[],([],[CallStmt(Id("foo"),[BinaryOp("+",IntLiteral(2),Id("x")),BinaryOp("\.",FloatLiteral(4.0),Id("y"))])])),FuncDecl(Id("foo"),[VarDecl(Id("a"),[],None),VarDecl(Id("b"),[],None)],([],[CallStmt(Id("writeln"),[BinaryOp("+.",Id("a"),Id("b"))])]))])
        self.assertTrue(TestAST.checkASTGen(input,expect,317))

    def test_call_statement_2(self):
        input = """
        Function: test
        Body:
            foo();
        EndBody.
        Function: foo
        Body:
        EndBody.
        """ 
        expect = Program([FuncDecl(Id("test"),[],([],[CallStmt(Id("foo"),[])])),FuncDecl(Id("foo"),[],([],[]))])
        self.assertTrue(TestAST.checkASTGen(input,expect,318))

    def test_call_statement_3(self):
        input = """
        Function: test
        Body:
            x = foo(2) - 2 \ 3 + 4;
            test();
        EndBody.
        Function: foo
        Parameter: n
        Body:
        EndBody.
        """ 
        expect = Program([FuncDecl(Id("test"),[],([],[Assign(Id("x"),BinaryOp("+",BinaryOp("-",CallExpr(Id("foo"),[IntLiteral(2)]),BinaryOp("\\",IntLiteral(2),IntLiteral(3))),IntLiteral(4))),CallStmt(Id("test"),[])])),FuncDecl(Id("foo"),[VarDecl(Id("n"),[],None)],([],[]))])
        self.assertTrue(TestAST.checkASTGen(input,expect,319))

    def test_call_statement_4(self):
        input = """
        Function: test
        Body:
            foo(True, "!@$C#hc%", 12. \. 921.9e5 * 32e1);
            foo(3,2,1);
            foo(foo(2021,foo(foo(),foo(),foo()),2020), "BKit", 2020e125);
        EndBody.
        Function: foo
        Parameter: n, c, t
        Body:
        EndBody.
        """ 
        expect = Program([FuncDecl(Id("test"),[],([],[CallStmt(Id("foo"),[BooleanLiteral(True),StringLiteral("!@$C#hc%"),BinaryOp("*",BinaryOp("\.",FloatLiteral(12.0),FloatLiteral(92190000.0)),FloatLiteral(320.0))]),CallStmt(Id("foo"),[IntLiteral(3),IntLiteral(2),IntLiteral(1)]),CallStmt(Id("foo"),[CallExpr(Id("foo"),[IntLiteral(2021),CallExpr(Id("foo"),[CallExpr(Id("foo"),[]),CallExpr(Id("foo"),[]),CallExpr(Id("foo"),[])]),IntLiteral(2020)]),StringLiteral("BKit"),FloatLiteral(2.02e+128)])])),FuncDecl(Id("foo"),[VarDecl(Id("n"),[],None),VarDecl(Id("c"),[],None),VarDecl(Id("t"),[],None)],([],[]))])
        self.assertTrue(TestAST.checkASTGen(input,expect,320))

    def test_continue_statement_1(self):
        input = """
        Function: test
        Body:
            Var: x = 1;
            Do 
                Continue;
            While !x EndDo.
        EndBody.
        """ 
        expect = Program([FuncDecl(Id("test"),[],([VarDecl(Id("x"),[],IntLiteral(1))],[Dowhile(([],[Continue()]),UnaryOp("!",Id("x")))]))])
        self.assertTrue(TestAST.checkASTGen(input,expect,321))

    def test_continue_statement_2(self):
        input = """
        Function: test
        Body:
            Var: x = 1;
            While !x Do
                Continue;
                x = True || False;
            EndWhile.
        EndBody.
        """ 
        expect = Program([FuncDecl(Id("test"),[],([VarDecl(Id("x"),[],IntLiteral(1))],[While(UnaryOp("!",Id("x")),([],[Continue(),Assign(Id("x"),BinaryOp("||",BooleanLiteral(True),BooleanLiteral(False)))]))]))])
        self.assertTrue(TestAST.checkASTGen(input,expect,322))

    def test_continue_statement_3(self):
        input = """
        Function: test
        Body:
            For (i = 1, i < 100, 1) Do
                If (i%2 !=0) Then Continue;
                EndIf.
                writeln(i);
            EndFor.
        EndBody.
        """ 
        expect = Program([FuncDecl(Id("test"),[],([],[For(Id("i"),IntLiteral(1),BinaryOp("<",Id("i"),IntLiteral(100)),IntLiteral(1),([],[If([(BinaryOp("!=",BinaryOp("%",Id("i"),IntLiteral(2)),IntLiteral(0)),[],[Continue()])],([],[])),CallStmt(Id("writeln"),[Id("i")])]))]))])
        self.assertTrue(TestAST.checkASTGen(input,expect,323))

    def test_do_while_statement_1(self):
        input = """
        Function: test
        Body:
            Var: i = 0;
            Do 
                writeln(i);
                i = i + 1;
            While (i < 10) EndDo.
        EndBody.
        """ 
        expect = Program([FuncDecl(Id("test"),[],([VarDecl(Id("i"),[],IntLiteral(0))],[Dowhile(([],[CallStmt(Id("writeln"),[Id("i")]),Assign(Id("i"),BinaryOp("+",Id("i"),IntLiteral(1)))]),BinaryOp("<",Id("i"),IntLiteral(10)))]))])
        self.assertTrue(TestAST.checkASTGen(input,expect,324))

    def test_do_while_statement_2(self):
        input = """
        Function: test **1 + 2 + ... n < max**
        Parameter: max
        Body:
            Var: n = 0, s = 0;
            Do 
                n = n + 1;
                s = s + n;
            While s + n + 1 < max EndDo.
            writeln(n);
        EndBody.
        """ 
        expect = Program([FuncDecl(Id("test"),[VarDecl(Id("max"),[],None)],([VarDecl(Id("n"),[],IntLiteral(0)),VarDecl(Id("s"),[],IntLiteral(0))],[Dowhile(([],[Assign(Id("n"),BinaryOp("+",Id("n"),IntLiteral(1))),Assign(Id("s"),BinaryOp("+",Id("s"),Id("n")))]),BinaryOp("<",BinaryOp("+",BinaryOp("+",Id("s"),Id("n")),IntLiteral(1)),Id("max"))),CallStmt(Id("writeln"),[Id("n")])]))])
        self.assertTrue(TestAST.checkASTGen(input,expect,325))

    def test_do_while_statement_3(self):
        input = """
        Function: test
        Body:
            Var: n = 0, s = 0;
            Do 
                n = n + 1;
                Do 
                    If n%2 == 0 Then s = s + 1;
                    EndIf.
                While (s < 1000) EndDo.
                s = s + n;
            While (s + n + 1 < max) EndDo.
            writeln(n);
        EndBody.
        """ 
        expect = Program([FuncDecl(Id("test"),[],([VarDecl(Id("n"),[],IntLiteral(0)),VarDecl(Id("s"),[],IntLiteral(0))],[Dowhile(([],[Assign(Id("n"),BinaryOp("+",Id("n"),IntLiteral(1))),Dowhile(([],[If([(BinaryOp("==",BinaryOp("%",Id("n"),IntLiteral(2)),IntLiteral(0)),[],[Assign(Id("s"),BinaryOp("+",Id("s"),IntLiteral(1)))])],([],[]))]),BinaryOp("<",Id("s"),IntLiteral(1000))),Assign(Id("s"),BinaryOp("+",Id("s"),Id("n")))]),BinaryOp("<",BinaryOp("+",BinaryOp("+",Id("s"),Id("n")),IntLiteral(1)),Id("max"))),CallStmt(Id("writeln"),[Id("n")])]))])
        self.assertTrue(TestAST.checkASTGen(input,expect,326))

    def test_do_while_statement_4(self):
        input = """
        Function: test
        Body:
            Var: i, j, k, l;
            Do 
                i = i + 1;
                While (j < 100) Do
                    Do
                        k = k + 1;
                        While (l < 100) Do
                            l = l + 2;
                        EndWhile.
                    While (k < 100) EndDo.
                    j = j + 3;
                EndWhile.
            While (i + j + k + l < foo(2)) EndDo.
            writeln(n);
        EndBody.
        """ 
        expect = Program([FuncDecl(Id("test"),[],([VarDecl(Id("i"),[],None),VarDecl(Id("j"),[],None),VarDecl(Id("k"),[],None),VarDecl(Id("l"),[],None)],[Dowhile(([],[Assign(Id("i"),BinaryOp("+",Id("i"),IntLiteral(1))),While(BinaryOp("<",Id("j"),IntLiteral(100)),([],[Dowhile(([],[Assign(Id("k"),BinaryOp("+",Id("k"),IntLiteral(1))),While(BinaryOp("<",Id("l"),IntLiteral(100)),([],[Assign(Id("l"),BinaryOp("+",Id("l"),IntLiteral(2)))]))]),BinaryOp("<",Id("k"),IntLiteral(100))),Assign(Id("j"),BinaryOp("+",Id("j"),IntLiteral(3)))]))]),BinaryOp("<",BinaryOp("+",BinaryOp("+",BinaryOp("+",Id("i"),Id("j")),Id("k")),Id("l")),CallExpr(Id("foo"),[IntLiteral(2)]))),CallStmt(Id("writeln"),[Id("n")])]))])
        self.assertTrue(TestAST.checkASTGen(input,expect,327))

    def test_do_while_statement_5(self):
        input = """
        Function: test
        Parameter: n
        Body:
            Var: flag = 0;
            Do
                If (n!=2) && (n%i==0) Then
                    flag=1;
                EndIf.
                i = i + 1;
            While i<=sqrt(n) EndDo.
            print(i);
        EndBody.
        """ 
        expect = Program([FuncDecl(Id("test"),[VarDecl(Id("n"),[],None)],([VarDecl(Id("flag"),[],IntLiteral(0))],[Dowhile(([],[If([(BinaryOp("&&",BinaryOp("!=",Id("n"),IntLiteral(2)),BinaryOp("==",BinaryOp("%",Id("n"),Id("i")),IntLiteral(0))),[],[Assign(Id("flag"),IntLiteral(1))])],([],[])),Assign(Id("i"),BinaryOp("+",Id("i"),IntLiteral(1)))]),BinaryOp("<=",Id("i"),CallExpr(Id("sqrt"),[Id("n")]))),CallStmt(Id("print"),[Id("i")])]))])
        self.assertTrue(TestAST.checkASTGen(input,expect,328))

    def test_do_while_statement_6(self):
        input = """
        Function: test
        Body:
            Var: flag = 0;
            Do
                While !flag Do
                EndWhile.
            While flag EndDo.
        EndBody.
        """ 
        expect = Program([FuncDecl(Id("test"),[],([VarDecl(Id("flag"),[],IntLiteral(0))],[Dowhile(([],[While(UnaryOp("!",Id("flag")),([],[]))]),Id("flag"))]))])
        self.assertTrue(TestAST.checkASTGen(input,expect,329))

    def test_do_while_statement_7(self):
        input = """
        Function: test
        Body:
            Do
                Do
                    Do
                    While (True) EndDo.
                        Do
                        While (True) EndDo.
                        Do
                            Do
                                Do
                                    Do
                                    While (True) EndDo.
                                While (True) EndDo.
                            While (True) EndDo.
                        While (True) EndDo.
                    Do
                        Do
                        While (True) EndDo.
                    While (True) EndDo.
                    Do
                    While (True) EndDo.
                While (True) EndDo.
            While (True) EndDo.
        EndBody.
        """ 
        expect = Program([FuncDecl(Id("test"),[],([],[Dowhile(([],[Dowhile(([],[Dowhile(([],[]),BooleanLiteral(True)),Dowhile(([],[]),BooleanLiteral(True)),Dowhile(([],[Dowhile(([],[Dowhile(([],[Dowhile(([],[]),BooleanLiteral(True))]),BooleanLiteral(True))]),BooleanLiteral(True))]),BooleanLiteral(True)),Dowhile(([],[Dowhile(([],[]),BooleanLiteral(True))]),BooleanLiteral(True)),Dowhile(([],[]),BooleanLiteral(True))]),BooleanLiteral(True))]),BooleanLiteral(True))]))])
        self.assertTrue(TestAST.checkASTGen(input,expect,330))

    def test_for_statement_1(self):
        input = """
        Function: test
        Body:   
            For (i = 0, i < 10, 2) Do
                writeln(i);
            EndFor.
        EndBody.
        """ 
        expect = Program([FuncDecl(Id("test"),[],([],[For(Id("i"),IntLiteral(0),BinaryOp("<",Id("i"),IntLiteral(10)),IntLiteral(2),([],[CallStmt(Id("writeln"),[Id("i")])]))]))])
        self.assertTrue(TestAST.checkASTGen(input,expect,331))

    def test_for_statement_2(self):
        input = """Function: foo 
        Parameter: n
        Body: 
        For (i = 0, i < 10, 2) Do
            writeln(i,1);
        EndFor.
        EndBody.""" 
        expect = Program([FuncDecl(Id("foo"),[VarDecl(Id("n"),[],None)],([],[For(Id("i"),IntLiteral(0),BinaryOp("<",Id("i"),IntLiteral(10)),IntLiteral(2),([],[CallStmt(Id("writeln"),[Id("i"),IntLiteral(1)])]))]))])
        self.assertTrue(TestAST.checkASTGen(input,expect,332))

    def test_for_statement_3(self):
        input = """Function: foo 
        Parameter: n
        Body: 
        For (i = 6*9,True, i-1) Do
            Var:x=5;
            a=3;
        EndFor.
        EndBody.""" 
        expect = Program([FuncDecl(Id("foo"),[VarDecl(Id("n"),[],None)],([],[For(Id("i"),BinaryOp("*",IntLiteral(6),IntLiteral(9)),BooleanLiteral(True),BinaryOp("-",Id("i"),IntLiteral(1)),([VarDecl(Id("x"),[],IntLiteral(5))],[Assign(Id("a"),IntLiteral(3))]))]))])
        self.assertTrue(TestAST.checkASTGen(input,expect,333))

    def test_for_statement_4(self):
        input = """
        Function: test
        Parameter: n
        Body:
            Var: x;   
            For (i = 0, i < sqrt(n)*2, 1) Do
                x = i + n;
                writeln(x);
            EndFor.
        EndBody.
        """ 
        expect = Program([FuncDecl(Id("test"),[VarDecl(Id("n"),[],None)],([VarDecl(Id("x"),[],None)],[For(Id("i"),IntLiteral(0),BinaryOp("<",Id("i"),BinaryOp("*",CallExpr(Id("sqrt"),[Id("n")]),IntLiteral(2))),IntLiteral(1),([],[Assign(Id("x"),BinaryOp("+",Id("i"),Id("n"))),CallStmt(Id("writeln"),[Id("x")])]))]))])
        self.assertTrue(TestAST.checkASTGen(input,expect,334))
        
    def test_for_statement_5(self):
        input = """
        Function: test
        Body:   
            For (i = 0, i <= 1000, 1) Do
                If i%2 == 0 Then writeln(i);
                EndIf.
            EndFor.
        EndBody.
        """ 
        expect = Program([FuncDecl(Id("test"),[],([],[For(Id("i"),IntLiteral(0),BinaryOp("<=",Id("i"),IntLiteral(1000)),IntLiteral(1),([],[If([(BinaryOp("==",BinaryOp("%",Id("i"),IntLiteral(2)),IntLiteral(0)),[],[CallStmt(Id("writeln"),[Id("i")])])],([],[]))]))]))])
        self.assertTrue(TestAST.checkASTGen(input,expect,335))

    def test_for_statement_6(self):
        input = """
        Function: test
        Parameter: n
        Body:
            Var: z = 0;
            For (i = z, i <= n*n - 2*n + 1, 1) Do
                print(i + i + i);
            EndFor.
        EndBody.
        """ 
        expect = Program([FuncDecl(Id("test"),[VarDecl(Id("n"),[],None)],([VarDecl(Id("z"),[],IntLiteral(0))],[For(Id("i"),Id("z"),BinaryOp("<=",Id("i"),BinaryOp("+",BinaryOp("-",BinaryOp("*",Id("n"),Id("n")),BinaryOp("*",IntLiteral(2),Id("n"))),IntLiteral(1))),IntLiteral(1),([],[CallStmt(Id("print"),[BinaryOp("+",BinaryOp("+",Id("i"),Id("i")),Id("i"))])]))]))])
        self.assertTrue(TestAST.checkASTGen(input,expect,336))

    def test_for_statement_7(self):
        input = """
        Function: test
        Body:
            Var: flag = False, c;
            c = !False;
            For (i = 0, flag == c, 1) Do
                flag = True;
            EndFor.
        EndBody.
        """ 
        expect = Program([FuncDecl(Id("test"),[],([VarDecl(Id("flag"),[],BooleanLiteral(False)),VarDecl(Id("c"),[],None)],[Assign(Id("c"),UnaryOp("!",BooleanLiteral(False))),For(Id("i"),IntLiteral(0),BinaryOp("==",Id("flag"),Id("c")),IntLiteral(1),([],[Assign(Id("flag"),BooleanLiteral(True))]))]))])
        self.assertTrue(TestAST.checkASTGen(input,expect,337))

    def test_for_statement_9(self):
        input = """
        Function: test
        Body:
            For (i = 0, True, 1) Do
            EndFor.
        EndBody.
        """ 
        expect = Program([FuncDecl(Id("test"),[],([],[For(Id("i"),IntLiteral(0),BooleanLiteral(True),IntLiteral(1),([],[]))]))])
        self.assertTrue(TestAST.checkASTGen(input,expect,338))

    def test_for_statement_10(self):
        input = """
        Function: test
        Body:
            Var: a = 2;
            For (i = 10 - a*a[1], a < 100, a > a + 1) Do
                writeln(a*a - i*i);
                i = i + 1;
            EndFor.
        EndBody.
        """ 
        expect = Program([FuncDecl(Id("test"),[],([VarDecl(Id("a"),[],IntLiteral(2))],[For(Id("i"),BinaryOp("-",IntLiteral(10),BinaryOp("*",Id("a"),ArrayCell(Id("a"),[IntLiteral(1)]))),BinaryOp("<",Id("a"),IntLiteral(100)),BinaryOp(">",Id("a"),BinaryOp("+",Id("a"),IntLiteral(1))),([],[CallStmt(Id("writeln"),[BinaryOp("-",BinaryOp("*",Id("a"),Id("a")),BinaryOp("*",Id("i"),Id("i")))]),Assign(Id("i"),BinaryOp("+",Id("i"),IntLiteral(1)))]))]))])
        self.assertTrue(TestAST.checkASTGen(input,expect,339))

    def test_full_program_1(self):
        input = """
        Var: a[100][100] = {{64.09e21,12.,0.9235e1},{"abc",{{0xF21, 0XABC},{212.409, 2.}, 72215},2},{9.,{{3,2},{4.,"cdf"},{0o12,{64,99}}},"hi"}};
        Var: c;
        Function: test
        Parameter: n
        Body:
            Var: t = 5432., s, r, a = 4.2, c=3, p_V[3];
            For (i = 1, i < n, 1) Do
                Do  
                    While !False Do
                        p_V[0] = t*t;
                        p_V[1] = a + c*t -. 9.e5 +. 2. - 2%2 \. 2;
                        p_V[2] = c*c*c - p_V[0]*(2%2) - 19e5 *.2 -. 1. --6 + p_V[1]*99999; 
                        s = False; 
                    EndWhile.
                    s =  !s || !(s ==2) && (t >=. 5432.) && t =/= t*.2;
                    Break;
                While True EndDo.
                If i == n Then Break;
                EndIf.
            EndFor.
            Return test(n%2);
        EndBody.
        Function: main
        Body:
            test(n);
        EndBody.
        """ 
        expect = Program([VarDecl(Id("a"),[100,100],ArrayLiteral([ArrayLiteral([FloatLiteral(6.409e+22),FloatLiteral(12.0),FloatLiteral(9.235)]),ArrayLiteral([StringLiteral("abc"),ArrayLiteral([ArrayLiteral([IntLiteral(3873),IntLiteral(2748)]),ArrayLiteral([FloatLiteral(212.409),FloatLiteral(2.0)]),IntLiteral(72215)]),IntLiteral(2)]),ArrayLiteral([FloatLiteral(9.0),ArrayLiteral([ArrayLiteral([IntLiteral(3),IntLiteral(2)]),ArrayLiteral([FloatLiteral(4.0),StringLiteral("cdf")]),ArrayLiteral([IntLiteral(10),ArrayLiteral([IntLiteral(64),IntLiteral(99)])])]),StringLiteral("hi")])])),VarDecl(Id("c"),[],None),FuncDecl(Id("test"),[VarDecl(Id("n"),[],None)],([VarDecl(Id("t"),[],FloatLiteral(5432.0)),VarDecl(Id("s"),[],None),VarDecl(Id("r"),[],None),VarDecl(Id("a"),[],FloatLiteral(4.2)),VarDecl(Id("c"),[],IntLiteral(3)),VarDecl(Id("p_V"),[3],None)],[For(Id("i"),IntLiteral(1),BinaryOp("<",Id("i"),Id("n")),IntLiteral(1),([],[Dowhile(([],[While(UnaryOp("!",BooleanLiteral(False)),([],[Assign(ArrayCell(Id("p_V"),[IntLiteral(0)]),BinaryOp("*",Id("t"),Id("t"))),Assign(ArrayCell(Id("p_V"),[IntLiteral(1)]),BinaryOp("-",BinaryOp("+.",BinaryOp("-.",BinaryOp("+",Id("a"),BinaryOp("*",Id("c"),Id("t"))),FloatLiteral(900000.0)),FloatLiteral(2.0)),BinaryOp("\.",BinaryOp("%",IntLiteral(2),IntLiteral(2)),IntLiteral(2)))),Assign(ArrayCell(Id("p_V"),[IntLiteral(2)]),BinaryOp("+",BinaryOp("-",BinaryOp("-.",BinaryOp("-",BinaryOp("-",BinaryOp("*",BinaryOp("*",Id("c"),Id("c")),Id("c")),BinaryOp("*",ArrayCell(Id("p_V"),[IntLiteral(0)]),BinaryOp("%",IntLiteral(2),IntLiteral(2)))),BinaryOp("*.",FloatLiteral(1900000.0),IntLiteral(2))),FloatLiteral(1.0)),UnaryOp("-",IntLiteral(6))),BinaryOp("*",ArrayCell(Id("p_V"),[IntLiteral(1)]),IntLiteral(99999)))),Assign(Id("s"),BooleanLiteral(False))])),Assign(Id("s"),BinaryOp("=/=",BinaryOp("&&",BinaryOp("&&",BinaryOp("||",UnaryOp("!",Id("s")),UnaryOp("!",BinaryOp("==",Id("s"),IntLiteral(2)))),BinaryOp(">=.",Id("t"),FloatLiteral(5432.0))),Id("t")),BinaryOp("*.",Id("t"),IntLiteral(2)))),Break()]),BooleanLiteral(True)),If([(BinaryOp("==",Id("i"),Id("n")),[],[Break()])],([],[]))])),Return(CallExpr(Id("test"),[BinaryOp("%",Id("n"),IntLiteral(2))]))])),FuncDecl(Id("main"),[],([],[CallStmt(Id("test"),[Id("n")])]))])
        self.assertTrue(TestAST.checkASTGen(input,expect,340))

    def test_full_program_2(self):
        input = """
        Var: s = 0, arr[2] = {1,2};
        Function: combat
        Parameter: hp1, hp2, d
        **// TODO: You have to complete this function followed by requirements**
        Body:
            Var: p1, p2;
            Var: h1;
            Var: none = False;
            Var: pR;
            p1 = hp1 * (1000 - d) \. int_of_float(1000);
            p2 = (hp2 * d) \. int_of_float(1000);
            h1 = (hp1 + hp2) % 100;
            h2 = (h1*hp2) % 100;
             
            If (hp2 == 888) Then none = True;
            EndIf.
            If hp1 == 777 && ((p1 < p2) || (h1 < h2)) && (none == False) Then
                Var: e = 1;
                d = e;
                p1 = hp1 *. (1000 - d) \. float(1000);
                p2 = (hp2 *. d) \. float(1000);
            EndIf.
            pR = (h1*p1 - h2 * p2) \. (h1*p1 + h2 * p2);
            print(pR);
        EndBody.
        Function: main
        Body:
            combat(544,290,600);
        EndBody.
        """ 
        expect = Program([VarDecl(Id("s"),[],IntLiteral(0)),VarDecl(Id("arr"),[2],ArrayLiteral([IntLiteral(1),IntLiteral(2)])),FuncDecl(Id("combat"),[VarDecl(Id("hp1"),[],None),VarDecl(Id("hp2"),[],None),VarDecl(Id("d"),[],None)],([VarDecl(Id("p1"),[],None),VarDecl(Id("p2"),[],None),VarDecl(Id("h1"),[],None),VarDecl(Id("none"),[],BooleanLiteral(False)),VarDecl(Id("pR"),[],None)],[Assign(Id("p1"),BinaryOp("\.",BinaryOp("*",Id("hp1"),BinaryOp("-",IntLiteral(1000),Id("d"))),CallExpr(Id("int_of_float"),[IntLiteral(1000)]))),Assign(Id("p2"),BinaryOp("\.",BinaryOp("*",Id("hp2"),Id("d")),CallExpr(Id("int_of_float"),[IntLiteral(1000)]))),Assign(Id("h1"),BinaryOp("%",BinaryOp("+",Id("hp1"),Id("hp2")),IntLiteral(100))),Assign(Id("h2"),BinaryOp("%",BinaryOp("*",Id("h1"),Id("hp2")),IntLiteral(100))),If([(BinaryOp("==",Id("hp2"),IntLiteral(888)),[],[Assign(Id("none"),BooleanLiteral(True))])],([],[])),If([(BinaryOp("==",Id("hp1"),BinaryOp("&&",BinaryOp("&&",IntLiteral(777),BinaryOp("||",BinaryOp("<",Id("p1"),Id("p2")),BinaryOp("<",Id("h1"),Id("h2")))),BinaryOp("==",Id("none"),BooleanLiteral(False)))),[VarDecl(Id("e"),[],IntLiteral(1))],[Assign(Id("d"),Id("e")),Assign(Id("p1"),BinaryOp("\.",BinaryOp("*.",Id("hp1"),BinaryOp("-",IntLiteral(1000),Id("d"))),CallExpr(Id("float"),[IntLiteral(1000)]))),Assign(Id("p2"),BinaryOp("\.",BinaryOp("*.",Id("hp2"),Id("d")),CallExpr(Id("float"),[IntLiteral(1000)])))])],([],[])),Assign(Id("pR"),BinaryOp("\.",BinaryOp("-",BinaryOp("*",Id("h1"),Id("p1")),BinaryOp("*",Id("h2"),Id("p2"))),BinaryOp("+",BinaryOp("*",Id("h1"),Id("p1")),BinaryOp("*",Id("h2"),Id("p2"))))),CallStmt(Id("print"),[Id("pR")])])),FuncDecl(Id("main"),[],([],[CallStmt(Id("combat"),[IntLiteral(544),IntLiteral(290),IntLiteral(600)])]))])
        self.assertTrue(TestAST.checkASTGen(input,expect,341))

    def test_function_decl_1(self):
        input = """Function: foo 
        Parameter: n 
        Body: 
            Var: x[12]={12};
        EndBody.""" 
        expect = Program([FuncDecl(Id("foo"),[VarDecl(Id("n"),[],None)],([VarDecl(Id("x"),[12],ArrayLiteral([IntLiteral(12)]))],[]))])
        self.assertTrue(TestAST.checkASTGen(input,expect,342))

    def test_function_decl_2(self):
        input = """
        Function: test
        Parameter: n
        Body: 
            n = n+1;
        EndBody.
        """ 
        expect = Program([FuncDecl(Id("test"),[VarDecl(Id("n"),[],None)],([],[Assign(Id("n"),BinaryOp("+",Id("n"),IntLiteral(1)))]))])
        self.assertTrue(TestAST.checkASTGen(input,expect,343))

    def test_function_decl_3(self):
        input = """
        Function: foo
        Body:
        EndBody.
        """ 
        expect = Program([FuncDecl(Id("foo"),[],([],[]))])
        self.assertTrue(TestAST.checkASTGen(input,expect,344))

    def test_function_decl_4(self):
        input = """
        Function: test___
        Parameter: x[10], a[2][3][2][9]
        Body:
            Return test___(12.,{2,{{2.e5},"hi"},4.});
        EndBody.
        """ 
        expect = Program([FuncDecl(Id("test___"),[VarDecl(Id("x"),[10],None),VarDecl(Id("a"),[2,3,2,9],None)],([],[Return(CallExpr(Id("test___"),[FloatLiteral(12.0),ArrayLiteral([IntLiteral(2),ArrayLiteral([ArrayLiteral([FloatLiteral(200000.0)]),StringLiteral("hi")]),FloatLiteral(4.0)])]))]))])
        self.assertTrue(TestAST.checkASTGen(input,expect,345))

    def test_function_decl_5(self):
        input = """
        Function: test 
        Body:
            Var: arr[2][3] = {"Hi",{"it-desert-theme='"false'""},{"it-player-ads","OK","404"}}; 
            e =  10e2;
        EndBody.
        """ 
        expect = Program([FuncDecl(Id("test"),[],([VarDecl(Id("arr"),[2,3],ArrayLiteral([StringLiteral("Hi"),ArrayLiteral([StringLiteral("it-desert-theme='\"false'\"")]),ArrayLiteral([StringLiteral("it-player-ads"),StringLiteral("OK"),StringLiteral("404")])]))],[Assign(Id("e"),FloatLiteral(1000.0))]))])
        self.assertTrue(TestAST.checkASTGen(input,expect,346))

    def test_if_statement_1(self):
        input = """
        Function: test
        Body:
            Var: x;
            If 2<=3 Then x = 3;
            EndIf.
        EndBody.
        """ 
        expect = Program([FuncDecl(Id("test"),[],([VarDecl(Id("x"),[],None)],[If([(BinaryOp("<=",IntLiteral(2),IntLiteral(3)),[],[Assign(Id("x"),IntLiteral(3))])],([],[]))]))])
        self.assertTrue(TestAST.checkASTGen(input,expect,347))

    def test_if_statement_2(self):
        input = """
        Function: test
        Body:
            Var: i = 21;
            If i == 10 Then 
            ElseIf i == 15 Then
            ElseIf i == 20 Then
            Else
            EndIf.
        EndBody.
        """ 
        expect = Program([FuncDecl(Id("test"),[],([VarDecl(Id("i"),[],IntLiteral(21))],[If([(BinaryOp("==",Id("i"),IntLiteral(10)),[],[]),(BinaryOp("==",Id("i"),IntLiteral(15)),[],[]),(BinaryOp("==",Id("i"),IntLiteral(20)),[],[])],([],[]))]))])
        self.assertTrue(TestAST.checkASTGen(input,expect,348))

    def test_if_statement_3(self):
        input = """Function: foo 
        Parameter: n
        Body: 
            If n == 0 Then
                If n!=0 Then
                    If n!=0 Then
                        a=5;
                    EndIf.
                EndIf.
            EndIf.
        EndBody.""" 
        expect = Program([FuncDecl(Id("foo"),[VarDecl(Id("n"),[],None)],([],[If([(BinaryOp("==",Id("n"),IntLiteral(0)),[],[If([(BinaryOp("!=",Id("n"),IntLiteral(0)),[],[If([(BinaryOp("!=",Id("n"),IntLiteral(0)),[],[Assign(Id("a"),IntLiteral(5))])],([],[]))])],([],[]))])],([],[]))]))])
        self.assertTrue(TestAST.checkASTGen(input,expect,349))

    def test_if_statement_4(self):
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
        expect = Program([FuncDecl(Id("foo"),[],([],[If([(BooleanLiteral(True),[VarDecl(Id("a"),[],None),VarDecl(Id("x"),[],None),VarDecl(Id("y"),[],None)],[Assign(Id("x"),IntLiteral(1)),Assign(Id("y"),IntLiteral(2)),Assign(Id("z"),IntLiteral(3))])],([],[]))]))])
        self.assertTrue(TestAST.checkASTGen(input,expect,350))

    def test_if_statement_5(self):
        input = """Function: foo 
        Body:
            If True Then
                x = 3;
            Else 
                x = 2;
            EndIf.
        EndBody.""" 
        expect = Program([FuncDecl(Id("foo"),[],([],[If([(BooleanLiteral(True),[],[Assign(Id("x"),IntLiteral(3))])],([],[Assign(Id("x"),IntLiteral(2))]))]))])
        self.assertTrue(TestAST.checkASTGen(input,expect,351))

    def test_if_statement_6(self):
        input = """Function: foo 
        Body:
            If True Then
            ElseIf True Then
                x = 2;
            EndIf.
        EndBody.""" 
        expect = Program([FuncDecl(Id("foo"),[],([],[If([(BooleanLiteral(True),[],[]),(BooleanLiteral(True),[],[Assign(Id("x"),IntLiteral(2))])],([],[]))]))])
        self.assertTrue(TestAST.checkASTGen(input,expect,352))

    def test_if_statement_7(self):
        input = """
        Function: test
        Body:
            Var: athos = 500, pothos = 900, jerry, tom = 200;
            If (pothos - athos) < 400 Then jerry = pothos - tom;
            Else jerry = athos - tom;
            EndIf.
        EndBody.
        """ 
        expect = Program([FuncDecl(Id("test"),[],([VarDecl(Id("athos"),[],IntLiteral(500)),VarDecl(Id("pothos"),[],IntLiteral(900)),VarDecl(Id("jerry"),[],None),VarDecl(Id("tom"),[],IntLiteral(200))],[If([(BinaryOp("<",BinaryOp("-",Id("pothos"),Id("athos")),IntLiteral(400)),[],[Assign(Id("jerry"),BinaryOp("-",Id("pothos"),Id("tom")))])],([],[Assign(Id("jerry"),BinaryOp("-",Id("athos"),Id("tom")))]))]))])
        self.assertTrue(TestAST.checkASTGen(input,expect,353))

    def test_if_statement_8(self):
        input = """
        Function: test
        Body:
            Var: time, greeting;
            time = date();
            If time < 10 Then greeting = "Good morning";
            ElseIf time < 20 Then greeting = "Good day";
            Else greeting = "Good evening";
            EndIf.
        EndBody.
        """ 
        expect = Program([FuncDecl(Id("test"),[],([VarDecl(Id("time"),[],None),VarDecl(Id("greeting"),[],None)],[Assign(Id("time"),CallExpr(Id("date"),[])),If([(BinaryOp("<",Id("time"),IntLiteral(10)),[],[Assign(Id("greeting"),StringLiteral("Good morning"))]),(BinaryOp("<",Id("time"),IntLiteral(20)),[],[Assign(Id("greeting"),StringLiteral("Good day"))])],([],[Assign(Id("greeting"),StringLiteral("Good evening"))]))]))])
        self.assertTrue(TestAST.checkASTGen(input,expect,354))

    def test_if_statement_9(self):
        input = """
        Function: test
        Body:
            Var: num = 10;
            If num > 0 Then print("Positive number");
            Else 
                If num == 0 Then print("Zero");
                Else print("Negative number");
                EndIf.
            EndIf.
        EndBody.
        """ 
        expect = Program([FuncDecl(Id("test"),[],([VarDecl(Id("num"),[],IntLiteral(10))],[If([(BinaryOp(">",Id("num"),IntLiteral(0)),[],[CallStmt(Id("print"),[StringLiteral("Positive number")])])],([],[If([(BinaryOp("==",Id("num"),IntLiteral(0)),[],[CallStmt(Id("print"),[StringLiteral("Zero")])])],([],[CallStmt(Id("print"),[StringLiteral("Negative number")])]))]))]))])
        self.assertTrue(TestAST.checkASTGen(input,expect,355))

    def test_if_statement_10(self):
        input = """
        Function: test
        Body:
            Var: a = 3, b = 4, c = 5;
            If (a < b + c) && ( b < a + c) && ( c < a + b) Then
                If (a*a==b*b+c*c) || (b*b==a*a+c*c) || (c*c== a*a+b*b) Then
                    print("Day la tam giac vuong");
                EndIf.
            ElseIf (a==b) && (b==c) Then print("Day la tam giac deu");
            ElseIf (a==b) || (a==c) || (b==c) Then print("Day la tam giac can");
            ElseIf (a*a > b*b+c*c) || (b*b > a*a+c*c) || (c*c > a*a+b*b) Then print("Day la tam giac tu");
            Else print("Day la tam giac nhon");
            EndIf.
        EndBody.
        """ 
        expect = Program([FuncDecl(Id("test"),[],([VarDecl(Id("a"),[],IntLiteral(3)),VarDecl(Id("b"),[],IntLiteral(4)),VarDecl(Id("c"),[],IntLiteral(5))],[If([(BinaryOp("&&",BinaryOp("&&",BinaryOp("<",Id("a"),BinaryOp("+",Id("b"),Id("c"))),BinaryOp("<",Id("b"),BinaryOp("+",Id("a"),Id("c")))),BinaryOp("<",Id("c"),BinaryOp("+",Id("a"),Id("b")))),[],[If([(BinaryOp("||",BinaryOp("||",BinaryOp("==",BinaryOp("*",Id("a"),Id("a")),BinaryOp("+",BinaryOp("*",Id("b"),Id("b")),BinaryOp("*",Id("c"),Id("c")))),BinaryOp("==",BinaryOp("*",Id("b"),Id("b")),BinaryOp("+",BinaryOp("*",Id("a"),Id("a")),BinaryOp("*",Id("c"),Id("c"))))),BinaryOp("==",BinaryOp("*",Id("c"),Id("c")),BinaryOp("+",BinaryOp("*",Id("a"),Id("a")),BinaryOp("*",Id("b"),Id("b"))))),[],[CallStmt(Id("print"),[StringLiteral("Day la tam giac vuong")])])],([],[]))]),(BinaryOp("&&",BinaryOp("==",Id("a"),Id("b")),BinaryOp("==",Id("b"),Id("c"))),[],[CallStmt(Id("print"),[StringLiteral("Day la tam giac deu")])]),(BinaryOp("||",BinaryOp("||",BinaryOp("==",Id("a"),Id("b")),BinaryOp("==",Id("a"),Id("c"))),BinaryOp("==",Id("b"),Id("c"))),[],[CallStmt(Id("print"),[StringLiteral("Day la tam giac can")])]),(BinaryOp("||",BinaryOp("||",BinaryOp(">",BinaryOp("*",Id("a"),Id("a")),BinaryOp("+",BinaryOp("*",Id("b"),Id("b")),BinaryOp("*",Id("c"),Id("c")))),BinaryOp(">",BinaryOp("*",Id("b"),Id("b")),BinaryOp("+",BinaryOp("*",Id("a"),Id("a")),BinaryOp("*",Id("c"),Id("c"))))),BinaryOp(">",BinaryOp("*",Id("c"),Id("c")),BinaryOp("+",BinaryOp("*",Id("a"),Id("a")),BinaryOp("*",Id("b"),Id("b"))))),[],[CallStmt(Id("print"),[StringLiteral("Day la tam giac tu")])])],([],[CallStmt(Id("print"),[StringLiteral("Day la tam giac nhon")])]))]))])
        self.assertTrue(TestAST.checkASTGen(input,expect,356))

    def test_if_statement_11(self):
        input = """
        Function: test
        Body:
            Var: i = 20, a, b, c;
            If i == 10 Then 
                a = 1;
                b = 2;
                c = a + b;
            ElseIf i == 15 Then
                a = 3;
                b = 4;
                c = b - a;
            ElseIf i == 20 Then
                a = 2;
                b = 2;
                c = a*2 + b*3;
            EndIf.
        EndBody.
        """ 
        expect = Program([FuncDecl(Id("test"),[],([VarDecl(Id("i"),[],IntLiteral(20)),VarDecl(Id("a"),[],None),VarDecl(Id("b"),[],None),VarDecl(Id("c"),[],None)],[If([(BinaryOp("==",Id("i"),IntLiteral(10)),[],[Assign(Id("a"),IntLiteral(1)),Assign(Id("b"),IntLiteral(2)),Assign(Id("c"),BinaryOp("+",Id("a"),Id("b")))]),(BinaryOp("==",Id("i"),IntLiteral(15)),[],[Assign(Id("a"),IntLiteral(3)),Assign(Id("b"),IntLiteral(4)),Assign(Id("c"),BinaryOp("-",Id("b"),Id("a")))]),(BinaryOp("==",Id("i"),IntLiteral(20)),[],[Assign(Id("a"),IntLiteral(2)),Assign(Id("b"),IntLiteral(2)),Assign(Id("c"),BinaryOp("+",BinaryOp("*",Id("a"),IntLiteral(2)),BinaryOp("*",Id("b"),IntLiteral(3))))])],([],[]))]))])
        self.assertTrue(TestAST.checkASTGen(input,expect,357))

    def test_if_statement_12(self):
        input = """
        Function: sum
        Parameter: n
        Body:
            If (n == 0) Then Return 0;
            EndIf.
            Return n + sum(n - 1);
        EndBody.
        """ 
        expect = Program([FuncDecl(Id("sum"),[VarDecl(Id("n"),[],None)],([],[If([(BinaryOp("==",Id("n"),IntLiteral(0)),[],[Return(IntLiteral(0))])],([],[])),Return(BinaryOp("+",Id("n"),CallExpr(Id("sum"),[BinaryOp("-",Id("n"),IntLiteral(1))])))]))])
        self.assertTrue(TestAST.checkASTGen(input,expect,358))

    def test_364(self):
        input = """
        Function: test
        Body:
            Return 1 +. 4e25 \. 2.;
        EndBody.
        """ 
        expect = Program([FuncDecl(Id("test"),[],([],[Return(BinaryOp("+.",IntLiteral(1),BinaryOp("\.",FloatLiteral(4e+25),FloatLiteral(2.0))))]))])
        self.assertTrue(TestAST.checkASTGen(input,expect,359))

    def test_367(self):
        input = """Function: foo 
        Body: 
            Return;
        EndBody.""" 
        expect = Program([FuncDecl(Id("foo"),[],([],[Return(None)]))])
        self.assertTrue(TestAST.checkASTGen(input,expect,360))

    def test_368(self):
        input = """
        Var: x;
        Function: main
        Body:
        x = 10;
        fact (x);
        EndBody.
        """ 
        expect = Program([VarDecl(Id("x"),[],None),FuncDecl(Id("main"),[],([],[Assign(Id("x"),IntLiteral(10)),CallStmt(Id("fact"),[Id("x")])]))])
        self.assertTrue(TestAST.checkASTGen(input,expect,361))

    def test_369(self):
        input = """
        Function: hello
        Parameter: str
        Body:
            Var: x = 2;
            hello(str);
            hello(x);
        EndBody.
        """ 
        expect = Program([FuncDecl(Id("hello"),[VarDecl(Id("str"),[],None)],([VarDecl(Id("x"),[],IntLiteral(2))],[CallStmt(Id("hello"),[Id("str")]),CallStmt(Id("hello"),[Id("x")])]))])
        self.assertTrue(TestAST.checkASTGen(input,expect,362))

    def test_370(self):
        input = """Var:x =5 ;""" 
        expect = Program([VarDecl(Id("x"),[],IntLiteral(5))])
        self.assertTrue(TestAST.checkASTGen(input,expect,363))

    def test_371(self):
        input = """
        Var: x;
        Function: fact
        Parameter: n
        Body:
        If n == 0 Then
        Return 1;
        Else
        Return n * fact (n - 1);
        EndIf.
        EndBody.
        Function: main
        Body:
        x = 10;
        fact (x);
        EndBody.
        """ 
        expect = Program([VarDecl(Id("x"),[],None),FuncDecl(Id("fact"),[VarDecl(Id("n"),[],None)],([],[If([(BinaryOp("==",Id("n"),IntLiteral(0)),[],[Return(IntLiteral(1))])],([],[Return(BinaryOp("*",Id("n"),CallExpr(Id("fact"),[BinaryOp("-",Id("n"),IntLiteral(1))])))]))])),FuncDecl(Id("main"),[],([],[Assign(Id("x"),IntLiteral(10)),CallStmt(Id("fact"),[Id("x")])]))])
        self.assertTrue(TestAST.checkASTGen(input,expect,364))

    def test_372(self):
        input = """Var: s___091 = {"abc",{"zyz"}}, arr[1][2]= {{{{"H","hihi",123}}}};""" 
        expect = Program([VarDecl(Id("s___091"),[],ArrayLiteral([StringLiteral("abc"),ArrayLiteral([StringLiteral("zyz")])])),VarDecl(Id("arr"),[1,2],ArrayLiteral([ArrayLiteral([ArrayLiteral([ArrayLiteral([StringLiteral("H"),StringLiteral("hihi"),IntLiteral(123)])])])]))])
        self.assertTrue(TestAST.checkASTGen(input,expect,365))

    def test_373(self):
        input = """Var:x[12]="None";""" 
        expect = Program([VarDecl(Id("x"),[12],StringLiteral("None"))])
        self.assertTrue(TestAST.checkASTGen(input,expect,366))

    def test_374(self):
        input = """Var:x[1][13][1][16]={0.5, 9e21};""" 
        expect = Program([VarDecl(Id("x"),[1,13,1,16],ArrayLiteral([FloatLiteral(0.5),FloatLiteral(9e+21)]))])
        self.assertTrue(TestAST.checkASTGen(input,expect,367))

    def test_375(self):
        input = """Var: arr[5][6] = {1,2}, y[1];""" 
        expect = Program([VarDecl(Id("arr"),[5,6],ArrayLiteral([IntLiteral(1),IntLiteral(2)])),VarDecl(Id("y"),[1],None)])
        self.assertTrue(TestAST.checkASTGen(input,expect,368))

    def test_376(self):
        input = """Var: b = True, c = False;""" 
        expect = Program([VarDecl(Id("b"),[],BooleanLiteral(True)),VarDecl(Id("c"),[],BooleanLiteral(False))])
        self.assertTrue(TestAST.checkASTGen(input,expect,369))

    def test_377(self):
        input = """Var:x[0x13];""" 
        expect = Program([VarDecl(Id("x"),[19],None)])
        self.assertTrue(TestAST.checkASTGen(input,expect,370))

    def test_378(self):
        input = """
        Var: simp_l_3;
        Function: test
        Parameter: a, b
        Body:
            print(a);
            print(b);
        EndBody.
        """ 
        expect = Program([VarDecl(Id("simp_l_3"),[],None),FuncDecl(Id("test"),[VarDecl(Id("a"),[],None),VarDecl(Id("b"),[],None)],([],[CallStmt(Id("print"),[Id("a")]),CallStmt(Id("print"),[Id("b")])]))])
        self.assertTrue(TestAST.checkASTGen(input,expect,371))

    def test_379(self):
        input = """
        Var: simp_2_3;
        Function: test
        Parameter: a, b, d, e, f, g, h, j[1000], k[2000]
        Body:
            a = b +. d;
            g = h && f || True;
            Return a;
        EndBody.
        """ 
        expect = Program([VarDecl(Id("simp_2_3"),[],None),FuncDecl(Id("test"),[VarDecl(Id("a"),[],None),VarDecl(Id("b"),[],None),VarDecl(Id("d"),[],None),VarDecl(Id("e"),[],None),VarDecl(Id("f"),[],None),VarDecl(Id("g"),[],None),VarDecl(Id("h"),[],None),VarDecl(Id("j"),[1000],None),VarDecl(Id("k"),[2000],None)],([],[Assign(Id("a"),BinaryOp("+.",Id("b"),Id("d"))),Assign(Id("g"),BinaryOp("||",BinaryOp("&&",Id("h"),Id("f")),BooleanLiteral(True))),Return(Id("a"))]))])
        self.assertTrue(TestAST.checkASTGen(input,expect,372))

    def test_380(self):
        input = """
        Var: a__Rr1[2][2] = {{0.9e2,10.e4},{22,212}};
        Function: test
        Parameter: c[1]
        Body:
            c[0] = 1-1;
            Return 2;
        EndBody.
        """ 
        expect = Program([VarDecl(Id("a__Rr1"),[2,2],ArrayLiteral([ArrayLiteral([FloatLiteral(90.0),FloatLiteral(100000.0)]),ArrayLiteral([IntLiteral(22),IntLiteral(212)])])),FuncDecl(Id("test"),[VarDecl(Id("c"),[1],None)],([],[Assign(ArrayCell(Id("c"),[IntLiteral(0)]),BinaryOp("-",IntLiteral(1),IntLiteral(1))),Return(IntLiteral(2))]))])
        self.assertTrue(TestAST.checkASTGen(input,expect,373))

    def test_382(self):
        input = """
        Var: a;
        Function: test
        Body:
            arr[foo()][foo(b[2][3])] = {{2,3,4},{4,5,6}};
            Return;
        EndBody.
        """ 
        expect = Program([VarDecl(Id("a"),[],None),FuncDecl(Id("test"),[],([],[Assign(ArrayCell(Id("arr"),[CallExpr(Id("foo"),[]),CallExpr(Id("foo"),[ArrayCell(Id("b"),[IntLiteral(2),IntLiteral(3)])])]),ArrayLiteral([ArrayLiteral([IntLiteral(2),IntLiteral(3),IntLiteral(4)]),ArrayLiteral([IntLiteral(4),IntLiteral(5),IntLiteral(6)])])),Return(None)]))])
        self.assertTrue(TestAST.checkASTGen(input,expect,374))

    def test_383(self):
        input = """
        Var: s;
        Function: square
        Body:
            Var: h; **height of hcn**
            **Some 
            thing**
            Return h*h; 
        EndBody.
        """ 
        expect = Program([VarDecl(Id("s"),[],None),FuncDecl(Id("square"),[],([VarDecl(Id("h"),[],None)],[Return(BinaryOp("*",Id("h"),Id("h")))]))])
        self.assertTrue(TestAST.checkASTGen(input,expect,375))

    def test_384(self):
        input = """
        Var: s;
        Function: foo
        Parameter: s
        Body:
            s = "hi_1";
            Return foo("hi");
        EndBody.
        """ 
        expect = Program([VarDecl(Id("s"),[],None),FuncDecl(Id("foo"),[VarDecl(Id("s"),[],None)],([],[Assign(Id("s"),StringLiteral("hi_1")),Return(CallExpr(Id("foo"),[StringLiteral("hi")]))]))])
        self.assertTrue(TestAST.checkASTGen(input,expect,376))

    def test_var_decl_1(self):
        input = """Var: a = 5;""" 
        expect = Program([VarDecl(Id("a"),[],IntLiteral(5))])
        self.assertTrue(TestAST.checkASTGen(input,expect,377))

    def test_var_decl_2(self):
        input = """Var: arr = {1,2}, a[10][22], e=40e5, c, d, f=20;
                """ 
        expect = Program([VarDecl(Id("arr"),[],ArrayLiteral([IntLiteral(1),IntLiteral(2)])),VarDecl(Id("a"),[10,22],None),VarDecl(Id("e"),[],FloatLiteral(4000000.0)),VarDecl(Id("c"),[],None),VarDecl(Id("d"),[],None),VarDecl(Id("f"),[],IntLiteral(20))])
        self.assertTrue(TestAST.checkASTGen(input,expect,378))

    def test_var_decl_3(self):
        input = """Var: b[2][3] = {{2,3,4},{4,5,6}};""" 
        expect = Program([VarDecl(Id("b"),[2,3],ArrayLiteral([ArrayLiteral([IntLiteral(2),IntLiteral(3),IntLiteral(4)]),ArrayLiteral([IntLiteral(4),IntLiteral(5),IntLiteral(6)])]))])
        self.assertTrue(TestAST.checkASTGen(input,expect,379))

    def test_var_decl_4(self):
        input = """Var: c, d = 6, e, f;""" 
        expect = Program([VarDecl(Id("c"),[],None),VarDecl(Id("d"),[],IntLiteral(6)),VarDecl(Id("e"),[],None),VarDecl(Id("f"),[],None)])
        self.assertTrue(TestAST.checkASTGen(input,expect,380))

    def test_var_decl_5(self):
        input = """Var: m, n[10];""" 
        expect = Program([VarDecl(Id("m"),[],None),VarDecl(Id("n"),[10],None)])
        self.assertTrue(TestAST.checkASTGen(input,expect,381))

    def test_var_decl_6(self):
        input = """Var: s="happyBirthDay";""" 
        expect = Program([VarDecl(Id("s"),[],StringLiteral("happyBirthDay"))])
        self.assertTrue(TestAST.checkASTGen(input,expect,382))

    def test_var_decl_7(self):
        input = """Var: s_1="'"superMan is'".", s_2="happyBirthDay", arr = {**"toYou"** 12, 99.4e2};""" 
        expect = Program([VarDecl(Id("s_1"),[],StringLiteral("'\"superMan is'\".")),VarDecl(Id("s_2"),[],StringLiteral("happyBirthDay")),VarDecl(Id("arr"),[],ArrayLiteral([IntLiteral(12),FloatLiteral(9940.0)]))])
        self.assertTrue(TestAST.checkASTGen(input,expect,383))

    def test_var_decl_8(self):
        input = """Var: arr[10], c[99][3][2], arr2[0];
                """ 
        expect = Program([VarDecl(Id("arr"),[10],None),VarDecl(Id("c"),[99,3,2],None),VarDecl(Id("arr2"),[0],None)])
        self.assertTrue(TestAST.checkASTGen(input,expect,384))

    def test_var_decl_9(self):
        input = """Var: s="DaiH0cB4ckHo4", x= 12.2e54, c=0xF212;
                """ 
        expect = Program([VarDecl(Id("s"),[],StringLiteral("DaiH0cB4ckHo4")),VarDecl(Id("x"),[],FloatLiteral(1.22e+55)),VarDecl(Id("c"),[],IntLiteral(61970))])
        self.assertTrue(TestAST.checkASTGen(input,expect,385))

    def test_var_decl_10(self):
        input = """Var: arr[2][3][5] = {{"string", "s!@#$"}, {{542.10e21, 2., 9e5}}, {{1023, 1024, 2098}, {0x2141, 0xF912}}};
                """ 
        expect = Program([VarDecl(Id("arr"),[2,3,5],ArrayLiteral([ArrayLiteral([StringLiteral("string"),StringLiteral("s!@#$")]),ArrayLiteral([ArrayLiteral([FloatLiteral(5.421e+23),FloatLiteral(2.0),FloatLiteral(900000.0)])]),ArrayLiteral([ArrayLiteral([IntLiteral(1023),IntLiteral(1024),IntLiteral(2098)]),ArrayLiteral([IntLiteral(8513),IntLiteral(63762)])])]))])
        self.assertTrue(TestAST.checkASTGen(input,expect,386))

    def test_var_decl_11(self):
        input = """
        Var: a;
        Function: test
        Body:
            Var: a_ = 10., b = 5., c3 = 9;
        EndBody.
        """ 
        expect = Program([VarDecl(Id("a"),[],None),FuncDecl(Id("test"),[],([VarDecl(Id("a_"),[],FloatLiteral(10.0)),VarDecl(Id("b"),[],FloatLiteral(5.0)),VarDecl(Id("c3"),[],IntLiteral(9))],[]))])
        self.assertTrue(TestAST.checkASTGen(input,expect,387))

    def test_var_decl_12(self):
        input = """
        Var: a;
        Function: test
        Body:
            Var: z_1[2][3] = {{6572e21, 2341e+56, 0.5},{"%^DFGZ", "Rvul^%",""}}, a[24], c;
        EndBody.
        """ 
        expect = Program([VarDecl(Id("a"),[],None),FuncDecl(Id("test"),[],([VarDecl(Id("z_1"),[2,3],ArrayLiteral([ArrayLiteral([FloatLiteral(6.572e+24),FloatLiteral(2.341e+59),FloatLiteral(0.5)]),ArrayLiteral([StringLiteral("%^DFGZ"),StringLiteral("Rvul^%"),StringLiteral("")])])),VarDecl(Id("a"),[24],None),VarDecl(Id("c"),[],None)],[]))])
        self.assertTrue(TestAST.checkASTGen(input,expect,388))

    def test_var_decl_13(self):
        input = """
        Function: test
        Body:
            Var: x = 43.9e10, y = 542, z = 0xFF2, t = 0O221, s="ThisIsString", w = False, arr[2][1] = {{2e5},{2}}; 
        EndBody.
        """ 
        expect = Program([FuncDecl(Id("test"),[],([VarDecl(Id("x"),[],FloatLiteral(439000000000.0)),VarDecl(Id("y"),[],IntLiteral(542)),VarDecl(Id("z"),[],IntLiteral(4082)),VarDecl(Id("t"),[],IntLiteral(145)),VarDecl(Id("s"),[],StringLiteral("ThisIsString")),VarDecl(Id("w"),[],BooleanLiteral(False)),VarDecl(Id("arr"),[2,1],ArrayLiteral([ArrayLiteral([FloatLiteral(200000.0)]),ArrayLiteral([IntLiteral(2)])]))],[]))])
        self.assertTrue(TestAST.checkASTGen(input,expect,389))

    def test_while_statement_1(self):
        input = """
        Function: test
        Body:
            While True Do
            EndWhile.
        EndBody.
        """ 
        expect = Program([FuncDecl(Id("test"),[],([],[While(BooleanLiteral(True),([],[]))]))])
        self.assertTrue(TestAST.checkASTGen(input,expect,390))

    def test_while_statement_2(self):
        input = """
        Function: test
        Parameter: n
        Body:
            Var: i = 0;
            While 1 Do
                i = i + 1;
                If (i == 10) Then write("OK");
                EndIf.
            EndWhile.
        EndBody.
        """ 
        expect = Program([FuncDecl(Id("test"),[VarDecl(Id("n"),[],None)],([VarDecl(Id("i"),[],IntLiteral(0))],[While(IntLiteral(1),([],[Assign(Id("i"),BinaryOp("+",Id("i"),IntLiteral(1))),If([(BinaryOp("==",Id("i"),IntLiteral(10)),[],[CallStmt(Id("write"),[StringLiteral("OK")])])],([],[]))]))]))])
        self.assertTrue(TestAST.checkASTGen(input,expect,391))

    def test_while_statement_3(self):
        input = """Function: foo 
        Parameter: n
        Body: 
            While i < 5 Do
                a = b +. 1.0;
            EndWhile.
        EndBody.""" 
        expect = Program([FuncDecl(Id("foo"),[VarDecl(Id("n"),[],None)],([],[While(BinaryOp("<",Id("i"),IntLiteral(5)),([],[Assign(Id("a"),BinaryOp("+.",Id("b"),FloatLiteral(1.0)))]))]))])
        self.assertTrue(TestAST.checkASTGen(input,expect,392))

    def test_while_statement_4(self):
        input = """
        Function: test
        Parameter: t
        Body:
            While t < 10 Do
                If t%2 Then t = t + 1;
                Else t = t + 2; 
                EndIf.
            EndWhile.
        EndBody.
        """ 
        expect = Program([FuncDecl(Id("test"),[VarDecl(Id("t"),[],None)],([],[While(BinaryOp("<",Id("t"),IntLiteral(10)),([],[If([(BinaryOp("%",Id("t"),IntLiteral(2)),[],[Assign(Id("t"),BinaryOp("+",Id("t"),IntLiteral(1)))])],([],[Assign(Id("t"),BinaryOp("+",Id("t"),IntLiteral(2)))]))]))]))])
        self.assertTrue(TestAST.checkASTGen(input,expect,393))

    def test_while_statement_5(self):
        input = """
        Function: test
        Body:
            Var: outer = 1;
            While (outer <= 5) Do
                Var: inner = 1;
                While (inner <= 5) Do
                    print(inner);
                    inner = inner + 1;
                EndWhile.
                outer = outer + 1;
            EndWhile.
        EndBody.
        """ 
        expect = Program([FuncDecl(Id("test"),[],([VarDecl(Id("outer"),[],IntLiteral(1))],[While(BinaryOp("<=",Id("outer"),IntLiteral(5)),([VarDecl(Id("inner"),[],IntLiteral(1))],[While(BinaryOp("<=",Id("inner"),IntLiteral(5)),([],[CallStmt(Id("print"),[Id("inner")]),Assign(Id("inner"),BinaryOp("+",Id("inner"),IntLiteral(1)))])),Assign(Id("outer"),BinaryOp("+",Id("outer"),IntLiteral(1)))]))]))])
        self.assertTrue(TestAST.checkASTGen(input,expect,394))

    def test_while_statement_6(self):
        input = """
        Function: test
        Body:
            Var: x = False, t = 100, a;
            While (!x || t == 2) Do
                x = True;
                a = x;
                x = a;
                t = t - 1;
            EndWhile.
        EndBody.
        """ 
        expect = Program([FuncDecl(Id("test"),[],([VarDecl(Id("x"),[],BooleanLiteral(False)),VarDecl(Id("t"),[],IntLiteral(100)),VarDecl(Id("a"),[],None)],[While(BinaryOp("==",BinaryOp("||",UnaryOp("!",Id("x")),Id("t")),IntLiteral(2)),([],[Assign(Id("x"),BooleanLiteral(True)),Assign(Id("a"),Id("x")),Assign(Id("x"),Id("a")),Assign(Id("t"),BinaryOp("-",Id("t"),IntLiteral(1)))]))]))])
        self.assertTrue(TestAST.checkASTGen(input,expect,395))

    def test_while_statement_7(self):
        input = """
        Function: test
        Parameter: m, n, o, p
        Body:
            Var: x;
            While (m <= 2) Do
                While (n >= 1) Do
                    While (o <= n) Do
                        o = o - 1;
                        While (p <= 2) Do
                            p = p + 1;
                        EndWhile.
                    EndWhile.
                    x = True;
                    n = n - 1;
                EndWhile.
                x = m * n * p * o;
                m = m + 1;
            EndWhile.
        EndBody.
        """ 
        expect = Program([FuncDecl(Id("test"),[VarDecl(Id("m"),[],None),VarDecl(Id("n"),[],None),VarDecl(Id("o"),[],None),VarDecl(Id("p"),[],None)],([VarDecl(Id("x"),[],None)],[While(BinaryOp("<=",Id("m"),IntLiteral(2)),([],[While(BinaryOp(">=",Id("n"),IntLiteral(1)),([],[While(BinaryOp("<=",Id("o"),Id("n")),([],[Assign(Id("o"),BinaryOp("-",Id("o"),IntLiteral(1))),While(BinaryOp("<=",Id("p"),IntLiteral(2)),([],[Assign(Id("p"),BinaryOp("+",Id("p"),IntLiteral(1)))]))])),Assign(Id("x"),BooleanLiteral(True)),Assign(Id("n"),BinaryOp("-",Id("n"),IntLiteral(1)))])),Assign(Id("x"),BinaryOp("*",BinaryOp("*",BinaryOp("*",Id("m"),Id("n")),Id("p")),Id("o"))),Assign(Id("m"),BinaryOp("+",Id("m"),IntLiteral(1)))]))]))])
        self.assertTrue(TestAST.checkASTGen(input,expect,396))

    def test_while_statement_8(self):
        input = """
        Function: test
        Body:
            Var: i, arr[100][100];
            While (i < 100) Do
                For (j = 1, j < 100, 1) Do
                    arr[i][j] = 1;
                EndFor.
                i = i + 1;
            EndWhile.
        EndBody.
        """ 
        expect = Program([FuncDecl(Id("test"),[],([VarDecl(Id("i"),[],None),VarDecl(Id("arr"),[100,100],None)],[While(BinaryOp("<",Id("i"),IntLiteral(100)),([],[For(Id("j"),IntLiteral(1),BinaryOp("<",Id("j"),IntLiteral(100)),IntLiteral(1),([],[Assign(ArrayCell(Id("arr"),[Id("i"),Id("j")]),IntLiteral(1))])),Assign(Id("i"),BinaryOp("+",Id("i"),IntLiteral(1)))]))]))])
        self.assertTrue(TestAST.checkASTGen(input,expect,397))

    def test_while_statement_9(self):
        input = """
        Function: lcd **LCD of n**
        Parameter: n
        Body:
            Var: i;
            i = n - 1;
            While (n % i != 0) Do
                i = i - 1;
            EndWhile.
            writeln(i);
        EndBody.
        """ 
        expect = Program([FuncDecl(Id("lcd"),[VarDecl(Id("n"),[],None)],([VarDecl(Id("i"),[],None)],[Assign(Id("i"),BinaryOp("-",Id("n"),IntLiteral(1))),While(BinaryOp("!=",BinaryOp("%",Id("n"),Id("i")),IntLiteral(0)),([],[Assign(Id("i"),BinaryOp("-",Id("i"),IntLiteral(1)))])),CallStmt(Id("writeln"),[Id("i")])]))])
        self.assertTrue(TestAST.checkASTGen(input,expect,398))

    def test_while_statement_10(self):
        input = """
        Function: sNum **square number**
        Parameter: n
        Body:
            Var: i = 0;
            While (i*i <= n) Do
                If (i*i == n) Then
                    writeln(n);
                    Return;
                EndIf.
                i = i + 1;
            EndWhile.
        EndBody.
        """ 
        expect = Program([FuncDecl(Id("sNum"),[VarDecl(Id("n"),[],None)],([VarDecl(Id("i"),[],IntLiteral(0))],[While(BinaryOp("<=",BinaryOp("*",Id("i"),Id("i")),Id("n")),([],[If([(BinaryOp("==",BinaryOp("*",Id("i"),Id("i")),Id("n")),[],[CallStmt(Id("writeln"),[Id("n")]),Return(None)])],([],[])),Assign(Id("i"),BinaryOp("+",Id("i"),IntLiteral(1)))]))]))])
        self.assertTrue(TestAST.checkASTGen(input,expect,399))

    def test_for_statement_8(self):
        input = """
        Function: test
        Body:
            Var: arr[10][10];
            For (i = 0, i < 10, 1) Do  
                For (j = 0, j < 10, 1) Do
                    arr[i][j] = 0;
                EndFor.
            EndFor.
        EndBody.
        """ 
        expect = Program([FuncDecl(Id("test"),[],([VarDecl(Id("arr"),[10,10],None)],[For(Id("i"),IntLiteral(0),BinaryOp("<",Id("i"),IntLiteral(10)),IntLiteral(1),([],[For(Id("j"),IntLiteral(0),BinaryOp("<",Id("j"),IntLiteral(10)),IntLiteral(1),([],[Assign(ArrayCell(Id("arr"),[Id("i"),Id("j")]),IntLiteral(0))]))]))]))])
        self.assertTrue(TestAST.checkASTGen(input,expect,400))
