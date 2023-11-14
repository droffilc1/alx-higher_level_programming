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
        if not type(value) is int:
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")
        self.__width = value

    @property
    def height(self):
        """Property to retrieve height.
        Property setter to set height
        """
        return self.__height

    @height.setter
    def height(self, value):
        if not type(value) is int:
            raise TypeError("height must be an integer")
        if value <= 0:
            raise ValueError("height must be > 0")
        self.__height = value

    @property
    def x(self):
        """Property to retrieve x.
        Property setter to set x
        """
        return self.__x

    @x.setter
    def x(self, value):
        if not type(value) is int:
            raise TypeError("x must be an integer")
        if value < 0:
            raise ValueError("x must be >= 0")
        self.__x = value

    @property
    def y(self):
        """Property to retrieve y.
        Property setter to set y
        """
        return self.__y

    @y.setter
    def y(self, value):
        if not type(value) is int:
            raise TypeError("y must be an integer")
        if value < 0:
            raise ValueError("y must be >= 0")
        self.__y = value

    def area(self):
        """Defines area of a rectangle"""
        return self.__width * self.__height

    def display(self):
        """ Prints to stdout Rectangle instance with character '#' """
        string = ""
        for i in range(0, self.__height+self.__y):
            if self.__y > i:
                string += "\n"
                continue
            for j in range(0, self.__width+self.__x):
                if j >= self.__x:
                    string += "#"
                else:
                    string += " "
            if i == self.__height+self.__y - 1:
                string += "\n"
                break
            string += "\n"
        print(string, end="")

    def __str__(self):
        """Update class Rectangle"""
        return (
            f"[Rectangle] ({self.id}) {self.x}/{self.y} - "
            f"{self.width}/{self.height}"
        )

    def update(self, *args, **kwargs):
        """Assigns an argument to class attributes"""
        if args:
            if len(args) >= 1:
                self.id = args[0]
            if len(args) >= 2:
                self.__width = args[1]
            if len(args) >= 3:
                self.__height = args[2]
            if len(args) >= 4:
                self.__x = args[3]
            if len(args) >= 5:
                self.__y = args[4]
        for key, value in kwargs.items():
            setattr(self, key, value)

    def to_dictionary(self):
        """Returns the dictionary represenation of a Rectangle"""
        return {
            'x': self.x,
            'y': self.y,
            'id': self.id,
            'height': self.height,
            'width': self.width
        }
