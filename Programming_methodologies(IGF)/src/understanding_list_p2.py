# Agregando elementos a una lista
motorcycles = ['honda', "mortalica", 'yamaha']
print(motorcycles) # ['honda', 'mortalica', 'yamaha']

# Metodo append - agrega elementos a la lista
motorcycles.append("kawasaki")
print(motorcycles) # ['honda', 'mortalica', 'yamaha', 'kawasaki']

"""

facilmente de manera dinamica
"""
motorcycles_2 = [] # Lista vacia
print(motorcycles_2)

motorcycle = "ducati"
motorcycles_2.append(motorcycle) # 1 elemento
motorcycles_2.append("yamaha") # 2 elemento
motorcycles_2.append("suzuki") # 3 elemento
print(motorcycles_2)
motorcycle = "charly"
print(motorcycles_2)
motorcycles_2.append(motorcycle)

# El metodod insert nos ayuda a  agregar elementos
# a una lista en un indice especifico
motorcycle_3 = ["honda", 'yamaha', "suzuki"]
print("\nLista Original")
print(motorcycles_3)
motorcycles_3.insert(0, "ducati")
print("lista despues del metodo insert")
print(motorcycles_3)

''

## Metodo .pop() Elimina el ultimo elemento de una lista,
# pero nos permite utilizar el elemento despues de eliminarlo.
motorcycles_4 = ['honda', 'suzuki', 'hd', 'mortalica']
print(motorcycles_4)
deleted_motorcycle = motorcycles_4.pop()
print(f"Tu motocicleta borrada es: {deleted_motorcycle}")
print(motorcycles_4)

# Se puede utilizar tambien para eliminar un elemento especifico.
motorcycles_5 = ['honda', 'suzuki', 'hd', 'mortalica']
print(motorcycles_5)
motorcycles_5.pop(0)
print(motorcycles_5) # Lista sin honda

# Metodo .remove(), permite eliminar elementos por su valor.
print("\n\t Aqui aprendi a utilizar el metodo remove".upper())
motorcycles_6 = ['honda', 'yamaha', 'suzuki', 'ducati']
print(motorcycles_6)
motorcycles_6.remove("yamaha")
print(motorcycles_6)

# Ordenar listas
car = ['bmw', 'audi', 'toyota', 'subaru']
print(cars)
cars.sort() # Ordenar la lista de manera permanente
# Argumento opcional se sort (reverse=True)
print(cars)
# Tarea estudiar metodo de las listas reverse()
# Estudiar metodos build-in: sorted(), len()