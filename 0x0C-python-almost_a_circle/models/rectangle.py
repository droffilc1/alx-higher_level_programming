#!/usr/bin/python3
""" rectangle """


from models.base import Base


class Rectangle(Base):
    """A Rectangle class that inherits from Base."""
    def __init__(self, width, height, x=0, y=0, id=None):
        """Initializing data."""
        super().__init__(id)
        self.width = width
        self.height = height
        self.x = x
        self.y = y

    @property
    def width(self):
        """Property to retrieve width.
        Property setter to set width
        """
        return self.__width

    @width.setter
    def width(self, value):
        self.__width = value

    @property
    def height(self):
        """Property to retrieve height.
        Property setter to set height
        """
        return self.__height

    @height.setter
    def height(self, value):
        self.__height = value

    @property
    def x(self):
        """Property to retrieve x.
        Property setter to set x
        """
        return self.__x

    @x.setter
    def x(self, value):
        self.__x = value

    @property
    def y(self):
        """Property to retrieve y.
        Property setter to set y
        """
        return self.__y

    @y.setter
    def y(self, value):
        self.__y = value
