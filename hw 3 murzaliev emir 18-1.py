def num(a, b):
    if a == 0:
        return b
    else:
        return num(b % a, a)


class Fraction:
    def init(self, numertor, denumerator):
        hcf1 = num(numertor, denumerator)
        self.numertor = numertor // hcf1
        self.denumerator = denumerator // hcf1

    def str(self):
        if self.denumerator == 1:
            return str(self.numertor)


        elif self.numertor > self.denumerator:
            return str(self.numertor // self.denumerator) + " " + \
                   str(Fraction(self.numertor % self.denumerator, self.denumerator))

        else:
            return str(self.numertor) + "/" + str(self.denumerator)

    def add(self, other):
        new_numertor = self.numertor * other.denumerator + other.numertor * self.denumerator
        new_denumerator = self.denumerator * other.denumerator
        return Fraction(new_numertor, new_denumerator)

    def sub(self, other):
        new_numertor = self.numertor * other.denumerator - other.numertor * self.denumerator
        new_denumerator = self.denumerator * other.denumerator
        return Fraction(new_numertor, new_denumerator)

    def mul(self, other):
        new_numertor = self.numertor * other.numertor
        new_denumerator = self.denumerator * other.denumerator
        return Fraction(new_numertor, new_denumerator)

    def floordiv(self, other):
        new_num = self.numertor // other.denumerator
        new_den = self.denumerator // other.denumerator
        return Fraction(new_num, new_den)


a = Fraction(4, 5)
b = Fraction(4, 5)
print(a + b)
print(a - b)
print(a * b)
print(a // b)