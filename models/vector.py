# -*- coding: utf-8 -*-

import math

"""
    Vector
    ~~~~~~

    Properties:
    - `x` The x coordinate of the point defining the vector
    - `y` The y coordinate of the point defining the vector
    - `r` The magnitude of the vector
    - `theta` The angle marking the vector's direction, in radians

    Important equations:
    - x = r * cos(θ)
    - y = r * sin(θ)
    - r = sqrt(x*x + y*y)
    - tan(θ) = y / x
"""

class Vector:

    x = None
    y = None
    r = None
    theta = None

    def __init__(self, x=None, y=None, r=None, theta=None):
        self.x = x
        self.y = y
        self.r = r
        self.theta = theta

        self.check_equations()

    def __init__(self, dict):
        if "x" in dict: self.x = float(dict["x"])
        if "y" in dict: self.y = float(dict["y"])
        if "r" in dict: self.r = float(dict["r"])
        if "theta" in dict: self.theta = float(dict["theta"])

        self.check_equations()

    def add(self, vector):
        x = self.x + vector.x
        y = self.y + vector.y
        return Vector(x=x, y=y)

    def subtract(self, vector):
        x = self.x - vector.x
        y = self.y - vector.y
        return Vector(x=x, y=y)

    def check_equations(self):
        if self.check_x_equation(): self.check_equations()
        if self.check_y_equation(): self.check_equations()
        if self.check_r_equation(): self.check_equations()
        if self.check_theta_equation(): self.check_equations()

    # x = r * cos(θ)
    def check_x_equation(self):
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

    # y = r * sin(θ)
    def check_y_equation(self):
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

    # r = sqrt(x*x + y*y)
    def check_r_equation(self):
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

    # tan(θ) = y / x
    def check_theta_equation(self):
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
