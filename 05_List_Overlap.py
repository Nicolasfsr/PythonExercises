"""
Ejercicio 5:

Toma dos listas, digamos por ejemplo estas dos:

  a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
  b = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]
y escriba un programa que devuelva una lista que contenga solo los elementos que son comunes entre las listas (sin duplicados). Asegúrese de que su programa funcione en dos listas de diferentes tamaños.

Extras:
- Genere aleatoriamente dos listas para probar esto
- Escriba esto en una línea de Python (no se preocupe si no puede resolver esto en este momento; lo abordaremos pronto)
"""
# a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
# b = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]

import random
a = [random.randint(1, 20) for i in range(random.randint(10, 15))]
b = [random.randint(1, 20) for i in range(random.randint(10, 15))]

print( list(set([x for x in a if x in b ])))
