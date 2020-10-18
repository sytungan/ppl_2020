import unittest
from TestUtils import TestLexer


class LexerSuite(unittest.TestCase):
    """test identifiers"""  
    def test_identifier1(self):
        self.assertTrue(TestLexer.checkLexeme("abc","abc,<EOF>",101))
    def test_identifier2(self):
        self.assertTrue(TestLexer.checkLexeme("a09Zx CDEbc","a09Zx,Error Token C",102))
    def test_identifier3(self):
        self.assertTrue(TestLexer.checkLexeme("qwerQWER021e2","qwerQWER021e2,<EOF>",103))
    def test_identifier4(self):
        self.assertTrue(TestLexer.checkLexeme("qwertyuioa0123456789sdfghjklzxmnbpq mnbvcxz","qwertyuioa0123456789sdfghjklzxmnbpq,mnbvcxz,<EOF>",104))
    def test_identifier5(self):
        self.assertTrue(TestLexer.checkLexeme("ankUn_k_n__hA_niE_chan","ankUn_k_n__hA_niE_chan,<EOF>",105))
    def test_identifier6(self):
        self.assertTrue(TestLexer.checkLexeme("abcdefghjklmnopqsrtywABCDEF chU bE l04t cH04t","abcdefghjklmnopqsrtywABCDEF,chU,bE,l04t,cH04t,<EOF>",106))
    def test_identifier7(self):
        self.assertTrue(TestLexer.checkLexeme("___heHeMeOme0","Error Token _",107))
    def test_identifier8(self):
        self.assertTrue(TestLexer.checkLexeme("varFunctionBodyReturn","varFunctionBodyReturn,<EOF>",108))
    def test_identifier9(self):
        self.assertTrue(TestLexer.checkLexeme("aA0010x12e12____If_____Then__0120","aA0010x12e12____If_____Then__0120,<EOF>",109))
    def test_identifier10(self):
        self.assertTrue(TestLexer.checkLexeme("Body: 12zX1A20o12____base_10_0o52167_0Oa77____EndBody.","Body,:,12,zX1A20o12____base_10_0o52167_0Oa77____EndBody,.,<EOF>",110))
    def test_identifier11(self):
        self.assertTrue(TestLexer.checkLexeme("a = int_of_string (read ());","a,=,int_of_string,(,read,(,),),;,<EOF>",111))    

    def test_keyword1(self):
        self.assertTrue(TestLexer.checkLexeme("BodyBreak_Continue Do","Body,Break,Error Token _",112))
    def test_keyword2(self):
        self.assertTrue(TestLexer.checkLexeme("paRameterVar While","paRameterVar,While,<EOF>",113))
    def test_keyword3(self):
        self.assertTrue(TestLexer.checkLexeme("functionEndBody____\nVar*ForFor\\EndIfIf","functionEndBody____,Var,*,For,For,\\,EndIf,If,<EOF>",114))
    def test_keyword4(self):
        self.assertTrue(TestLexer.checkLexeme("ElseElseIfIfEndBodyEndIfIfEndForForEndWhileWhileEndDoDo","Else,ElseIf,If,EndBody,EndIf,If,EndFor,For,EndWhile,While,EndDo,Do,<EOF>",115))

    def test_comment1(self):
        self.assertTrue(TestLexer.checkLexeme("""** This is a** single-line comment.** Var""","single,-,line,comment,.,Unterminated Comment",116))
    def test_comment2(self):
        self.assertTrue(TestLexer.checkLexeme("** This @!#%^&^is a \n multi-line~><>: \n comment ><\\{}. **For","For,<EOF>",117))
    def test_comment3(self):
        self.assertTrue(TestLexer.checkLexeme("***** *sample*","*,*,sample,*,<EOF>",118))
    def test_comment4(self):
        self.assertTrue(TestLexer.checkLexeme("**___***bK_IT_____**__*** *","*,bK_IT_____,*,*,<EOF>",119))
    def test_comment5(self):
        self.assertTrue(TestLexer.checkLexeme("*** * ** * * *","*,*,*,<EOF>",120))
    def test_comment6(self):
        self.assertTrue(TestLexer.checkLexeme("""** This is a
                                                 * multi-line
                                                 * comment.
                                                 **""","<EOF>",121))
    def test_comment7(self):
        self.assertTrue(TestLexer.checkLexeme("""**"This"+is\\nmulti\n" ****"('"line/2-1'")"**"zzz" ""","zzz,<EOF>",122))

    def test_operator1(self):
        self.assertTrue(TestLexer.checkLexeme("+-Var*\\ab\\.","+,-,Var,*,\\,ab,\\.,<EOF>",123))
    def test_operator2(self):  
        self.assertTrue(TestLexer.checkLexeme("x*2\\3-4+.z\\.9.0-.y*.2%10","x,*,2,\\,3,-,4,+.,z,\\.,9.0,-.,y,*.,2,%,10,<EOF>",124))
    def test_operator3(self):
        self.assertTrue(TestLexer.checkLexeme("!x == id && True || y!=z || y >=.9.5 && id>=1 && z<=2","!,x,==,id,&&,True,||,y,!=,z,||,y,>=.,9.5,&&,id,>=,1,&&,z,<=,2,<EOF>",125))
    def test_operator4(self):
        self.assertTrue(TestLexer.checkLexeme("x>.2.0 && z<=.1.0 || e<2 && c<.1.8 || e =/= z && z > c","x,>.,2.0,&&,z,<=.,1.0,||,e,<,2,&&,c,<.,1.8,||,e,=/=,z,&&,z,>,c,<EOF>",126))
    def test_operator5(self):
        self.assertTrue(TestLexer.checkLexeme("s*2*\\2\\\\++-.-*.*(4. \. 3.) *. 3.14 *. r *. r *. r","s,*,2,*,\,2,\,\,+,+,-.,-,*.,*,(,4.,\.,3.,),*.,3.14,*.,r,*.,r,*.,r,<EOF>",127))
    def test_operator6(self):
        self.assertTrue(TestLexer.checkLexeme("(2*3)\\0xAF21 && 9.*.x+ 29-.12%2-0O1234567","(,2,*,3,),\\,0xAF21,&&,9.,*.,x,+,29,-.,12,%,2,-,0O1234567,<EOF>",128))
    def test_operator7(self):
        self.assertTrue(TestLexer.checkLexeme("(foo(2+x,4.\\.y)-.a[21412\\2]||!True&&False&&!!c","(,foo,(,2,+,x,,,4.,\\.,y,),-.,a,[,21412,\\,2,],||,!,True,&&,False,&&,!,!,c,<EOF>",129))
    def test_operator8(self):
        self.assertTrue(TestLexer.checkLexeme("-112*e+6091\\!<=42%12\\0xA9<=5%2&&102.!>=.12.","-,112,*,e,+,6091,\\,!,<=,42,%,12,\\,0xA9,<=,5,%,2,&&,102.,!,>=.,12.,<EOF>",130))
    def test_operator9(self):
        self.assertTrue(TestLexer.checkLexeme("57e9 - 3*a+.5*x\\y!==/=98129>.1<.2020952.<=17","57e9,-,3,*,a,+.,5,*,x,\,y,!=,=/=,98129,>.,1,<.,2020952.,<=,17,<EOF>",131))
    def test_operator10(self):
        self.assertTrue(TestLexer.checkLexeme("--0xF---++12%43%b%c == 21\\2\\2\\2\\7.*.2*.7*.2.","-,-,0xF,-,-,-,+,+,12,%,43,%,b,%,c,==,21,\,2,\,2,\,2,\,7.,*.,2,*.,7,*.,2.,<EOF>",132))
    
    

    def test_separator1(self):
        self.assertTrue(TestLexer.checkLexeme(":)abc)}.[].;,",":,),abc,),},.,[,],.,;,,,<EOF>",133))
    def test_separator2(self):
        self.assertTrue(TestLexer.checkLexeme("foo(a[12]) = c };","foo,(,a,[,12,],),=,c,},;,<EOF>",134))
    def test_separator3(self):
        self.assertTrue(TestLexer.checkLexeme("Body::::::{[","Body,:,:,:,:,:,:,{,[,<EOF>",135))
    def test_separator4(self):
        self.assertTrue(TestLexer.checkLexeme("Parameter:,Body:][}.}[}{(EndIfIf.);;","Parameter,:,,,Body,:,],[,},.,},[,},{,(,EndIf,If,.,),;,;,<EOF>",136))
    def test_separator5(self):
        self.assertTrue(TestLexer.checkLexeme("(({:([[[]))jaNhu@Em_Nhi_nLai)];","(,(,{,:,(,[,[,[,],),),jaNhu,Error Token @",137))

    def test_integer1(self):
        """test integers"""
        self.assertTrue(TestLexer.checkLexeme("01990XABC","0,1990,Error Token X",138))
    def test_integer2(self):
        self.assertTrue(TestLexer.checkLexeme("0x0 0o0F9","0,x0,0,o0F9,<EOF>",139))
    def test_integer3(self):
        self.assertTrue(TestLexer.checkLexeme("0 199 0xFF 0XABC 0o567 0O77","0,199,0xFF,0XABC,0o567,0O77,<EOF>",140))
    def test_integer4(self):
        self.assertTrue(TestLexer.checkLexeme("20398723819290132 0942112212","20398723819290132,0,942112212,<EOF>",141))
    def test_integer5(self):
        self.assertTrue(TestLexer.checkLexeme("0x0123456789ABCDEF","0,x0123456789ABCDEF,<EOF>",142))
    def test_integer6(self):
        self.assertTrue(TestLexer.checkLexeme("0x9876543210ABCDEF 0X9876543210abcdef","0x9876543210ABCDEF,0X9876543210,abcdef,<EOF>",143))       
    def test_integer7(self):
        self.assertTrue(TestLexer.checkLexeme("0X112FACDB","0X112FACDB,<EOF>",144))
    def test_integer8(self):
        self.assertTrue(TestLexer.checkLexeme("0o01234567 0O012","0,o01234567,0,Error Token O",145))
    def test_integer9(self):
        self.assertTrue(TestLexer.checkLexeme("0o12345670abcdef","0o12345670,abcdef,<EOF>",146))
    def test_integer10(self):
        self.assertTrue(TestLexer.checkLexeme("0o1234567891011 0O1234567","0o1234567,891011,0O1234567,<EOF>",147))
    def test_integer11(self):
        self.assertTrue(TestLexer.checkLexeme("2519489+5202056 000 5240492	3511181\\3367084	4688584	1797485	8139282	7132125	1614874","2519489,+,5202056,0,0,0,5240492,3511181,\\,3367084,4688584,1797485,8139282,7132125,1614874,<EOF>",148))
    def test_integer12(self):
        self.assertTrue(TestLexer.checkLexeme("c0001 = e000012\\0O12412 + 0xfF912 || x0AF1221","c0001,=,e000012,\\,0O12412,+,0,xfF912,||,x0AF1221,<EOF>",149))

    def test_float1(self):
        self.assertTrue(TestLexer.checkLexeme("12.0e309121","12.0e309121,<EOF>",150))
    def test_float2(self):
        self.assertTrue(TestLexer.checkLexeme("11212e3099","11212e3099,<EOF>",151))
    def test_float3(self):
        self.assertTrue(TestLexer.checkLexeme("9876.e5","9876.e5,<EOF>",152))
    def test_float4(self):
        self.assertTrue(TestLexer.checkLexeme("1269.0e4", "1269.0e4,<EOF>",153))
    def test_float5(self):
        self.assertTrue(TestLexer.checkLexeme("12345.","12345.,<EOF>",154))
    def test_float6(self):
        self.assertTrue(TestLexer.checkLexeme("120000e-1","120000e-1,<EOF>",155))
    def test_float7(self):
        self.assertTrue(TestLexer.checkLexeme("0e05 0x00.12e5 100e-10","0e05,0,x00,.,12e5,100e-10,<EOF>",156))
    def test_float8(self):
        self.assertTrue(TestLexer.checkLexeme(".e5 .5 01e2.32 50.e+9 ",".,e5,.,5,01e2,.,32,50.e+9,<EOF>",157))
    def test_float9(self):
        self.assertTrue(TestLexer.checkLexeme("-0.e21 02.e-10  121E+4 0.E09 4060E12","-,0.e21,02.e-10,121E+4,0.E09,4060E12,<EOF>",158))
    def test_float11(self):
        self.assertTrue(TestLexer.checkLexeme("12.E-1 0.E+9 12E2e-2 0e0 0E+0 0E-0","12.E-1,0.E+9,12E2,e,-,2,0e0,0E+0,0E-0,<EOF>",159))
    def test_float12(self):
        self.assertTrue(TestLexer.checkLexeme("0.0E-12 -9.0E12 212E-292+921E2","0.0E-12,-,9.0E12,212E-292,+,921E2,<EOF>",160))
    def test_float13(self):
        self.assertTrue(TestLexer.checkLexeme("144.400e55 126.711561 101.e395564 25.154157 200.83e841 205.313014","144.400e55,126.711561,101.e395564,25.154157,200.83e841,205.313014,<EOF>",161))

    def test_boolean1(self):
        self.assertTrue(TestLexer.checkLexeme("a == True || False","a,==,True,||,False,<EOF>",162))   
    def test_boolean2(self):
        self.assertTrue(TestLexer.checkLexeme("TrueFalseTrueTrueFalseFalseTrueFalse","True,False,True,True,False,False,True,False,<EOF>",163))

    def test_string1(self):
        self.assertTrue(TestLexer.checkLexeme(""" "This is a string containing tab \\t" ""","""This is a string containing tab \\t,<EOF>""",164))
    def test_string2(self):
        self.assertTrue(TestLexer.checkLexeme(""" "He asked me: '"Where is John?'"" ""","""He asked me: '"Where is John?'",<EOF>""",165))
    def test_string3(self):
        self.assertTrue(TestLexer.checkLexeme(""" "ab\\\\'"c\\n def"  ""","""ab\\\\'"c\\n def,<EOF>""",166))
    def test_string4(self):
        self.assertTrue(TestLexer.checkLexeme("""\"\"\"hello\"\"\"\"""",""",hello,,Unclosed String: """,167))
    def test_string5(self):
        self.assertTrue(TestLexer.checkLexeme(""" "'"'"ab'"c\\'"!=!!"?"  ""","""'"'"ab'"c\\',!=,!,!,?,<EOF>""",168))
    def test_string6(self):
        self.assertTrue(TestLexer.checkLexeme(""" "\\b \\f time \\r \\n \\t \\\' \\\\"  ""","""\\b \\f time \\r \\n \\t \\\' \\\\,<EOF>""",169))  
    def test_string7(self):
        self.assertTrue(TestLexer.checkLexeme(""" "~!@#$%^&*()_+{}?.,.<>|"  ""","""~!@#$%^&*()_+{}?.,.<>|,<EOF>""",170))
    def test_string8(self):
        self.assertTrue(TestLexer.checkLexeme(""" "7I66sTfdiygoAChWx81o\\n04:47:43 UTC"  ""","""7I66sTfdiygoAChWx81o\\n04:47:43 UTC,<EOF>""",171))
    def test_string9(self):
        self.assertTrue(TestLexer.checkLexeme(""" "G17>TY/??PNB/48PBx@fR/e0z Var: x=foo(2)"  ""","""G17>TY/??PNB/48PBx@fR/e0z Var: x=foo(2),<EOF>""",172))
    def test_string10(self):
        self.assertTrue(TestLexer.checkLexeme(""" "https://www.facebook.com/cal=a[2]*3+9/.ar[1][12]"  ""","""https://www.facebook.com/cal=a[2]*3+9/.ar[1][12],<EOF>""",173))
    def test_string11(self):
        self.assertTrue(TestLexer.checkLexeme(""" "**this is a single-line comment**" ""","""**this is a single-line comment**,<EOF>""",174))
    def test_string12(self):
        self.assertTrue(TestLexer.checkLexeme(""" "{string, 12, 12412}, 01292.0e0000}" ""","""{string, 12, 12412}, 01292.0e0000},<EOF>""",175))
    def test_string13(self):
        self.assertTrue(TestLexer.checkLexeme(""" "C6!2xR0X Q/S" "HA%s#sNa^Bj&" "LastName varchar(255)" ""","""C6!2xR0X Q/S,HA%s#sNa^Bj&,LastName varchar(255),<EOF>""",176))
    def test_string14(self):
        self.assertTrue(TestLexer.checkLexeme(""" "Lexical Structure" "copyright\'\"2007-2014'"-'"Dai hoc\'\" \'\"Bach Khoa\'\" Tp.HCM" ""","""Lexical Structure,copyright'"2007-2014'"-'"Dai hoc'" '"Bach Khoa'" Tp.HCM,<EOF>""",177))

    def test_illegal_escape1(self):
        self.assertTrue(TestLexer.checkLexeme(""" "abc\\h def"  ""","""Illegal Escape In String: abc\\h""",178))
    def test_illegal_escape2(self):
        self.assertTrue(TestLexer.checkLexeme(""" "abc\\"  ""","""Illegal Escape In String: abc\\\"""",179))
    def test_illegal_escape3(self):
        self.assertTrue(TestLexer.checkLexeme(""" "thisIs\'aString"  ""","""Illegal Escape In String: thisIs\'a""",180))
    def test_illegal_escape4(self):
        self.assertTrue(TestLexer.checkLexeme(""" "!@!#$%%\\^qwqerty"  ""","""Illegal Escape In String: !@!#$%%\\^""",181))
    def test_illegal_escape5(self):
        self.assertTrue(TestLexer.checkLexeme(""" \"^HX7 v/Eu!dK\" \"!nKgOt4Ilpnm\\$\" "AFC7c&b/0tK#" ""","""^HX7 v/Eu!dK,Illegal Escape In String: !nKgOt4Ilpnm\\$""",182))
    def test_illegal_escape6(self):
        self.assertTrue(TestLexer.checkLexeme(""" "D:\\Works_HK5_PPL_assignment1_src\test\testcases" ""","""Illegal Escape In String: D:\W""",183))
    def test_illegal_escape7(self):
        self.assertTrue(TestLexer.checkLexeme(""" "#justatee\\#tlinh\\#mck\\#lien" "#LOST #Obito #DefJamRecordingsVietNam" ""","""Illegal Escape In String: #justatee\\#""",184))
    
    def test_unterminated_string1(self):
        self.assertTrue(TestLexer.checkLexeme(""" "abc def  ""","""Unclosed String: abc def  """,185))
    def test_unterminated_string2(self):
        self.assertTrue(TestLexer.checkLexeme(""" "abc@?~12"thisIs"x ""","""abc@?~12,thisIs,Unclosed String: x """,186))
    def test_unterminated_string3(self):
        self.assertTrue(TestLexer.checkLexeme(""" "dna def\nZSEQWQSA" ""","""Unclosed String: dna def\n""",187))
    def test_unterminated_string4(self):
        self.assertTrue(TestLexer.checkLexeme(""" "~!#\\b\\f@#Tstring'\"""","""Unclosed String: ~!#\\b\\f@#Tstring'\"""",188))
    def test_unterminated_string5(self):
        self.assertTrue(TestLexer.checkLexeme(""" \"an.sytung@hcmut.edu.vn\"\\n \"October\" \\f \"2020""","""an.sytung@hcmut.edu.vn,\,n,October,\,f,Unclosed String: 2020""",189))
    def test_unterminated_string6(self):
        self.assertTrue(TestLexer.checkLexeme(""" "Top_trending_gggg124!@\\n" "value '"non-zero'"" "Sunday, 10 October 2048, 7:21:21'PM" "" "" ""","""Top_trending_gggg124!@\\n,value '"non-zero'",Illegal Escape In String: Sunday, 10 October 2048, 7:21:21'P""",190))
    
    def test_unterminated_comment1(self):
        self.assertTrue(TestLexer.checkLexeme("""**{21.e-1, {23e2}, {{12.e+2, 0e8}},2*3-1*""","""Unterminated Comment""",191))
    def test_unterminated_comment2(self):
        self.assertTrue(TestLexer.checkLexeme("""**"skip'"Ne"****@@@@@!@!@@!134112""","""Unterminated Comment""",192))
    def test_unterminated_comment3(self):
        self.assertTrue(TestLexer.checkLexeme("""**x*3+2*.2.Var: ASCII-FF""","""Unterminated Comment""",193))

    def test_array1(self):
        self.assertTrue(TestLexer.checkLexeme("""{1, 5, 7, 12}""","""{,1,,,5,,,7,,,12,},<EOF>""",194))
    # def test_array2(self):
    #     self.assertTrue(TestLexer.checkLexeme("""{{1, 2}, {4, 5}, {3, 5}}""","""{{1, 2}, {4, 5}, {3, 5}},<EOF>""",129))
    # def test_array3(self):
    #     self.assertTrue(TestLexer.checkLexeme("""{{1, 2}, {4, 5}, {3, 5}}""","""{{1, 2}, {4, 5}, {3, 5}},<EOF>""",129))
    # def test_array4(self):
    #     self.assertTrue(TestLexer.checkLexeme("""{"abc","def","ghj"}""","""{"abc","def","ghj"},<EOF>""",129))
    # def test_array5(self):
    #     self.assertTrue(TestLexer.checkLexeme("""{{"kitucc", "dyonla", "hjhj"}, "$~#?hcyaknc!@@!!$", {"tneghj"}}""","""{{"kitucc", "dyonla", "hjhj"}, "$~#?hcyaknc!@@!!$", {"tneghj"}},<EOF>""",129))
    # def test_array6(self):
    #     self.assertTrue(TestLexer.checkLexeme("""{0.2, 12., 5.e2, 9E-2, 100E+1, 25.E-1}""","""{0.2, 12., 5.e2, 9E-2, 100E+1, 25.E-1},<EOF>""",128))
    # def test_array7(self):
    #     self.assertTrue(TestLexer.checkLexeme("""{21.e-1, {23e2}, {{12.e+2, 0e8}}, {8.23, 2.}}""","""{21.e-1, {23e2}, {{12.e+2, 0e8}}, {8.23, 2.}},<EOF>""",128))
    # def test_array8(self):
    #     self.assertTrue(TestLexer.checkLexeme("""{212, {23e2}, {{12.e+2, 0e8}}, {8.23, 2.}}""","""{21.e-1, {23e2}, {{12.e+2, 0e8}}, {8.23, 2.}},<EOF>""",128))
    
    def test_wrong_token1(self):
        self.assertTrue(TestLexer.checkLexeme("ab?svn","ab,Error Token ?",195))
    def test_wrong_token2(self):
        self.assertTrue(TestLexer.checkLexeme("x+2.@@^!@!&*","x,+,2.,Error Token @",196))
    def test_wrong_token3(self):
        self.assertTrue(TestLexer.checkLexeme("abcd\nef\nhihiVx%%^&&","abcd,ef,hihiVx,%,%,Error Token ^",197))
    def test_wrong_token4(self):
        self.assertTrue(TestLexer.checkLexeme("()<=()!!!~?????>?!~","(,),<=,(,),!,!,!,Error Token ~",198))

    def test_full1(self):
        self.assertTrue(TestLexer.checkLexeme("""Var: abc = 12*.2e5 - 0xEF12, st = "@gmail\\ndotcom", bo = (True || x>.5. && y <=.2.); **var here** \\. 91.012e2""","""Var,:,abc,=,12,*.,2e5,-,0xEF12,,,st,=,@gmail\\ndotcom,,,bo,=,(,True,||,x,>.,5.,&&,y,<=.,2.,),;,\.,91.012e2,<EOF>""",199))
    def test_full2(self):
        self.assertTrue(TestLexer.checkLexeme("""For (i = 0, i < n, i=i+1) Do x="'"shi'"show" r=2*.3 == 6 EndFor.""","""For,(,i,=,0,,,i,<,n,,,i,=,i,+,1,),Do,x,=,'"shi'"show,r,=,2,*.,3,==,6,EndFor,.,<EOF>""",200))