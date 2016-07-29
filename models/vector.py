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

    def get_x(self):
        if self.x != None:
            return self.x
        elif self.get_y() != None and self.get_r() != None:
            # r = sqrt(x*x + y*y) -> x = sqrt(r*r - y*y)
            self.x = math.sqrt(self.r * self.r - self.y * self.y)
        elif self.get_y() != None and self.get_theta() != None:
            # θ = atan(y/x) -> x = y / tan(θ)
            self.x = self.y / math.tan(self.theta)
        elif self.get_r() != None and self.get_theta() != None:
            # x = r * cos(θ)
            self.x = self.r * math.cos(self.theta)

        return self.x

    def get_y(self):
        if self.y != None:
            return self.y
        elif self.get_x() != None and self.get_r() != None:
            # r = sqrt(x*x + y*y) -> y = sqrt(r*r - x*x)
            self.y = math.sqrt(self.r * self.r - self.x * self.x)
        elif self.get_x() != None and self.get_theta() != None:
            # θ = atan(y/x) -> y = x * tan(θ)
            self.y = self.x * math.tan(self.theta)
        elif self.get_r() != None and self.get_theta() != None:
            # y = r * sin(θ)
            self.y = self.r * math.sin(self.theta)

        return self.y

    def get_r(self):
        if self.r != None:
            return self.r
        elif self.get_x() != None and self.get_y() != None:
            # r*r = x*x + y*y -> r = sqrt(x*x + y*y)
            self.r = math.hypot(self.x, self.y)
        elif self.get_x() != None and self.get_theta() != None:
            # x = r * cos(θ) -> r = x / cos(θ)
            self.r = self.x / math.cos(self.theta)
        elif self.get_y() != None and self.get_theta() != None:
            # y = r * sin(θ) -> r = y / sin(θ)
            self.r = self.y / math.sin(self.theta)

        return self.r

    def get_theta(self):
        if self.theta != None:
            return self.theta
        elif self.get_x() != None and self.get_y() != None:
            # tan(θ) = y / x -> θ = atan(y / x)
            self.theta = math.atan2(self.y, self.x)
        elif self.get_x() != None and self.get_r() != None:
            # x = r * cos(θ) -> θ = acos(x / r)
            self.theta = math.acos(self.x / self.r)
        elif self.get_y() != None and self.get_r() != None:
            # y = r * sin(θ) -> θ = asin(y / r)
            self.theta = math.asin(self.y / self.r)

        return self.theta
