import unittest
from TestUtils import TestParser

class ParserSuite(unittest.TestCase):
    def test_simple_program(self):
        """Simple program: int main() {} """
        input = """
        Var : c, d = 6, e, f;
        Function: foo 
        Parameter: n 
        Body: 
            c = a < 4;
            c = !a; 
        EndBody.
"""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,201))
    
    def test_wrong_miss_close(self):
        """Miss variable"""
        input = """Var: ;"""
        expect = "Error on line 1 col 5: ;"
        self.assertTrue(TestParser.checkParser(input,expect,202))
    def test_num_1(self):
        """Test 01"""
        input = """ Function: foo 
        Parameter: n 
        Body: 
            If !a Then b = 5; EndIf.
        EndBody.
        """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,203))
        
    def test_num_2(self):
        input = """ Function: foo 
        Parameter: n 
        Body: 
            If !a Then b = 5; 
            Else c=5; 
            EndIf. 
        EndBody.
        """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,203))