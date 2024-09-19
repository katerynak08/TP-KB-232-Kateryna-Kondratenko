def discriminant(a, b, c):
    D = b**2 - 4*a*c
    return D

a = float(input("Введіть коефіцієнт a: "))
b = float(input("Введіть коефіцієнт b: "))
c = float(input("Введіть коефіцієнт c: "))

result = discriminant(a, b, c)
print(f"Дискримінант рівняння: {result}")
