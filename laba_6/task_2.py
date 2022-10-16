class Vector():
    def __init__(self, x = 0, y = 0, z = 0):
        self.x = x
        self.y = y
        self.z = z


    @classmethod
    def string(cls, str):
        x, y, z = [int(i) for i in str.split(',')]
        return cls(x, y, z)

    def __str__(self):
        return "Vector ({}; {}; {})".format(self.x, self.y, self.z)


    def __add__(self, other):
        return Vector(self.x + other.x, self.y + other.y, self.z + other.z)

    def __sub__(self, other):
        return Vector(self.x - other.x, self.y - other.y, self.z - other.z)

    def __mul__(self, other):
        return (self.x * other.x + self.y * other.y + self.z * other.z)

    def __abs__(self):
        return (self.x**2 + self.y**2 + self.z**2)**0.5

    def dev_by_num(self, num):
        return (self.x / num, self.y / num, self.z / num)

    def mixed_mul(self, other_2, other_3):
        return (self.x * other_2.y * other_3.z -
                self.x * other_2.z * other_3.y -
                self.y * other_2.x * other_3.z +
                self.y * other_2.z * other_3.x +
                self.z * other_2.x * other_3.y -
                self.z * other_2.y * other_3.x)


    @staticmethod
    def distance():
        N = int(input())
        max_dist = 0
        dist = Vector(0, 0, 0)
        cords = Vector(0, 0, 0)

        for _ in range(N):
            point = Vector.string(input())
            dist = abs(point)
            if dist > max_dist:
                max_dist = dist
                cords = point
        print(cords, max_dist)

    @staticmethod
    def centre_mass():
        N = int(input())
        max_dist = 0
        dist = Vector(0, 0, 0)
        sum_cords = Vector(0, 0, 0)

        for _ in range(N):
            point = Vector.string(input())
            dist = abs(point)
            sum_cords += point
        print(sum_cords.dev_by_num(N))

    @staticmethod
    def square_parallelogram():
        vect_1 = Vector.string(input())
        vect_2 = Vector.string(input())
        square = ((abs(vect_1)*abs(vect_2))**2 - (vect_1*vect_2)**2)**0.5
        print(abs(square))

    @staticmethod
    def volume_3d_parall():
        vect_1 = Vector.string(input())
        vect_2 = Vector.string(input())
        vect_3 = Vector.string(input())
        volume = vect_1.mixed_mul(vect_2, vect_3)
        print(abs(volume))
