#game 2
import os
from random import randint
lives=3
status=True
suma=0
###Funcion que retorna los numeros de dados que lanzo aleatoriamente 
def roll_dice():
    dice1=randint(1,6)
    dice2=randint(1,6)
    return dice1,dice2

############ MAIN ###########
#print(roll_dice())
#blucle while
while True:
    key = input("Press any key to roll dices : ")
    dices = roll_dice()
    print(f"Dice 1: {dices[0]}")
    print(f"Dice 2: {dices[1]}")
    #dices_unida="".join(map(str,dices)) ##para sumar los resultados de los dados
    #resul_ent=int(dices_unida)
    suma+=1
    if (dices[0]+dices[1])%2==0:
        lives+=1
    else:
        lives-=1
    if dices[0
             ]==6 and dices[1]==6:
        print("YOU WIN")
        print("con un total de lanzamientos", suma)
        os.system("pause")
        break     
    #print(lives) 
    if lives==0:
        print("GAMER OVER")
        print("con un total de lanzamientos", suma)
        break      