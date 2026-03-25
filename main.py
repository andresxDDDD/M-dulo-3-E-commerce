from menu.menu import menu_pricipal,limpiar_pantalla
from funciones.mostrar_catalogo import ver_productos, buscar_producto
from productos.catalogo import catalogo
from carrito.agregar_carrito import agrega_producto


def main():
    """ carrito = [] """

    while True:
        limpiar_pantalla()
        opcion=menu_pricipal()

        

        if opcion ==1:
      
            limpiar_pantalla()
            print("Bienvenido a nuestros productos")
            ver_productos(catalogo)
           
            input("\nPresiona Enter para volver al menú...")

        elif opcion ==2:

            limpiar_pantalla()
            print("Buscar productos:")
            msj=input("Ingrese Nombre o categoraia del producto a buscar:")
            buscar_producto(catalogo,msj)
            input("\nPresiona Enter para volver al menú...")


        elif opcion ==3:
            limpiar_pantalla()
            print("Agregar productos al carrito:")
            op1= input("ingrese ID del producto a comprar")
            op2= input("Ingrese la cantidad")
            agrega_producto(catalogo,op1,op2)
            input("\nPresiona Enter para volver al menú...")

        elif opcion ==4:
            limpiar_pantalla()
            print("Ver carro de compras")
            input("\nPresiona Enter para volver al menú...")


        elif opcion ==5:
            limpiar_pantalla()
            print("Vaciar el carro de compras")
            input("\nPresiona Enter para volver al menú...")


        elif opcion ==6:
           break

main()    