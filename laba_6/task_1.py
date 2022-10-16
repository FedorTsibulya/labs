class Complex:
    # z = x+yi
    def __init__(self, x, y):
        self.x = x
        self.y = y


    @classmethod
    def z_str(cls, string_input):
        string_input = string_input.replace('i', '')
        if '+' in string_input:
            string_input = string_input.split('+')
        elif '-' in string_input:
            string_input = string_input.split('-')
        return cls(float(string_input[0]), float(string_input[1]))


    def __str__(self):
        if self.y < 0:
            return '{}-{}i'.format(self.x, abs(self.y))
        return '{}+{}i'.format(self.x, self.y)



    def __add__(self, other):
        return Complex(self.x + other.x, self.y + other.y)

    def __sub__(self, other):
        return Complex(self.x - other.x, self.y - other.y)

    def __mul__(self, other):
        return Complex(self.x * other.x - self.y * other.y, self.x * other.y + self.y * other.x)

    def __truediv__(self, other):
        return Complex((self.x * other.x + self.y * other.y) / (other.y**2 + other.x**2),
                       (self.x * other.y + self.y * other.x) / (other.y**2 + other.x**2))

    def __abs__(self):
        return (self.y**2 + self.x**2)**0.5


