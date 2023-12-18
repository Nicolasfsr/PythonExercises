"""
Ejercicio 6:

Solicite al usuario una cadena e imprima si esta cadena es un palíndromo o no. (Un palíndromo es una cadena que se lee igual hacia adelante y hacia atrás).
"""
print("Digite la palabra: ")
value = input(str(""))
val = list(value)
val.reverse()
vals = ""
for x in val:
    vals += ""+ x
if value != vals:
    print("La palabra",value,"no es una palabra palíndroma")
elif value == vals:
    print("La palabra",value,"es una palabra palíndroma")