#projeto pessoal com intuito de marcar e analizar ganhador de bisca

import os
import time
run = True
fs = True
cond = True
p1 = 0
p2 = 0
p3 = 0
njog = 2
def limpar():
    if os.name == ("posix"):
        os.system ("clear")
    else:
        os.system ("cls")
    

while run == True:
    if fs == True:
        limpar()
        if njog > 3 or njog < 2:
            print("retorne os valores validos : ")
        njog = int(input("selecione 2 para dois jogadores ou duplas\nou digite 3 para trio\n-------------> : "))
        fs = False
        if njog > 3 or njog < 2:
            run == True
            fs == True
    while cond == True:
        limpar()
        np1 = int(input("qual o numero de pontos do jogador 1 : "))
        p1 = p1 + np1
        limpar()
        np2 = int(input("qual o numero de pontos do jogador 2 : "))
        p2 = p2 + np2
        if njog == 3:
            limpar()
            np3 = int(input("qual o numero de pontos do player 3 : "))
            p3 = p3+np3
        cond == False
        break
            
        
    limpar()
    esc = int(input("1 para continuar\n2 para resetar\n3 para sair : "))
    if esc == 1:
        run = True
        cond = True
    elif esc == 2:
        p1 = 0
        p2 = 0
        np1 = 0
        np2 = 0
        if njog == 3:
            p3 = 0
            np3 = 0
        fs = True
        cond = True
        run = True
    else:
        if esc == 3:
            break
        else:
            print ("retorne valores validos")
limpar()
if njog == 2 :
    if p1>p2 :
        print("o jogador ganhador é o player 1 com ",p1,"pontos\nseguido do player 2 com",p2,"pontos")
    elif p2>p1 :
        print("o jogador ganhador é o player 2 com ",p2,"pontos\nseguido do player 1 com",p1,"pontos")
    else:
        print("ambos empataram com ",p1," pontos")
if njog ==3 :
    if p1 > p2 and p1 > p3:
        if p2 > p3:
            print ("o ganhador é o player 1 com ",p1,"pontos\nseguido pelo player 2 com ",p2," pontos\ne o player 3 com ",p3,"pontos")
        elif p3 > p2:
            print ("o ganhador é o player 1 com ",p1," pontos\nseguido do player 3 com ",p3,"pontos\ne o player 2 com",p2,"pontos")
        else:
            print("o ganhador é o player 1 com",p1,"pontos \nseguido de um empate enrtre player 2 e player 3 com",p2,"pontos cada um")
    elif  p2 > p1 and p2 > p3:
        if p1>p3:
            print ("o ganhador é o player 2 com ",p2,"pontos\nseguido pelo player 1 com ",p1," pontos\ne o player 3 com ",p3,"pontos")
        elif p3>p1:
            print ("o ganhador é o player 2 com ",p2,"pontos\nseguido pelo player 2 com ",p3," pontos\ne o player 3 com ",p1,"pontos")
        else:
            print("o ganhador é o player 2 com",p2,"pontos \nseguido de um empate entre player 1 e player 3 com",p1,"pontos cada um")
    else:
        if p3 >p2 and p3 > p1:
            if p1 > p2:
                print ("o ganhador é o player 3 com ",p3,"pontos\nseguido pelo player 1 com ",p1," pontos\ne o player 2 com ",p2,"pontos")
            elif p2 > p1:
                print ("o ganhador é o player 3 com ",p3,"pontos\nseguido pelo player 2 com ",p2," pontos\ne o player 1 com ",p1,"pontos")
            else:
                print("o ganhador é o player 3 com",p3,"pontos \nseguido de um empate entre player 1 e player 2 com",p2,"pontos cada um")
        elif p1 == p2 and p1 == p3 and p2 == p3:
            print("não sei como voces empataram com ",p1," pontos cada um ")
aux = (input("\n\n\n\nnome do desenvolvedor : EDUARDO VERUS DE BRITTO\ntecle enter para finalizar..................."))

