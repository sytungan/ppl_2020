import unittest
from TestUtils import TestChecker
from StaticError import *
from AST import *

class CheckSuite(unittest.TestCase):
    def test_418(self):
        """Created automatically"""
        input = r"""
        Var: x[5];
        Var: y[5];
        Function: main
        Body:
            x = {1.5,2.5,3.5,4.5,5.};
            y = {1,2,3,4,5};
            y = {1,2,3,4,6};
            y = foo();
            x = foo();
        EndBody.
        Function: foo
        Body:
        EndBody.
        """
        expect = str()
        self.assertTrue(TestChecker.test(input,expect,418))
        