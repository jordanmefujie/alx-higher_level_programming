#!/usr/bin/python3
"""
Module to import class Base
"""

from models.base import Base



class Rectangle(Base):
    """class intialization"""

    def __init__(self, width, height, x=0, y=0, id=None):

        self.width = width

        self.height = height

        self.x = x

        self.y = y

        super().__init__(id)


    @property

    def width(self):
        """gets width"""

        return self.__width


    @width.setter

    def width(self, value):
        """sets width"""

        self.setter_validation("width", value)

        self.__width = value


    @property

    def height(self):
        """gets height"""

        return self.__height


    @height.setter

    def height(self, value):
        """sets height"""

        self.setter_validation("height", value)

        self.__height = value


    @property

    def x(self):
        """gets x"""

        return self.__x


    @x.setter

    def x(self, value):
        """sets x"""

        self.setter_validation("x", value)

        self.__x = value


    @property

    def y(self):
        """gets y"""

        return self.__y


    @y.setter

    def y(self, value):
        """sets y"""

        self.setter_validation("y", value)

        self.__y = value


    def area(self):
        """Return area of rectangle"""

        return (self.height * self.width)


    def display(self):
        """Print shape of rectangle with # in stdout"""

        rectangle = ""

        print("\n" * self.y, end="")

        for i in range(self.height):

            rectangle += (" " * self.x) + ("#" * self.width) + "\n"

        print(rectangle, end="")


    def update(self, *args, **kwargs):
        """A public method that assigns an argument to each attribute"""

        if len(args) == 0:

            for key, val in kwargs.items():

                self.__setattr__(key, val)

            return

        try:

            self.id = args[0]

            self.width = args[1]

            self.height = args[2]

            self.x = args[3]

            self.y = args[4]

        except IndexError:

            pass


    def to_dictionary(self):
        """The dictionary representation"""

        return {'x': getattr(self, "x"),

                'y': getattr(self, "y"),

                'id': getattr(self, "id"),

                'height': getattr(self, "height"),

                'width': getattr(self, "width")}


    @staticmethod

    def setter_validation(attribute, value):
        """At static method"""

        if type(value) != int:

            raise TypeError("{} must be an integer".format(attribute))

        if attribute == "x" or attribute == "y":

            if value < 0:

                raise ValueError("{} must be >= 0".format(attribute))

        elif value <= 0:

            raise ValueError("{} must be > 0".format(attribute))


    def __str__(self):
        """Overriding the _str_method"""

        return "[Rectangle] ({}) {}/{} - {}/{}".format(self.id, self.x, self.y,

                                                       self.width, self.height)
