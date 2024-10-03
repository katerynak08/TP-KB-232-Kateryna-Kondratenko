import math

def discriminant(a, b, c):
    D = b**2 - 4*a*c
    return D

def froots(a, b, c):
    D = discriminant(a, b, c) 
    if D > 0:
        root1 = (-b + math.sqrt(D)) / (2 * a)
        root2 = (-b - math.sqrt(D)) / (2 * a)
        return f"Рівняння має два різні дійсні корені: x1 = {root1}, x2 = {root2}"
    elif D == 0:
        root = -b / (2 * a)
        return f"Рівняння має один дійсний корінь: x = {root}"
    else:
        return "Рівняння не має дійсних коренів"

a = float(input("Введіть коефіцієнт a: "))
b = float(input("Введіть коефіцієнт b: "))
c = float(input("Введіть коефіцієнт c: "))

result = froots(a, b, c)
print(result)

