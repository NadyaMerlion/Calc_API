import cmath


def calculate(a, b, c):
    discrement = (b ** 2) - (4 * a * c)
    divider = (2 * a)

    root1 = (-b - cmath.sqrt(discrement)) / divider
    root2 = (-b + cmath.sqrt(discrement)) / divider
    if discrement > 0:
        return root1, root2
    elif discrement < 0:
        return None
    else:
        return root1, None
