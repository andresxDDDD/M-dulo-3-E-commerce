def ver_productos(productos: list):
    print("------Bienvenido a nuestros productos:------")
    if not productos:
        print("No hay resultados")
        return

    for p in productos:
        print(f"{p['id']} - {p['nombre']}- Precio:(${p['precio']}) [{p['categoria']}]")


def buscar_producto(catalogo: list,msj:str):
    encontrar= False
    
    for i in catalogo:
             if msj.lower() in i["nombre"].lower() or msj.lower() in i["categoria"].lower():
                print(f"{i['id']} - {i['nombre']}- Precio (${i['precio']}) [{i['categoria']}]")
                encontrar=True
    if not encontrar: 
         print("productos no encontrado por favor revise nuestro catalogo:")            






          