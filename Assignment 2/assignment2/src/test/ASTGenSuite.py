import unittest
from TestUtils import TestAST
from AST import *

from main.bkit.utils.AST import ArrayLiteral, FloatLiteral, IntLiteral, Program, StringLiteral

class ASTGenSuite(unittest.TestCase):
    def test_simple_program(self):
        """Simple program: int main() {} """
        input = """Var:x;"""
        expect = Program([VarDecl(Id("x"),[],None)])
        self.assertTrue(TestAST.checkASTGen(input,expect,300))

    def test_simple_program1(self):
        """Simple program: int main() {} """
        input = """Var:x =5 ;"""
        expect = Program([VarDecl(Id("x"),[],IntLiteral(5))])
        self.assertTrue(TestAST.checkASTGen(input,expect,301))
    
    def test_simple_program2(self):
        """Simple program: int main() {} """
        input = """Var:x[12];"""
        expect = Program([VarDecl(Id("x"),[12],None)])
        self.assertTrue(TestAST.checkASTGen(input,expect,302))
    
    def test_simple_program3(self):
        """Simple program: int main() {} """
        input = """Var:x[0x13];"""
        expect = Program([VarDecl(Id("x"),[19],None)])
        self.assertTrue(TestAST.checkASTGen(input,expect,303))
    
    def test_simple_program4(self):
        """Simple program: int main() {} """
        input = """Var:x[1][13][16]=5;"""
        expect = Program([VarDecl(Id("x"),[1,13,16],IntLiteral(5))])
        self.assertTrue(TestAST.checkASTGen(input,expect,304))
 
    def test_simple_program5(self):
        """Simple program: int main() {} """
        input = """Var: arr[5][6] = {1,2}, y[1];"""
        expect = Program([VarDecl(Id("arr"),[5,6],ArrayLiteral([IntLiteral(1),IntLiteral(2)])),VarDecl(Id("y"),[1],None)])
        self.assertTrue(TestAST.checkASTGen(input,expect,305))

    def test_simple_program6(self):
        """Simple program: int main() {} """
        input = """Var: x[5] = {1,2,"h",2.e56,""}, y = 12.;"""
        expect = Program([VarDecl(Id("x"),[5],ArrayLiteral([IntLiteral(1),IntLiteral(2),StringLiteral("h"),FloatLiteral(2.e56),StringLiteral("")])),VarDecl(Id("y"),[],FloatLiteral(12.))])
        print(expect)
        self.assertTrue(TestAST.checkASTGen(input,expect,306))

 
   