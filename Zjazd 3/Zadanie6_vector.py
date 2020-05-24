

class Vector:

    def __init__(self,x =1,y=2):
        self.x = x
        self.y = y

    def __str__(self):
        return"[{}, {}]".format(self.x, self.y)
    def __add__ (self,other):
        return Vector(self.x + other.x,self.y + other.y)
    def __mul__(self,other):
        return self.x * other.x + self.y * other.y




x = Vector(1, 2)
y = Vector(1, 2)

print(x+y)
print(x*y)



class TestVector:
    def test_init(self):
        vector = Vector(1, 2)
        assert vector.x == 1
        assert vector.y == 2
    def test_add_two_vectors(self):
        v1 = Vector(1, 2)
        v2 = Vector(3, 4)
        v3 = v1 + v2
        assert v3.x == 4
        assert v3.y == 6
    def test_mul_two(self):
        v1 = Vector(1, 2)
        v2 = Vector(3, 4)
        v3 = v1 * v2
        assert v3.x == 1 * 3 + 2 * 4
    def test_mul_vector_int(self):
        v1 = Vector(3,4)
        v2 = v1 + 3
        assert v2.x == 9
        assert v2.y == 12