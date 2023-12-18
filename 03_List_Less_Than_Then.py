"""
Ejercicio 3:

Tome una lista, diga por ejemplo esta:
  a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
y escriba un programa que imprima todos los elementos de la lista que son menos de 5.

Extras:

- En lugar de imprimir los elementos uno por uno, haga una nueva lista que tenga todos los elementos menos de 5 de esta lista e imprima esta nueva lista.
- Solicite al usuario un número y devuelva una lista que contenga solo elementos de la lista original aque sean más pequeños que el número proporcionado por el usuario.
"""
print("Digite un numero: ")
num = int(input(""))
a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
n = 0
f = []
while n <= len(a)-1:
    if a[n] < num:
        f.append(a[n])
        n = n + 1
    else:
        n = n + 1 
print(f)