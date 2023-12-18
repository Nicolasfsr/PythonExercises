"""
Digamos que te doy una lista guardada en una variable: a = [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]. Escribe una línea de Python que tome esta lista a y cree una nueva lista que contenga solo los elementos pares de esta lista.
"""
a = [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]
print([a[i] for i in range(len(a)) if a[i] % 2 == 0])