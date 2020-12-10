import unittest
from TestUtils import TestChecker
from StaticError import *
from AST import *

class CheckSuite(unittest.TestCase):
    def test_418(self):
        """Created automatically"""
        input = r"""
        Var: x;
        Function: main 
            Parameter: x[5]
            Body:
                x = {1.,2.,3.,4.,5.}
            EndBody.
        Function: foo
            Body:
                x = 2;
            EndBody.
        """
        expect = str()
        self.assertTrue(TestChecker.test(input,expect,418))
        