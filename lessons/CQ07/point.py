"""Defining the Point class."""

from __future__ import annotations
__author__ = "730642818"


class Point:
    """This class represents the point."""
    x: float
    y: float

    def __init__(self, x_input: float = 0.0, y_input: float = 0.0):
        """Constructor."""
        self.x = x_input
        self.y = y_input

    def __str__(self) -> str:
        """Print Point in a readable way."""
        string: str = f"x: {str(self.x)}; y: {str(self.y)}"
        return string

    def __mul__(self, factor: int | float) -> Point:
        """Creat a new point with each component multiplied by the factor."""
        new_point: Point = Point(self.x * factor, self.y * factor)
        return new_point     

    def __add__(self, factor: int | float) -> Point:
        """Create a new point with each component added by the factor."""
        new_point: Point = Point(self.x + factor, self.y + factor)
        return new_point

    def scale_by(self, factor: int) -> None:
        """Scale the point up by factor."""
        self.x *= factor
        self.y *= factor
    
    def scale(self, factor: int) -> Point:
        """Create a new point that is scaled up by factor."""
        new_point: Point = Point(self.x * factor, self.y * factor)
        return new_point