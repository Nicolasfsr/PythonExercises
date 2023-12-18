"""
Pide al usuario un número y determina si el número es primo o no. (Para aquellos que lo hayan olvidado, un número primo es un número que no tiene divisores). Puedes (¡y debes!) usar tu respuesta al Ejercicio 4 como ayuda. Aproveche esta oportunidad para practicar el uso de las funciones que se describen a continuación.
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
if f == [1, num] :
    print("El numero es primo")
else:
    print("El numero no es primo")