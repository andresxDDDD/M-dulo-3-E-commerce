def agrega_producto(productos: list,carr_prod: list,id: int,cantidad:int):
      
      for i in productos:
         if i["id"]==id and cantidad > 0:
                  carro={
                   "id": i["id"],
                   "nombre": i["nombre"],
                   "precio" : i["precio"],
                  "cantidad": cantidad,
                   }
                  carr_prod.append(carro)
                  print(f"{i['nombre']} agregado al carrito.")
                  return(carr_prod)  
      print("Producto no agregado: ID no corresponde o la cantidad ingresada fue menor a 0")        

def calcular_total(carr_prod: list ):
    total = 0
    for item in carr_prod:
        total += item["precio"] * item["cantidad"]
    return total

def mostrar_carrito(carr_prod: list):
   print("\n------------------------Tu Carrito-----------------------")
   for item in carr_prod:
      subtotal = item["precio"] * item["cantidad"]
      print(f"id: {item["id"]}-- producto:{item["nombre"]}-- cantidad x {item["cantidad"]}--: ${subtotal}")
      print("----------------------------------------------------------")

def vaciar_carrito(carr_prod: list, op3: str):

    if op3.lower() == "si":
      carr_prod.clear()
      print("Carrito a sido eliminado")
    else:
        print("Opcion incorrecta")      