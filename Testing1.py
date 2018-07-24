import sympy

# returns tangent line to the ellipse
def tangent(x, y):
    slope = x / y
    slope *= (-4)
    yIntercept = y
    yIntercept -= slope * x
    return slope, yIntercept


# returns intersection of two lines
def intersection(m1, b1, m2, b2):
    x = b2 - b1
    x /= m1 - m2
    y = m1 * x
    y += b1
    return x, y


# returns tangent line at given point, tangent line input first
def reflect(m2, b2, m3, b3, xpoint, ypoint):
    m = 2 * m2 - m3 + (m3) * (m2 ** 2)
    m /= (2 * m2 * m3) - (m2 ** 2) + 1
    b = ypoint - m * xpoint
    return m, b


m = 14.071428571428571428571428571429
b = 10.1
tanx, tany = tangent(1.4, -9.6)

print(intersection(m, b, tanx, tany))
