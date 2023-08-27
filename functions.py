import math
def almighty_formula(a, b, c):
    positive = (-b + math.sqrt((b**2)-(4*a*c)))/(2*a)
    negative = (-b - math.sqrt((b**2)-(4*a*c)))/(2*a)
    results = (positive, negative)
    return results

print(almighty_formula(3,-10,8))