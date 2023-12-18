"""
Ejercicio 9:

Genera un número aleatorio entre 1 y 9 (incluidos 1 y 9). Pídale al usuario que adivine el número y luego dígale si adivinó si fue demasiado bajo, demasiado alto o exactamente correcto. ( Sugerencia: recuerde utilizar las lecciones aportadas por el usuario desde el primer ejercicio )

Extras:

-Continúe el juego hasta que el usuario escriba "salir"
-Lleve un registro de cuántas conjeturas ha realizado el usuario y, cuando finalice el juego, imprímalo.
"""
import random
ganancias = 0
perdidas = 0
user = "indefinido"
while user != "salir":
    num = random.randint(1,9)
    print("Que numero del 1 al 9 cree que ha salido?: ")
    numuser = int(input(""))
    if numuser == num :
        print("¡Has adivinado!")
        ganancias = ganancias+1
    elif numuser <= num:
        print("Demasiado bajo, el numero era ",num)
        perdidas = perdidas+1
    elif numuser >= num:
        print("Demasiado alto, el numero era ",num)
        perdidas = perdidas+1
    print("Si quiere seguir, escriba ""salir"" para salir o ""continuar"" para continuar: ")
    user = input("")
print("Ganaste ",ganancias," veces y perdiste ",perdidas ,"veces")
