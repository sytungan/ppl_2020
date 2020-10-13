import unittest
from TestUtils import TestParser

class ParserSuite(unittest.TestCase):
    def test_simple_program(self):
        """Simple program: int main() {} """
        input = """
Function: fact
Parameter: n
Body:
For (i = 0, i < 10, 2) Do
writeln(i);
EndFor.
EndBody."""
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
EndBody."""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,203))