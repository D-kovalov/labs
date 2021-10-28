class main:
    Squar="square"
    d = "diogonal"
    l="lenth circle"
    k=" "
    s="square circle"
class triangle(main):
    a="a"
    b="b"
    c="c"
    k="0.5"
    sinalpha="sin_bet_ab"
    def square(self):
        print(self.Squar+"=" +self.k+"*"+self.a+"*"+self.b +"*" +self.sinalpha)

class isosceles_triangle(triangle):
    b="a"
    def square_i(self):
        print(self.square())

class right_triangle (triangle):
            sinalpha = "1"

            def square_r(self):
                print(self.square())
class equilateral_triangle(triangle):
    b="a"
    sinalpha = "1"
    k="sin(60)"
    def square_e(self):
        print(self.square())
class rectangle(main):
    aa="a"
    bb="b"
    d="diogonal"
    def diogonal(self):
        print(self.d+"=sqrt("+self.aa+"*"+self.aa+"+"+self.bb+"*"+self.bb+ ")")
class kvadrat(rectangle):
    bb="a"
    def diogonal_k(self):
        print(self.diogonal())
class circle(main):
    r="r"
    k="2Pi"
class l_circle(circle):
    def len(self):
        print(self.l+"="+self.k+"*"+self.r)
class s_circle(circle):
    k="Pi"
    def sq(self):
        print(self.s + "=" + self.k + "*" + self.r+ "*" + self.r)

triangle = triangle()
triangle.square()
isosceles_triangle=isosceles_triangle()
isosceles_triangle.square_i()
right_triangle=right_triangle()
right_triangle.square_r()
equilateral_triangle=equilateral_triangle()
equilateral_triangle.square_e()
rectangle= rectangle()
rectangle.diogonal()
kvadrat= kvadrat()
kvadrat.diogonal_k()
l_circle=l_circle()
l_circle.len()
s_circle=s_circle()
s_circle.sq()