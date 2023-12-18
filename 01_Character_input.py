"""
Ejercicio 1:

Cree un programa que le pida al usuario que ingrese su nombre y su edad. Imprime un mensaje dirigido a ellos que les indique el año en que cumplirán 100 años. Nota: para este ejercicio, la expectativa es que escriba explícitamente el año (y, por lo tanto, esté desactualizado el próximo año). Si quiere hacer esto de forma genérica, vea el ejercicio 39 .

Extras:

- Agregue al programa anterior pidiéndole al usuario otro número e imprimiendo tantas copias del mensaje anterior. ( Pista: el orden de las operaciones existe en Python )
- Imprima esa cantidad de copias del mensaje anterior en líneas separadas. ( Pista: la cadena " \n es lo mismo que presionar el botón ENTER )
"""
print("Ingrese su nombre: ")
nombre = input("")
print("Ingrese su edad: ")
edad = int(input(""))
print("Ingrese un numero: ")
value = int(input(""))
centenario = (100-edad)+2023
x = 0
while x < value:
    print("Hola",nombre,", tendras 100 años en: " ,centenario)
    x=x+1