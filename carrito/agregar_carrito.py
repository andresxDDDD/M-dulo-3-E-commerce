def agrega_producto(productos: list,carr_prod,id: int,cantidad:int):
      
      for i in productos:
         if i["id"]==id:
            carro={
                "id": id,
                "cantidad": cantidad,
                 }
            carr_prod.append(carro)
   
      return(carr_prod)   



               