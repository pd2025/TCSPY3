class Point:
    """ Point class represents and manipulates x,y coords. """

    def __init__(self, x=0, y=0):
        """ Create a new point at x, y """
        self.x = x
        self.y = y

    def distance_from_origin(self):
        """ Compute my distance from the origin """
        return ((self.x ** 2) + (self.y ** 2)) ** 0.5

    def __str__(self):  # All we have done is renamed the method
        return "({0}, {1})".format(self.x, self.y)

    def halfway(self, target):
        """ Return the halfway point between myself and the target """
        mx = (self.x + target.x) / 2
        my = (self.y + target.y) / 2
        return Point(mx, my)

    def reflect_x(self):
        return self.x, -self.y

    def slope_from_origin(self):
        return self.y / self.x

    def get_line_to(self, target):
        slope = (target.y - self.y) / (target.x - self.x)
        intercept = self.y - (slope * self.x)
        return slope, intercept

    def distance(self, b):
        dx = b.x - self.x
        dy = b.y - self.y
        dsquared = dx * dx + dy * dy
        result = dsquared ** 0.5
        return result


class Rectangle:
    """ A class to manufacture rectangle objects """

    def __init__(self, posn, w, h):
        """ Initialize rectangle at posn, with width w, height h """
        self.corner = posn
        self.width = w
        self.height = h

    def __str__(self):
        return "({0}, {1}, {2})".format(self.corner, self.width, self.height)

    def grow(self, delta_width, delta_height):
        """ Grow (or shrink) this object by the deltas """
        self.width += delta_width
        self.height += delta_height

    def move(self, dx, dy):
        """ Move this object by the deltas """
        self.corner.x += dx
        self.corner.y += dy

    def area(self):
        return self.width * self.height

    def perimeter(self):
        return self.width * 2 + self.height * 2

    def flip(self):
        self.width, self.height = self.height, self.width

    def contains(self, point):
        if self.corner.x + self.width > point.x >= self.corner.x:
            if self.corner.y + self.height > point.y >= self.corner.y:
                return True
        return False

    def collide(self, other_rectangle):
        if self.corner.x < other_rectangle.corner.x < self.corner.x + self.width:
            if self.corner.y < other_rectangle.corner.y < self.corner.y + self.height:
                return True
        # elif self.corner.x < other_rectangle.corner.x < self.corner.x + self.width:
        #     if self.corner.y + self.corner.height < self.corner.x and > self.corner.x + width:
        #


# box = Rectangle(Point(0, 0), 100, 200)
# bomb = Rectangle(Point(100, 80), 5, 10)  # In my video game
# print("box: ", box)
# print("bomb: ", bomb)
# r = Rectangle(Point(100, 50), 10, 5)
# print(r.width == 10 and r.height == 5)
# r.flip()
# print(r.width == 5 and r.height == 10)
r = Rectangle(Point(0, 0), 5, 10)
# print(r.contains(Point(0, 0)))
# print(r.contains(Point(3, 3)))
# print(not r.contains(Point(3, 7)))
# print(not r.contains(Point(3, 5)))
# print(r.contains(Point(3, 4.99999)))
# print(not r.contains(Point(-3, -3)))
a = Point(4, 5)
print(r.contains(a))
