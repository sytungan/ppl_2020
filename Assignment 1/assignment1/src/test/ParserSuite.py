import unittest
from TestUtils import TestParser

class ParserSuite(unittest.TestCase):
    def test_simple_program(self):
        """Simple program: int main() {} """
        input = """
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
        input = """
Function: foo 
        Parameter: n
        Body: 
            fact (x) + 3;
        EndBody."""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,203))