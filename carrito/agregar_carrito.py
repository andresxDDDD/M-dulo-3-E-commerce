def agrega_producto(productos: list,id: int,cantidad:int):
      carr_prod=[]
      for i in productos:
         if id == i["id"]:
            carr_prod.append({
                "id": id,
                "cantidad": cantidad,
                 })
   
      print(carr_prod)        