import unittest
from TestUtils import TestParser

class ParserSuite(unittest.TestCase):
    def test_var_declare1(self):
        input = """Var: a = 5;"""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,201))

    def test_var_declare2(self):
        input = """Var: b[2][3] = {{2,3,4},{4,5,6}};"""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,202))

    def test_var_declare3(self):
        input = """Var: c, d = 6, e, f;"""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,203))

    def test_var_declare4(self):
        input = """Var: m, n[10];"""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,204))

    def test_var_declare5(self):
        input = """Var: s="happyBirthDay";"""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,205))

    def test_var_declare6(self):
        input = """Var: s_1="'"superMan is'".", s_2="happyBirthDay";"""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,206))

    def test_var_declare7(self):
        input = """Var: arr[10], c[99][3][2], arr2[];
                """
        expect = "Error on line 1 col 32: ]"
        self.assertTrue(TestParser.checkParser(input,expect,207))

    def test_var_declare8(self):
        input = """Var: s="DaiH0cB4ckHo4", x= 12.2e54, c=0xF212;
                """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,208))
    
    def test_var_declare9(self):
        input = """Var: arr[2][3][5] = {{"string", "s!@#$"}, {{542.10e21, 2., 9e5}}, {{1023, 1024, 2098}, {0x2141, 0xF912}}};
                """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,209))
    def test_var_declare10(self):
        input = """Var: arr = {1,2}, a[10][22], e=40e5, c, d f=20;
                """
        expect = "Error on line 1 col 42: f"
        self.assertTrue(TestParser.checkParser(input,expect,210))
    
    def test_function_declare1(self):
        input = """
        Function: test
        Parameter: n
        Body: 
            n = n+1;
        EndBody.
        """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,211))    

    def test_function_declare2(self):
        input = """
        Function: test 
        Body:
            Var: arr[2][3] = {"Hi",{"it-desert-theme='"false'""},{"it-player-ads","OK","404"}}; 
            e =  10e2;
        EndBody.
        """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,212))
    
    def test_function_declare3(self):
        input = """
        Function: test 
        Body:
            Var: x = 10, a[10]; 
            x = x + 1;
        EndBody.
        """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,213))

    def test_function_declare4(self):
        input = """
        Function: test 
        Body:
        EndBody.
        """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,214))

    def test_function_declare5(self):
        input = """
        Function:  
        Body:
            Var s = "hi_hi";
            s = "nice";
        EndBody.
        """
        expect = "Error on line 3 col 8: Body"
        self.assertTrue(TestParser.checkParser(input,expect,215))

    def test_function_declare6(self):
        input = """
        Function:  test
        Parameter: Var x = 2;
        Body:
            x = (x - 1)\\2;
        EndBody.
        """
        expect = "Error on line 3 col 19: Var"
        self.assertTrue(TestParser.checkParser(input,expect,216))

    def test_function_declare6(self):
        input = """
        Function:  test
        Var x[2][3] = {1, {2, 4}, {"5"}, 7.};
        Parameter: n, c
        Body:
            Var h = a*b;
        EndBody.
        """
        expect = "Error on line 3 col 8: Var"
        self.assertTrue(TestParser.checkParser(input,expect,217))

    def test_function_declare7(self):
        input = """
        Function:  test___1
        Parameter: n = 2, c, d
        Body:
            Var: c = 5;
            
        EndBody.
        """
        expect = "Error on line 3 col 21: ="
        self.assertTrue(TestParser.checkParser(input,expect,218))
    
    def test_function_declare8(self):
        input = """
        Function: foo
        Parameter: a[5], b
        Body:
            Var: i = 0;
            Return 1;
        EndBody.
        """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,219))
    
    def test_function_declare9(self):
        input = """
        Function: foo
        Parameter:
        Body:
        EndBody.
        """
        expect = "Error on line 4 col 8: Body"
        self.assertTrue(TestParser.checkParser(input,expect,220))

    def test_function_declare10(self):
        input = """
        Function: test___
        Parameter: x[10], a[2][3][2][9]
        Body:
            Return test___(12.,{2,{{2.e5},"hi"},4.});
        EndBody.
        """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,221))

    def test_simple_program1(self):
        input = """
        Var: x;
        Function: main
        Body:
        x = 10;
        fact (x);
        EndBody.
        """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,222))
    
    def test_simple_program2(self):
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
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,223))

    def test_simple_program3(self):
        input = """
        Var: atn_2 = 2.e65;
        Var: a[10], b[10][2], c[10];
        Function: main
        Body:
        atn_2 = 1 + 2;
        c[9] = a[9] + b[9][1];
        EndBody.
        """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,224))
    
    def test_simple_program4(self):
        input = """
        Var: simp_l_3;
        Function: test
        Parameter: a, b
        Body:
            print(a);
            print(b);
        EndBody.
        """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,225))

    def test_simple_program5(self):
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
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,226))

    def test_simple_program6(self):
        input = """
        Var: a__Rr1[2][2] = {{0.9e2,10.e4},{22,212}};
        Function: test
        Parameter: c[1]
        Body:
            c[0] = 1-1;
            Return 2;
        EndBody
        """
        expect = "Error on line 9 col 8: <EOF>"
        self.assertTrue(TestParser.checkParser(input,expect,227))

    def test_simple_program7(self):
        input = """
        Var: a;
        Function: test
        Parameter a, c
        Body:
        EndBody.
        """
        expect = "Error on line 4 col 18: a"
        self.assertTrue(TestParser.checkParser(input,expect,228))
    
    def test_simple_program8(self):
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
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,229))

    def test_simple_program9(self):
        input = """
        Var: s;
        Function: foo
        Parameter: s
        Body:
            s = "hi_1";
            Return foo("hi");
        EndBody.
        """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,230))
    
    def test_simple_program10(self):
        input = """
        Function: hello
        Parameter: str
        Body:
            Var: x = 2;
            hello(str);
            hello(x);
        EndBody.
        """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,231))

    def test_var_declare_statement1(self):
        input = """
        Function: test
        Body:
            Var: x, y__, z23, t_12;
        EndBody.
        """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,232))

    def test_var_declare_statement2(self):
        input = """
        Var: a;
        Function: test
        Body:
            Var: a_ = 10., b = 5., c3 = 9;
        EndBody.
        """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,233))
    
    def test_var_declare_statement3(self):
        input = """
        Var: a;
        Function: test
        Body:
            Var: z_1[2][3] = {{6572e21, 2341e+56, 0.5},{"%^DFGZ", "Rvul^%", "sin2xy"}}, a[24], c;
        EndBody.
        """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,234))

    def test_var_declare_statement4(self):
        input = """
        Function: test
        Body:
            Var: x = y = z;
            Var: c = 2;
        EndBody.
        """
        expect = "Error on line 4 col 23: ="
        self.assertTrue(TestParser.checkParser(input,expect,235))

    def test_var_declare_statement5(self):
        input = """
        Function: test
        Body:
            Var: x = 43.9e10, y = 542, z = 0xFF2, t = 0O221, s="ThisIsString", w = False, arr[2][1] = {{2e5},{2}}; 
        EndBody.
        """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,236))
    def test_assignment_statement1(self):
        input = """
        Var: a;
        Function: test
        Body:
            Var: r = 10., v;
            v = (4. \. 3.) *. 3.14 *. r *. r *. r;
        EndBody.
        """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,237))

    def test_assignment_statement2(self):
        input = """
        Function: test
        Body:
            Var: a[100], x[3][4];
            a[3 + foo(2)] = a[b[2][3]] + 4;
            x = {{{12,1}, {12., 12e3}},{23}, {13,32}};
        EndBody.
        """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,238))
    
    def test_assignment_statement3(self):
        input = """
        Function: test
        Body:
            Var: r = 2, c = 9;
            r = r + c = 9 - r;
            Return True;
        EndBody.
        """
        expect = "Error on line 5 col 22: ="
        self.assertTrue(TestParser.checkParser(input,expect,239))

    def test_assignment_statement4(self):
        input = """
        Function: test
        Body:
            Var: r, d, t;
            r = 3.14;
            s = r*r + 2;
            t = s && !foo(2) || r =/= 9. && (2+3)*.5.;
            t = t \\. 3.;
            Return True;
        EndBody.
        """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,240))
    
    def test_assignment_statement5(self):
        input = """
        Var: x, y = 5e3, z;
        Function: test
        Body:
            z = (x*x*x*x*x*x*x)\\.(2.*.y -. 2.3e12 + 23\\11 + 12%2) - test();
            x = x -. 10.;
            If x >=. 1. Then
                Return z;
            EndIf.
        EndBody.
        """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,241))

    def test_assignment_statement6(self):
        input = """
        Function: test
        Body:
            Var: r = 3.14, t;
            r = r*r == (2*3);
            t =  True;
            t = !t == !(r && False || 2-2); 
        EndBody.
        """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,242))

    def test_assignment_statement7(self):
        input = """
        Var: s = 0;
        Function: test
        Parameter: count
        Body:
            s = s + 3 - 15 \.-.2.;
            t = 2.e5 <=. 2.5 || (0xF21 >= 0XFF) && (0o124 < 0O171);
        EndBody.
        """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,243))

    def test_assignment_statement8(self):
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
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,244))
    def test_assignment_statement9(self):
        input = """
        Function: test
        Body:
            Var: a=1, b=2, c=3, d[2]={2e-1, 9e5}, z;
            b = d[1] - a;
            c = d[0] - c;
            a = b *. c;
            z =  a*a + b*b + c*c - 3\\a*a*b -  4*a\\.b - 5*c*c*.c + 1*1*1;
        EndBody.
        """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,245))

    def test_assignment_statement10(self):
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
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,246))

    def test_if_statement1(self):
        input = """
        Function: test
        Body:
            Var: x;
            If 2<=3 Then x = 3;
            EndIf.
        EndBody.
        """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,247))

    def test_if_statement2(self):
        input = """
        Function: test
        Body:
            Var: athos = 500, pothos = 900, jerry, tom = 200;
            If (pothos - athos) < 400 Then jerry = pothos - tom;
            Else jerry = athos - tom;
            EndIf.
        EndBody.
        """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,248))

    def test_if_statement3(self):
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
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,249))
    
    def test_if_statement4(self):
        input = """
        Function: test
        Body:
            Var: math=10, literature=6, english=8, avg, raise;
            avg = (math + literature + english)\\3;
            If avg < 3 Then raise = "Hoc lai";
            ElseIf avg < 4 Then raise = "Yeu";
            ElseIf avg <. 6.5 Then raise = "TB";
            ElseIf avg <. 8. Then raise = "Kha";
            ElseIf avg <. 9. Then raise =  "Gioi";
            Else raise = "Xuat sac";
            EndIf.
        EndBody.
        """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,250))

    def test_if_statement5(self):
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
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,251))
    
    def test_if_statement6(self):
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
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,252))

    def test_if_statement7(self):
        input = """
        Function: test
        Body:
            Var: arr[2] = {2,4}, x = 4.5, y = 5.;
            If arr[1] >. x Then arr[1] = y;
            ElseIf Return 2;
            EndIf
        EndBody.
        """
        expect = "Error on line 6 col 19: Return"
        self.assertTrue(TestParser.checkParser(input,expect,253))
  
    def test_if_statement8(self):
        input = """
        Function: test
        Body:
            Var: abc = 1, cde = 2, efg = 3;
            If abc + cde == efg Then Else efg = 3;
            EndIf.
        EndBody.
        """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,254))
    
    def test_if_statement9(self):
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
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,255))

    def test_if_statement10(self):
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
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,256))

    def test_for_statement1(self):
        input = """
        Function: test
        Body:   
            For (i = 0, i < 10, 2) Do
                writeln(i);
            EndFor.
        EndBody.
        """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,257))

    def test_for_statement2(self):
        input = """
        Function: test
        Parameter: n
        Body:
            Var: x;   
            For (i = 0, i < sqrt(n)*2, 1) Do
                x = i + n;
                writeln(x\\2);
            EndFor.
        EndBody.
        """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,258))
    
    def test_for_statement3(self):
        input = """
        Function: test
        Body:   
            For (i = 0, i <= 1000\\10, 1) Do
                If i%2 == 0 Then writeln(i\\2);
                EndIf.
            EndFor.
        EndBody.
        """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,259))

    def test_for_statement4(self):
        input = """
        Function: test
        Parameter: n
        Body:
            Var: i = 0;
            For (i, i <= n*n - 2*n + 1, 1) Do
                print(i + i + i);
            EndFor.
        EndBody.
        """
        expect = "Error on line 6 col 18: ,"
        self.assertTrue(TestParser.checkParser(input,expect,260))

    def test_for_statement5(self):
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
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,261))

    def test_for_statement6(self):
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
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,262))

    def test_for_statement7(self):
        input = """
        Function: test
        Body:
            For (i = 0, True, 1) Do
            EndFor.
        EndBody.
        """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,263))

    def test_for_statement8(self):
        input = """
        Function: test
        Body:
            Var: a = 2;
            For (i = 10 - a*a\\2, a < 100, a = a + 1) Do
                writeln(a*a - i*i);
                i = i + 1;
            EndFor.
        EndBody.
        """
        expect = "Error on line 5 col 44: ="
        self.assertTrue(TestParser.checkParser(input,expect,264))

    def test_while_statement1(self):
        input = """
        Function: test
        Body:
            While True Do
            EndWhile.
        EndBody.
        """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,265))

    def test_while_statement2(self):
        input = """
        Function: test
        Body:
            Var: x = 0;
            While i < 10 Do
                writeln(i);
                i = i + 1;
            EndWhile.
        EndBody.
        """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,266))

    def test_while_statement3(self):
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
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,267))

    def test_while_statement4(self):
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
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,268))

    def test_while_statement5(self):
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
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,269))

    def test_while_statement6(self):
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
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,270))

    def test_while_statement7(self):
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
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,271))

    def test_while_statement8(self):
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
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,272))

    def test_while_statement9(self):
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
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,273))

    def test_while_statement10(self):
        input = """
        Function: test
        Parameter: n
        Body:
            Var: i = 0;
            While 1 Do
                i = i + 1;
                If (i == 10) Then write("OK");
        EndBody.
            EndWhile.
        """
        expect = "Error on line 9 col 8: EndBody"
        self.assertTrue(TestParser.checkParser(input,expect,274))

    def test_do_while_statement1(self):
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
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,275))

    def test_do_while_statement2(self):
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
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,276))

    def test_do_while_statement3(self):
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
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,277))
    
    def test_do_while_statement4(self):
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
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,278))

    def test_do_while_statement5(self):
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
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,279))

    def test_do_while_statement6(self):
        input = """
        Function: test
        Body:
            Var: flag = 0;
            Do
                While !flag Do
                EndWhile
            EndDo.
        EndBody.
        """
        expect = "Error on line 8 col 12: EndDo"
        self.assertTrue(TestParser.checkParser(input,expect,280))

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
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,281))
    
    def test_break_statement1(self):
        input = """
        Function: test
        Body:   
            For (i = 0, i < 10, 2) Do
                Break;
            EndFor.
            writeln(i);
        EndBody.
        """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,282))
    
    def test_break_statement2(self):
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
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,283))

    def test_break_statement3(self):
        input = """
        Function: test
        Body:
            Var: a[2][3][4][5];
            Do 
                a[1][2][3][4] = 2.e59;
                Break;
            While True EndDo.
            writeln(a[1][2][3][4]);
        EndBody.
        """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,284))

    def test_continue_statement1(self):
        input = """
        Function: test
        Body:
            Var: x = 1;
            Do 
                Continue;
            While !x EndDo.
        EndBody.
        """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,285))

    def test_continue_statement2(self):
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
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,286))

    def test_continue_statement3(self):
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
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,287))

    def test_call_statement1(self):
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
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,288))

    def test_call_statement2(self):
        input = """
        Function: test
        Body:
            foo();
        EndBody.
        Function: foo
        Body:
        EndBody.
        """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,289))

    def test_call_statement3(self):
        input = """
        Function: test
        Body:
            foo(2) - 2 \\ 3 + 4;
        EndBody.
        Function: foo
        Parameter: n
        Body:
        EndBody.
        """
        expect = "Error on line 4 col 19: -"
        self.assertTrue(TestParser.checkParser(input,expect,290))

    def test_call_statement4(self):
        input = """
        Function: test
        Body:
            foo(True, "!@$C#hc%", 12. \\. 921.9e5 * 32e1);
            foo(3,2,1);
            foo(2021, "BKit", 2020e125);
        EndBody.
        Function: foo
        Parameter: n, c, t
        Body:
        EndBody.
        """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,291))

    def test_return_statement1(self):
        input = """
        Function: test
        Body:
            Return True;
        EndBody.
        """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,292))

    def test_return_statement2(self):
        input = """
        Function: test
        Body:
            Return 1 +. 4e25 \\. 2.;
        EndBody.
        """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,293))

    def test_return_statement3(self):
        input = """
        Function: sum
        Parameter: n
        Body:
            If (n == 0) Then Return 0;
            EndIf.
            Return n + sum(n - 1);
        EndBody.
        """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,294))

    def test_wrong_miss_close(self):
        """Miss variable"""
        input = """Var: ;"""
        expect = "Error on line 1 col 5: ;"
        self.assertTrue(TestParser.checkParser(input,expect,202))
    def test_scope_error(self):
        input = """
        Var: x;
        Function: test
        Body:
            Body:
                Body:
                    print(1);
                EndBody.
            EndBody.
        EndBody.
        """
        expect = "Error on line 5 col 12: Body"
        self.assertTrue(TestParser.checkParser(input,expect,295))

    def test_full_program1(self):
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
                        p_V[1] = a + c*t\\2 -. 9.e5 +. 2. - 2%2 \\. 2;
                        p_V[2] = c*c*c - p_V[2%2] - 19e5 *.2 -. 1. --6 + p_V[0]*99999; 
                        s = False; 
                    EndWhile.
                    s =  !s || !(s ==2) && (t >=. 5432.) && t =/= t*.2;
                    Break;
                While True EndDo.
                If i == n\\2 Then Break;
                EndIf.
            EndFor.
            Return test(n%2);
        EndBody.
        Function: main
        Body:
            test(n);
        EndBody.
        """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,296))

    def test_full_program2(self):
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
            p1 = hp1 * (1000 - d) \\. int_of_float(1000);
            p2 = (hp2 * d) \\. int_of_float(1000);
            h1 = (hp1 + hp2) % 100;
            h2 = (h1*hp2) % 100;
             
            If (hp2 == 888) Then none = True;
            EndIf.
            If hp1 == 777 && ((p1 < p2) || (h1 < h2)) && (none == False) Then
                Var: e = 1;
                d = e;
                p1 = hp1 *. (1000 - d) \\. float(1000);
                p2 = (hp2 *. d) \\. float(1000);
            EndIf.
            pR = (h1*p1 - h2 * p2) \\. (h1*p1 + h2 * p2);
            print(pR);
        EndBody.
        Function: main
        Body:
            combat(544,290,600);
        EndBody.
        """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,297))
    
    def test_full_program3(self):
        input = """
        Var: s = "ppL2020";
        Function: adventure
        Parameter: nEvents
        Body:
            For (i = 0, i < nEvents, 1) Do
                fibonacci(float_to_int(i*.25e5-.2.+(2*fibonacci(2 + 1 + i)\\.2e54)*2) + i%2);
                If i == nEvents\\5 Then Break;
                EndIf.
            EndFor.
        EndBody.
        Function: fibonacci
        Body:
            Var: n;
            If (n == 1) || (n == 2) Then
                Return 1;
            EndIf.
            Return fibonacci(n - 1) + fibonacci(n - 2);
        EndBody.
        Function: main
        Body:
            adventure(1023);
        EndBody.
        """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,298))

    def test_full_program4(self):
        input = """
        Var: c[100];
        Function: test
        Parameter: value
        Body:
            Var: count = 0;
            Var: value_ = value;
            If (value == 0) Then
                Var: c[2];
                c[0] = "0";
                c[1] = "\\n";
            Else
                While (value_ \\ 10 != 0) Do
                    count = count+1;
                    value_ = value_ \\ 10;
                EndWhile.
                For (i = count, i >= 0, -1) Do
                    c[i] = (value % 10) + 48;
                    value = value \\. 10.;
                EndFor.
                c[count+1] = "\\b";
            EndIf.
        EndBody.
        Function: main
        Body:
            test(2293);
        EndBody.
        """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,299))

    def test_full_program5(self):
        input = """
        Function: foo
        Parameter: a[5], b
        Body:
        Var: i = 0;
        While (i < 5) Do
            a[i] = b +. 1.0;
            i = i + 1;
        EndWhile.
        Return a[5];
        EndBody.
        Function: test
        Parameter: arr[21][90], b, c
        Body:
            For (i = 0 , i < arr[20][2] , 1) Do
                If foo(i) <= (foo(i+1)\\foo(foo(i))) Then
                    Return;
                ElseIf foo(i\\2) <= (foo(i+4)\\foo(foo(4*i\\2))) Then
                    Break;
                Else 
                    While !False Do
                        If (!False == True) Then print((foo(i*i+111)\\foo(foo(arr[2][1]*i\\2))));
                        Else Continue;
                        EndIf.    
                    EndWhile.
                EndIf.
            EndFor.
        EndBody.
        Function: main
        Body:
            test(2293);
        EndBody.
        """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,300))