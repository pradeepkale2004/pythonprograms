import math
class Coordinates:
    def __init__(self, x,y):
        self.x_axis = x
        self.y_axis = y

    def __str__(self):
        return f'<{self.x_axis},{self.y_axis}>'

    def euclidean_distance(self, other):
        diff = (other.x_axis - self.x_axis)**2 + (other.y_axis - self.y_axis)**2
        distance = math.sqrt(diff)
        return distance

    def distance_from_origin(self):
        distance = ((self.x_axis ** 2) + (self.y_axis ** 2)) ** 0.5
        return distance

class Line:
    def __init__(self,a,b,c):
        self.a = a
        self.b = b
        self.c = c

    def __str__(self):
        return f'{self.a}x + {self.b}y + {self.c} = 0'

    def point_on_line(line, point):
        if line.a* point.x_axis + line.b*point.y_axis + line.c == 0:
            return 'point lies on line'
        else:
            return 'Point does not lies on line'


c1 = Coordinates(4,5)
c2 = Coordinates(2,3)
print(c1)
print(c2)
print(c1.euclidean_distance(c2))
print(f'Distance from center is {c1.distance_from_origin()}')

l1 = Line(3,3,3)
p1 = Coordinates(1,1)
print(l1)
print(l1.point_on_line(p1))
