"""
Ejercicio 4:

Cree un programa que le pida al usuario un número y luego imprima una lista de todos los divisores de ese número. (Si no sabe qué es un divisor , es un número que se divide por igual entre otro número. Por ejemplo, 13 es un divisor de 26 porque 26/13 no tiene resto).
"""
print("Digite un numero: ")
num = int(input(""))
n = 1
f = []
while n <= num:
    if num % n == 0:
        f.append(n)
        n = n + 1 
    else:
        n = n + 1 
print(f)