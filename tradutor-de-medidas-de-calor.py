import os

def limpar ():
    if os.name == "posix":
        os.system ("clear")
    else:
        os.sytem ("cls")

def celcius ():
    celcius = float (input("qual o valor dos graus celcius : "))
    fire = (celcius * 9/5) + 32
    kelvin=celcius + 273.15
    print ("fahreinheight é",fire)
    print ("kelvin é ",kelvin)
def fire ():
    fire = float(input("qual o valor dos graus fahreinheight : "))
    celcius = (fire - 32) * 5/9 
    kelvin = (fire - 32) * 5/9 +273.15
    print ("celcius é ",celcius)
    print ("kelvin é ",kelvin)
def kelvin ():
    kelvin = float (input("qual o valor do graus em kelvin : "))
    celcius = kelvin - 273.15
    fire = (kelvin - 273.15) * 9/5 + 32
    print ("o celcius é ", celcius)
    print ("o fahreinheight é ",fire)
def escolha():
    esc2 = int (input("\n\nescolha 1 para continuar\n 2 para para parar\n ------>:"))
    if esc2 != 2 and esc2 != 1:
        print("retorne valores validos")
        escolha()
    if esc2 == 1:
        menu()
    if esc2== 2:
        aux = (input("nome do desenvolvedor: EDUARDO VERUS DE BRITTO\nenter para finalizar........"))
        exit (0)
def menu ():
    limpar()
    esc = int (input("digite:\n1 para celcius\n2 para fahreinheight\n3 para kelvin\n4 para sair\n-------> : "))
    if esc != 1 and esc !=2 and esc != 3 and esc != 4:
        print("por favor retorne valores pedidos")
        menu()
    limpar()
    if esc == 1:
        celcius()
        escolha()
    if esc == 2 :
        fire()
        escolha()
    if esc == 3:
        kelvin()
        escolha()
    if esc == 4:
        aux = (input("nome do desenvolvedor: EDUARDO VERUS DE BRITTO\nenter para finalizar........"))
        exit (0)
menu()
