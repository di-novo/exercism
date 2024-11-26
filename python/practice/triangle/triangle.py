def istriangle(sides):
    a, b, c = sides
    return (a + b >= c) and (b + c >= a) and (a + c >= b) and 0 not in sides

def equilateral(sides):
    a, b, c = sides
    return istriangle(sides) and a==b and b==c

def isosceles(sides):
    a, b, c = sides
    return istriangle(sides) and len(set(sides)) <= 2

def scalene(sides):
    a, b, c = sides
    return istriangle(sides) and a != b and b != c and c != a
