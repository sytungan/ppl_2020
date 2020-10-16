import unittest
from TestUtils import TestLexer


class LexerSuite(unittest.TestCase):
    """test identifiers"""  
    def test_identifier1(self):
        self.assertTrue(TestLexer.checkLexeme("abc","abc,<EOF>",101))
    def test_identifier2(self):
        self.assertTrue(TestLexer.checkLexeme("a09Zx CDEbc","a09Zx,Error Token C",102))
    def test_identifier3(self):
        self.assertTrue(TestLexer.checkLexeme("qwerQWER021e2","qwerQWER021e2,<EOF>",102))
    def test_identifier4(self):
        self.assertTrue(TestLexer.checkLexeme("qwertyuioa0123456789sdfghjklzxmnbpq mnbvcxz","qwertyuioa0123456789sdfghjklzxmnbpq,mnbvcxz,<EOF>",102))

    """test keywords"""
    def test_keyword1(self):
        self.assertTrue(TestLexer.checkLexeme("BodyBreak_Continue Do","Body,Break,Error Token _",103))
    def test_keyword2(self):
        self.assertTrue(TestLexer.checkLexeme("paRameterVar While","paRameterVar,While,<EOF>",104))

    def test_comment1(self):
        self.assertTrue(TestLexer.checkLexeme("""** This is a** single-line comment.** Var""","single,-,line,comment,.,Unterminated Comment",105))
    def test_comment2(self):
        self.assertTrue(TestLexer.checkLexeme("** This is a \n multi-line \n comment. **For","For,<EOF>",106))
    def test_comment3(self):
        self.assertTrue(TestLexer.checkLexeme("***** *sample*","*,*,sample,*,<EOF>",107))

    def test_operator1(self):
        self.assertTrue(TestLexer.checkLexeme("+-Var*\\ab\\.","+,-,Var,*,\\,ab,\\.,<EOF>",208))
    def test_operator2(self):  
        self.assertTrue(TestLexer.checkLexeme("x*2\\3-4+.z\\.9.0-.y*.2%10","x,*,2,\\,3,-,4,+.,z,\\.,9.0,-.,y,*.,2,%,10,<EOF>",209))
    def test_operator3(self):
        self.assertTrue(TestLexer.checkLexeme("!x == id && True || y!=z || y >=.9.5 && id>=1 && z<=2","!,x,==,id,&&,True,||,y,!=,z,||,y,>=.,9.5,&&,id,>=,1,&&,z,<=,2,<EOF>",210))
    def test_operator4(self):
        self.assertTrue(TestLexer.checkLexeme("x>.2.0 && z<=.1.0 || e<2 && c<.1.8 || e =/= z && z > c","x,>.,2.0,&&,z,<=.,1.0,||,e,<,2,&&,c,<.,1.8,||,e,=/=,z,&&,z,>,c,<EOF>",211))
    

    def test_separator(self):
        self.assertTrue(TestLexer.checkLexeme(":)abc)}.[].;,",":,),abc,),},.,[,],.,;,,,<EOF>",109))

    def test_integer1(self):
        """test integers"""
        self.assertTrue(TestLexer.checkLexeme("01990XABC","0,1990,Error Token X",110))
    def test_integer2(self):
        self.assertTrue(TestLexer.checkLexeme("0x0 0o0F9","0,x0,0,o0F9,<EOF>",111))
    def test_integer3(self):
        self.assertTrue(TestLexer.checkLexeme("0 199 0xFF 0XABC 0o567 0O77","0,199,0xFF,0XABC,0o567,0O77,<EOF>",112))
    
    def test_float1(self):
        self.assertTrue(TestLexer.checkLexeme("12.0e3 12e3 12.e5 12.0e3 12000. 120000e-1","12.0e3,12e3,12.e5,12.0e3,12000.,120000e-1,<EOF>",113))
    def test_float2(self):
        self.assertTrue(TestLexer.checkLexeme("0e05 0x00.12e5 ","0e05,0,x00,.,12e5,<EOF>",114))
    def test_float3(self):
        self.assertTrue(TestLexer.checkLexeme(".e5 .5 01e2.32 ",".,e5,.,5,0,1e2,.,32,<EOF>",115))

    def test_boolean(self):
        self.assertTrue(TestLexer.checkLexeme("True and False","True,and,False,<EOF>",116))   

    def test_string1(self):
        self.assertTrue(TestLexer.checkLexeme(""" "This is a string containing tab \\t" ""","""This is a string containing tab \\t,<EOF>""",117))
    
    def test_string2(self):
        self.assertTrue(TestLexer.checkLexeme(""" "He asked me: '"Where is John?'"" ""","""He asked me: '"Where is John?'",<EOF>""",118))
    def test_string3(self):
        self.assertTrue(TestLexer.checkLexeme(""" "ab\\\\'"c\\n def"  ""","""ab\\\\'"c\\n def,<EOF>""",119))
    def test_string4(self):
        self.assertTrue(TestLexer.checkLexeme("""\"\"\"hello\"\"\"\"""",""",hello,,Unclosed String: """,120))
    def test_string5(self):
        self.assertTrue(TestLexer.checkLexeme(""" "'"'"ab'"c\\'"!=!!"?"  ""","""'"'"ab'"c\\',!=,!,!,?,<EOF>""",121))
    def test_string6(self):
        self.assertTrue(TestLexer.checkLexeme(""" "\\b \\f time \\r \\n \\t \\\' \\\\"  ""","""\\b \\f time \\r \\n \\t \\\' \\\\,<EOF>""",122))    

    def test_illegal_escape1(self):
        self.assertTrue(TestLexer.checkLexeme(""" "abc\\h def"  ""","""Illegal Escape In String: abc\\h""",122))
    def test_illegal_escape2(self):
        self.assertTrue(TestLexer.checkLexeme(""" "abc\\"  ""","""Illegal Escape In String: abc\\\"""",123))
    def test_illegal_escape3(self):
        self.assertTrue(TestLexer.checkLexeme(""" "thisIs\'aString"  ""","""Illegal Escape In String: thisIs\'a""",124))

    def test_unterminated_string1(self):
        self.assertTrue(TestLexer.checkLexeme(""" "abc def  ""","""Unclosed String: abc def  """,125))
    def test_unterminated_string2(self):
        self.assertTrue(TestLexer.checkLexeme(""" "abc@?~12"thisIs"x ""","""abc@?~12,thisIs,Unclosed String: x """,126))
    def test_unterminated_string3(self):
        self.assertTrue(TestLexer.checkLexeme(""" "dna def\nZSEQWQSA" ""","""Unclosed String: dna def\n""",127))
    
    def test_array1(self):
        self.assertTrue(TestLexer.checkLexeme("""{1, 5, 7, 12}""","""{1, 5, 7, 12},<EOF>""",128))
    def test_array2(self):
        self.assertTrue(TestLexer.checkLexeme("""{1, 5, 7, 12}""","""{1, 5, 7, 12},<EOF>""",128))