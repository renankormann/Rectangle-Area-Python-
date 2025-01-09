'''
Created on Jul 10, 2023

@author: renan
'''
from rectangle import Rectangle
from rectangle import Square

#Testing the functions.

rect = Rectangle(5, 10)
print(rect.get_area())
rect.set_width(3)
print(rect.get_perimeter())
print(rect)
print(rect.get_amount_inside(2,3))

sq = Square(9)
print(sq.get_area())
sq.set_side(4)
print(sq.get_diagonal())
print(sq)
