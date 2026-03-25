import os

def menu_pricipal():
    while True:

    
        print("-------------Menu-----------") 
        print("1- Ver catalogos de productos:")
        print("2- Buscar productos:")
        print("3- Agregar productos al carro:")
        print("4- Ver carro:")
        print("5- Vaciar carro:")
        print("6- Salir:")

        opcion= int(input("Ingrese una opcion: "))
        return opcion
    

def limpiar_pantalla():
    os.system('cls' if os.name == 'nt' else 'clear')