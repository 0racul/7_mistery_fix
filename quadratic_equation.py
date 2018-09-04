from math import sqrt


def get_roots(a, b, c):

    discriminant = b ** 2 - 4 * a * c
    root1 = (-b - sqrt(discriminant)) / (2 * a)

    if discriminant < 0:

        root1 = None
        root2 = None

        return root1, root2

    elif discriminant == 0:

        root2 = None
        return root1, root2

    else:

        root2 = (-b + sqrt(discriminant)) / (2 * a)
        return root1, root2
