import math
class Circle:
    def __init__(self,a,b,r):
        self.a = a
        self.b = b
        self.r = r

    def Area(self):
        return 3.14* self.r * self.r

    def Perimeter(self):
        return 2*3.14*self.r

    def testBelongs(self, x, y):
        a = x - self.a
        b = y - self.b

        c = math.sqrt(a*a + b*b)
        if c <= self.r:
            return True
        else:
            return False

cir = Circle(1,2,1)
print(cir.Area())
print(cir.testBelongs(1,1))
