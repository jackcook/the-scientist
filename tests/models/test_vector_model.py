# -*- coding: utf-8 -*-

import math
from scientist import Vector

x = 2.5
y = 7.5
r = 7.905694150420948
theta = 1.2490457723982544

# ---------------- #

# x = r * cos(θ)
def test_x_from_r_and_theta():
    vec = Vector(r=r, theta=theta)
    assert vec.x == x

# r = x / cos(θ)
def test_r_from_x_and_theta():
    vec = Vector(x=x, theta=theta)
    assert vec.r == r

# θ = acos(x / r)
def test_theta_from_x_and_r():
    vec = Vector(x=x, r=r)
    assert vec.theta == theta

# ---------------- #

# y = r * sin(θ)
def test_y_from_r_and_theta():
    vec = Vector(r=r, theta=theta)
    assert vec.y == y

# r = y / sin(θ)
def test_r_from_y_and_theta():
    vec = Vector(y=y, theta=theta)
    assert round(vec.r, 4) == round(r, 4)

# θ = asin(y / r)
def test_theta_from_y_and_r():
    vec = Vector(y=y, r=r)
    assert vec.theta == theta

# ---------------- #

# r = sqrt(x*x + y*y)
def test_r_from_x_and_y():
    vec = Vector(x=x, y=y)
    assert vec.r == r

# x = sqrt(r*r - y*y)
def test_x_from_y_and_r():
    vec = Vector(y=y, r=r)
    assert vec.x == x

# y = sqrt(r*r - x*x)
def test_y_from_x_and_r():
    vec = Vector(x=x, r=r)
    assert vec.y == y

# ---------------- #

# θ = atan2(y, x)
def test_theta_from_x_and_y():
    vec = Vector(x=x, y=y)
    assert vec.theta == theta

# y = x * tan(θ)
def test_y_from_x_and_theta():
    vec = Vector(x=x, theta=theta)
    assert vec.y == y

# x = y / tan(θ)
def test_x_from_y_and_theta():
    vec = Vector(y=y, theta=theta)
    assert round(vec.x, 4) == round(x, 4)

# ---------------- #

def test_addition():
    vec1 = Vector(r=5, theta=0)
    vec2 = Vector(r=2, theta=math.radians(45))
    vec3 = vec1.add(vec2)

    assert round(vec3.x, 4) == 6.4142
    assert round(vec3.y, 4) == 1.4142
    assert round(vec3.r, 4) == 6.5683
    assert round(vec3.theta, 4) == 0.217

def test_subtraction():
    vec1 = Vector(r=5, theta=0)
    vec2 = Vector(r=2, theta=math.radians(45))
    vec3 = vec1.subtract(vec2)

    assert round(vec3.x, 4) == 3.5858
    assert round(vec3.y, 4) == -1.4142
    assert round(vec3.r, 4) == 3.8546
    assert round(vec3.theta, 4) == 0.3757
