#!/usr/bin/python3
""" Square  """
from models.rectangle import Rectangle


class Square(Rectangle):
    """This is the square class that inherit from rectangle class"""

    def __init__(self, size, x=0, y=0, id=None):
        """
        Initializes a new instance of the Square class.
        """
        super().__init__(size, size, x, y, id)

    def __str__(self) -> str:
        return "[Square] ({}) {}/{} - {}".format(
            self.id,
            self.x,
            self.y,
            self.width,
        )

    @property
    def size(self):
        """Return the size property"""
        return self.width

    @size.setter
    def size(self, value):
        self.width = value
        self.height = value
