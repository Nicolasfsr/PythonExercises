"""
Ejercicio 2:

El ejercicio viene primero (con algunos extras si desea un desafío adicional o quiere pasar más tiempo), seguido de una discusión. ¡Disfrutar!

Pide al usuario un número. Dependiendo de si el número es par o impar, imprima un mensaje apropiado para el usuario. Pista: ¿cómo reacciona de manera diferente un número par/impar cuando se divide por 2?

Extras:

- Si el número es un múltiplo de 4, imprima un mensaje diferente.
- Solicite al usuario dos números: un número para verificar (llámelo num) y un número para dividir por ( check). Si se checkdivide uniformemente en num, dígaselo al usuario. Si no, imprima un mensaje apropiado diferente.
"""
print("Ingresa un numero: ")
numero = int(input(""))
print("Ingresa un numero: ")
check = int(input(""))
num = numero
if numero % 4 == 0:
    print("El numero" ,numero, "es multiplo de 4")
elif numero % 2 == 1:
    print("El numero", numero, "es impar")
elif numero % 2 == 0:
    print("El numero", numero, "es par")
if num % check == 0:
    print(numero, "es divisible entre" ,check)
else:
    print(numero, "no es divisible entre" ,check)