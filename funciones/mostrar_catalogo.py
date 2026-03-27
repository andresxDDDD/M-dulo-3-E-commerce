def ver_productos(productos: list):
    print("------Bienvenido a nuestros productos:------")
    if not productos:
        print("No hay resultados")
        return

    for p in productos:
        print(f"{p['id']} - {p['nombre']} (${p['precio']}) [{p['categoria']}]")


def buscar_producto(productos: list,msj:str):
    encontrar= False
    if not productos:
            print("No hay resultados")
            return
    else:       
        for i in productos:
             if msj== i["nombre"].lower() or msj== i["categoria"].lower():
                print(f"{i['id']} - {i['nombre']} (${i['precio']}) [{i['categoria']}]")
                encontrar=True
    if not encontrar: 
         print("productos no encontrado por favor revise nuestro catalogo:")            






          