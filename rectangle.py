'''
Created on Jul 10, 2023

@author: renan
'''

class Rectangle:

    def __init__(self, width, height):
        self.width = width
        self.height = height

    def set_width(self, new_width):
        self.width = new_width

    def set_height(self, new_height):
        self.height = new_height

    def get_area(self):
        self.area = self.width * self.height
        return self.area

    def get_perimeter(self):
        self.perimeter = 2 * self.width + 2 * self.height
        return self.perimeter

    def get_diagonal(self):
        self.diagonal = float((self.width ** 2 + self.height ** 2) ** 0.5)
        return self.diagonal

    def get_picture(self):
        self.picture = ""
        if self.width > 50 or self.height > 50:
            self.picture = "Too big for picture."
        else:
            for row in range(self.height):
                for length in range(self.width):
                    self.picture += "*"
                self.picture += "\n"

        return self.picture

    def get_amount_inside(self, shape):
        self.area = self.get_area()
        self.shape_area = shape.get_area()
        self.times_in = 0
        while self.area >= self.shape_area:
            self.area -= self.shape_area
            self.times_in += 1

        return self.times_in

    def __str__(self):
        self.printing_shape = ""
        self.printing_sides = ""
        if self.width == self.height:
            self.printing_shape = "Square"
            self.printing_sides = "(side=" + str(self.width) + ")"
        else:
            self.printing_shape = "Rectangle"
            self.printing_sides = "(width=" + str(self.width) + ", height=" + str(self.height) + ")"

        self.printing = self.printing_shape + self.printing_sides

        return self.printing

class Square(Rectangle):
    
    def __init__(self, side):
        super().__init__(side, side)

    def set_side(self, new_side):
        super().set_width(new_side)
        super().set_height(new_side)

    def set_width(self, new_width):
        self.width = new_width
        self.height = new_width

    def set_height(self, new_height):
        self.width = new_height
        self.height = new_height
