"""
Ejercicio 8:

Crea un juego de piedra, papel o tijera para dos jugadores. ( Sugerencia: pregunte por las jugadas de los jugadores (usando input), compárelas, imprima un mensaje de felicitación para el ganador y pregunte si los jugadores quieren comenzar un nuevo juego ).
"""
import random
n = True
while n == True:
  Player = input("Elija Piedra, Papel o Tijeras: ")
  Bot = random.randint(1, 3)
  if Bot == 1:
    Bot = "Piedra"
  elif Bot == 2:
    Bot = "Papel"
  elif Bot == 3:
    Bot = "Tijeras"


  if Bot == "Piedra" and Player == "Papel":
    Ganador = "Player"
  elif Bot == "Tijeras" and Player == "Papel":
    Ganador = "Bot"
  elif Bot == "Tijeras" and Player == "Piedra":
    Ganador = "Player"
  elif Bot == "Piedra" and Player == "Tijeras":
    Ganador = "Bot"
  elif Bot == "Papel" and Player == "Tijeras":
    Ganador = "Player"
  elif Bot == "Papel" and Player == "Piedra":
    Ganador = "Bot"
  else:
    Ganador = "Empate"
  if Ganador == "Bot":
    print("Sorry, Has perdido")
  elif Ganador == "Player":
    print("Que bien, Has ganado")
  elif Ganador == "Empate":
    print("EMPATE")
  y = input("Quieres seguir jugando: ")
  if y == "Si":
    n = True
  elif y == "No":
    break