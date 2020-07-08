import math


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


# Other statements outside the class continue below here.


# p = Point()
# q = Point()
# print("(x={0}, y={1})".format(p.x, p.y))
#

# p = Point(4, 2)  # Instantiate an object of type Point
# q = Point(6, 3)  # Make a second point
# r = Point()  # r represent the origin
# print(p.x, q.y, r.x)


p = Point()
q = Point()
p.x = 3
p.y = 4


# print(p.x, p.y, q.x, q.y)  # Each point object has its own x and y
# distance_squared_from_origin = p.x * p.x + p.y * p.y
# print(distance_squared_from_origin)


def print_point(pt):
    print("({0}, {1})".format(pt.x, pt.y))


def midpoint(p1, p2):
    """ Return the midpoint of points p1 and p2 """
    mx = (p1.x + p2.x) / 2
    my = (p1.y + p2.y) / 2
    return Point(mx, my)


# p = Point(3, 4)
# q = Point(5, 12)
# r = p.halfway(q)
# print(r)


class SMS_store:

    def __init__(self):
        self.inbox = []
        self.has_been_viewed = False

    def add_new_arrival(self, from_number, time_arrived, text_of_SMS):
        self.has_been_viewed = False
        self.inbox.append([self.has_been_viewed, from_number, time_arrived, text_of_SMS])

    def message_count(self):
        return len(self.inbox)

    def get_unread_indexes(self):
        list_of_indexes = []
        for i in self.inbox:
            if not i[0]:
                list_of_indexes.append(self.inbox.index(i))
        return list_of_indexes

    def get_messages(self, i):
        if not self.inbox:
            return None
        else:
            self.inbox[i][0] = True
            return self.inbox[i]

    def delete(self, i):
        self.inbox.remove(self.inbox[i])

    def clear(self):
        self.inbox = []


# p = Point(4, 3)
# print(p.reflect_x())
# print(distance(Point(1, 1), Point(3, 3)))
# print(p.slope_from_origin())
# print(Point(4, 11).get_line_to(Point(6, 15)))
# my_inbox = SMS_store()
# my_inbox.add_new_arrival(from_number, time_arrived, text_of_SMS)
# Makes new SMS tuple, inserts it after other messages
# in the store. When creating this message, its
# has_been_viewed status is set False.
#
# my_inbox.message_count()
# # Returns the number of sms messages in my_inbox
#
# my_inbox.get_unread_indexes()
# # Returns list of indexes of all not-yet-viewed SMS messages
#
# my_inbox.get_message(i)
# # Return (from_number, time_arrived, text_of_sms) for message[i]
# # Also change its state to "has been viewed".
# # If there is no message at position i, return None
#
# my_inbox.delete(i)  # Delete the message at index i
# my_inbox.clear()  # Delete all messages from inbo
# p = Point(-1, 2)
# q = Point(3, -3)
# a = Point(-1, 1)
my_inbox = SMS_store()
my_inbox.add_new_arrival(0, 0, '1')
my_inbox.add_new_arrival(0, 0, '2')
my_inbox.add_new_arrival(0, 0, '3')
print('all texts in inbox:', my_inbox.inbox)
print('number of texts in inbox:', my_inbox.message_count())
print('text at index 0:', my_inbox.get_messages(0))
print('new text count:', my_inbox.message_count())
print('indexes of unread texts:', my_inbox.get_unread_indexes())
print('text at index 1:', my_inbox.get_messages(1))
print('indexes of unread texts:', my_inbox.get_unread_indexes())
my_inbox.delete(0)
print('new text count:', my_inbox.message_count())
my_inbox.clear()
print('new text count:', my_inbox.message_count())
print('text at index 0:', my_inbox.get_messages(0))

