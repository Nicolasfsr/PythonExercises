"""
Ejercicio 10:
El ejercicio de esta semana será revisar un ejercicio antiguo (ver Ejercicio 5 ), excepto que requerirá la solución de una manera diferente.

Tome dos listas, digamos, por ejemplo, estas dos:

	a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
	b = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]
y escriba un programa que devuelva una lista que contenga solo los elementos que son comunes entre las listas (sin duplicados). Asegúrese de que su programa funcione en dos listas de diferentes tamaños. Escriba esto en una línea de Python usando al menos una lista por comprensión . ( Pista: recuerde la lista de comprensiones del ejercicio 7 ).

La formulación original de este ejercicio decía escribir la solución usando una línea de Python, pero algunos lectores señalaron que esto era imposible de hacer sin usar setmensajes de correo electrónico que aún no había discutido en el blog, por lo que puedes optar por usar el Directiva original y lea sobre el setcomando en Python 3.3 , o intente implementar esto por su cuenta y use al menos una lista de comprensión en la solución.

Extra:

Genere aleatoriamente dos listas para probar esto
"""
a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
b = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13] 

print( list(set([x for x in a if x in b ])))

