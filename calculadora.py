#esse foi um  exercicio feito para treinar principios basicos

import math
import os 
def limpar():
    if os.name == "posix":
        os.system ("clear")
    else:
        os.system ("cls")
def somar () :
    soma1 = float(input("qual o primeiro valor : "))
    soma2 = float(input("qual o segundo valor : "))
    soma = soma1 + soma2
    print ("a soma é ",soma)
    
def subtrair () :
    sub1 = float(input("qual o primeiro valor : "))
    sub2 = float(input("qual o segundo valor : "))
    sub = sub1 - sub2
    print ("a subtração é ",sub)
    
def multy ():
    multy1 = float(input("qual o primero valor :"))
    multy2 = float(input("qual o valor a ser multiplicado : "))
    multy = multy1 * multy2
    print("a multiplicação é",multy)

def divisão ():
    div1 = float (input("qual o primeiro valor :"))
    div2 = float (input("qual o valor a ser divido :"))
    div = div1 / div2
    print("a divisão é ",div)

def fatorial():
    xp = int(input("qual o número a ser fatorado: "))
    fatorial = 1  
    while xp > 0:
        fatorial = fatorial * xp
        xp = xp - 1
    print("o fatorial é ",fatorial)

print("O fatorial é", fatorial)

def potencia ():
    base = int (input("qual o numero base :"))
    expoencia = int (input("qual o expoente : "))
    potencia = base ** expoencia
    print("a potencia é ",potencia)

def raiz():
    nraiz = int(input("qual o nuimero que você deseja a raiz quadrada : "))
    raiz = nraiz ** 1/2 
    print ("a raiz é ",raiz)

def porcentagem ():
    n1 = float (input("qual a porcentagem que deseja :"))
    n2 = float (input("de que numero : "))
    porcentagem = (n2 / 100) * n1
    print("a porcentagem é ",porcentagem)

def logaritimo ():
    limpar()
    base = float(input("Qual é a base do logaritmo: "))
    valor = float(input("Qual é o valor do logaritmo: "))
    resultado = math.log(valor, base)
    print("o logaritimo na base ",base ," de" ,valor," é ",resultado,)


def menu():
    fs = True
    limpar()
    if fs == True:
        
        esc = int(input("digite :\n1 para subtrair\n2 para somar\n3 para multiplicar\n4 para dividir\n5 para fatorial\n6 para potencia\n7 para raiz\n8 para porcentagem\n9 para logaritimo\n------------------> : "))
        if esc != 1 and esc != 2 and esc != 3 and esc != 4 and esc != 5 and esc != 6 and esc != 7 and esc != 8 and esc != 9:
            print("retorne valores validos")
        limpar()
        if esc == 1:
            subtrair()
        if esc == 2:
            somar()
        if esc == 3:
            multy()
        if esc == 4:
            divisão()
        if esc == 5:
            fatorial()
        if esc == 6:
            potencia()
        if esc == 7:
            raiz()
        if esc == 8:
            porcentagem()
        if esc == 9:
            logaritimo()
        fs = False
        if esc != 1 and esc != 2 and esc != 3 and esc != 4 and esc != 5 and esc != 6 and esc != 7 and esc != 8 and esc != 9:
            menu()
            fs = True
    
    esc2 = int(input("1 para continuar\n2 para parar\n -----> : "))
    limpar()
    if esc2 == 1:
        fs == True
        menu()
    elif esc2 == 2 :
        posmenu()
    else :
        print ("retorne um valor valido")

def posmenu():
    aux = (input("codigo feito por :EDUARDO VERUS DE BRITTO\ntecle enter para finalizar............."))
    exit()

menu()
