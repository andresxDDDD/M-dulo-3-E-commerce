def agrega_producto(productos: list,carr_prod,id: int,cantidad:int):
      
      for i in productos:
         if i["id"]==id:
                  carro={
                   "id": i["id"],
                   "nombre": i["nombre"],
                   "precio" : i["precio"],
                  "cantidad": cantidad,
                   }
                  carr_prod.append(carro)
                  print(f"{i['nombre']} agregado al carrito.")
                  return(carr_prod)  
      print("Producto no agregado: ID no corresponde revisa nuestro catalogo")        

def calcular_total(carr_prod ):
    total = 0
    for item in carr_prod:
        total += item["precio"] * item["cantidad"]
    return total

def mostrar_carrito(carr_prod):
   print("\n--- Tu Carrito ---")
   for item in carr_prod:
      subtotal = item["precio"] * item["cantidad"]
      print(f"{item["nombre"]} x {item["cantidad"]}: ${subtotal}")
      print("------------------")

def vaciar_carrito(carr_prod: list, op3: str):
    if not carr_prod:
        print("El carro esta vacio")
    elif op3 == "SI":
      carr_prod.clear()
      print("Carrito a sido eliminado")
    else:
        print("Opcion incorrecta")      