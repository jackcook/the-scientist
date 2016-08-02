# -*- coding: utf-8 -*-

import math

class Vector:
    """A vector on a 2D plane.

    Attributes:
        x: The x coordinate of the point defining this vector.
        y: The y coordinate of the point defining this vector.
        r: The vector's magnitude.
        theta: The angle marking the vector's direction, in radians.
    """

    def __init__(self, x=None, y=None, r=None, theta=None, dict=None):
        """Inits Vector with its attributes or a dictionary of them."""

        if dict:
            if "x" in dict: self.x = float(dict["x"])
            if "y" in dict: self.y = float(dict["y"])
            if "r" in dict: self.r = float(dict["r"])
            if "theta" in dict: self.theta = float(dict["theta"])
        else:
            self.x = x
            self.y = y
            self.r = r
            self.theta = theta

        self.check_equations()

    def add(self, vector):
        """Adds this vector to another vector.

        Args:
            vector: The vector being added to this one.

        Returns:
            A new vector, the result of adding the two other vectors.
        """

        x = self.x + vector.x
        y = self.y + vector.y
        return Vector(x=x, y=y)

    def subtract(self, vector):
        """Subtracts this vector from another vector.

        Args:
            vector: The vector being subtracted from this one.

        Returns:
            A new vector, the result of subtracting the two other vectors.
        """

        x = self.x - vector.x
        y = self.y - vector.y
        return Vector(x=x, y=y)

    def check_equations(self):
        """Checks all vector equations, updating as many values as possible."""

        if self.check_x_equation(): self.check_equations()
        if self.check_y_equation(): self.check_equations()
        if self.check_r_equation(): self.check_equations()
        if self.check_theta_equation(): self.check_equations()

    def check_x_equation(self):
        """Updates values that can be derived from the equation for x,
        x = r * cos(θ)"""

        if self.x == None and self.r != None and self.theta != None:
            self.x = self.r * math.cos(self.theta)
            return True
        elif self.r == None and self.x != None and self.theta != None:
            self.r = self.x / math.cos(self.theta)
            return True
        elif self.theta == None and self.x != None and self.r != None:
            self.theta = math.acos(self.x / self.r)
            return True

        return False

    def check_y_equation(self):
        """Updates values that can be derived from the equation for y,
        y = r * sin(θ)"""

        if self.y == None and self.r != None and self.theta != None:
            self.y = self.r * math.sin(self.theta)
            return True
        elif self.r == None and self.y != None and self.theta != None:
            self.r = self.y / math.sin(self.theta)
            return True
        elif self.theta == None and self.y != None and self.r != None:
            self.theta = math.asin(self.y / self.r)
            return True

        return False

    def check_r_equation(self):
        """Updates values that can be derived from the equation for magnitude,
        r = sqrt(x*x + y*y)"""

        if self.r == None and self.x != None and self.y != None:
            self.r = math.hypot(self.x, self.y)
            return True
        elif self.x == None and self.r != None and self.y != None:
            self.x = math.sqrt(self.r * self.r - self.y * self.y)
            return True
        elif self.y == None and self.r != None and self.x != None:
            self.y = math.sqrt(self.r * self.r - self.x * self.x)
            return True

        return False

    def check_theta_equation(self):
        """Updates values that can be derived from the equation for theta,
        tan(θ) = y / x"""

        if self.theta == None and self.x != None and self.y != None:
            self.theta = math.atan2(self.y, self.x)
            return True
        elif self.y == None and self.x != None and self.theta != None:
            self.y = self.x * math.tan(self.theta)
            return True
        elif self.x == None and self.y != None and self.theta != None:
            self.x = self.y / math.tan(self.theta)
            return True

        return False
