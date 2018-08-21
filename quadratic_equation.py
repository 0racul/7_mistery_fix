from math import sqrt


def get_roots(a, b, c):
    discriminant = b ** 2 - 4 * a * c
    root1 = (-b - sqrt(abs(discriminant))) / (2 * a)
    root2 = (-b + sqrt(abs(discriminant))) / (2 * a)

    return root1, root2
