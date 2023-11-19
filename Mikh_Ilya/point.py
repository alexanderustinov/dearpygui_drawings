from math import cos, sin, pi

class Point:
    
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def sum(self, p2):
        self.x = self.x + p2.x
        self.y = self.y + p2.y
        return self
    
    def turn(self, fi):
        old_x = self.x
        old_y = self.y
        self.x = old_x * round(cos(fi * pi / 180), 14) - old_y * round(sin(fi * pi / 180), 14)
        self.y = old_x * round(sin(fi * pi / 180), 14) + old_y * round(cos(fi * pi / 180), 14)
        return self

    def __str__(self):
        return '(' + str(self.x) + ', ' + str(self.y) + ')'
    
    def toTuple(self):
        return(self.x, self.y)