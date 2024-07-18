import math

class Fraction:
    def __init__(self, n, d):
        self.numerator = n
        self.denominator = d

    def add(self, f):
        lcm = math.lcm(self.denominator, f.denominator)
        num = (lcm / self.denominator) * self.numerator + (lcm / f.denominator) * f.numerator 
        self.numerator = num
        self.denominator = lcm

    def __add__(self, f):
        lcm = math.lcm(self.denominator, f.denominator)
        num = (lcm / self.denominator) * self.numerator + (lcm / f.denominator) * f.numerator 
        return Fraction(int(num), lcm)

    def __str__(self):
        return f"{self.numerator}/{self.denominator}"
    
    def __eq__(self, f):
        g = math.gcd(self.numerator, self.denominator)
        n1 = self.numerator // g
        d1  = self.denominator // g

        g = math.gcd(f.numerator, f.denominator)
        n2 = f.numerator // g
        d2  = f.denominator // g

        return n1 == n2 and d1 == d2

    def __ne__(self, f):
        return not self.__eq__(f)

    def __gt__(self, f):
        return (self.numerator * f.denominator) > (f.numerator * self.denominator)

    def __lt__(self, f):
        return (self.numerator * f.denominator) < (f.numerator * self.denominator)
    
f1 = Fraction(1, 2)
f2 = Fraction(1, 5)

result = f1 + f2
print(result)
print(result.numerator, result.denominator)

f1 = Fraction(1, 5)
f2 = Fraction(2, 10)

print(f1 == f2)
print(f1 != f2)
print(f1 > f2)
print(f1 < f2)
