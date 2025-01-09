'''
Created on Jul 10, 2023

@author: renan
'''

# Class with all the necessary functions to work properly.
class Rectangle:

    # Define the rectangle with width and height
    def __init__(self, width, height):
        self.width = width
        self.height = height

    # Function to change the width of the rectangle
    def set_width(self, new_width):
        self.width = new_width

    # Function to change the height of the rectangle
    def set_height(self, new_height):
        self.height = new_height

    # Function that returns the area of the rectangle
    def get_area(self):
        self.area = self.width * self.height
        return self.area

    # Function that returns the perimeter of the rectangle
    def get_perimeter(self):
        self.perimeter = 2 * self.width + 2 * self.height
        return self.perimeter

    # Function that returns the size of the diagonal of the rectangle
    def get_diagonal(self):
        self.diagonal = float((self.width ** 2 + self.height ** 2) ** 0.5)
        return self.diagonal

    # Function that draws the rectangle with * . Must be smaller or equal to 50 by 50
    def get_picture(self):
        self.picture = ""
        if self.width > 50 or self.height > 50:
            self.picture = "Too big for picture."
        else:
            for _ in range(self.height):
                for _ in range(self.width):
                    self.picture += "*"
                self.picture += "\n"

        return self.picture

    # This function calculates the amount of rectangles that fits inside of the rectangle given
    def get_amount_inside(self, t_width, t_height):
        self.times_in = 0
        if t_width <= self.width and t_height <= self.height:
            for _ in range(t_width, self.width, t_width):
                for _ in range(t_height, self.height, t_height):
                    self.times_in += 1
        
        return self.times_in

    # This functions sets up what is going to be printed when asked to print a rectangle.
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

# This is a class that creates a square but also have access to the rectangle functions.
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
