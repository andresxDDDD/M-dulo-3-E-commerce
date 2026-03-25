def ver_productos(productos):
    if not productos:
        print("No hay resultados")
        return

    for p in productos:
        print(f"{p['id']} - {p['nombre']} (${p['precio']}) [{p['categoria']}]")


def buscar_producto(productos: list,msj:str):

    if not productos:
            print("No hay resultados")
            return
    else:       
        for i in productos:
             if msj== i["nombre"].lower() or msj== i["categoria"].lower():
                print(f"{i['id']} - {i['nombre']} (${i['precio']}) [{i['categoria']}]")






          