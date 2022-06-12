import math


def calculate(a, b, c):

    discrement = (b ** 2) - (4 * a * c)
    divider = (2 * a)

    root1 = (-b - math.sqrt(discrement)) / divider
    root2 = (-b + math.sqrt(discrement)) / divider

    return root1, root2
