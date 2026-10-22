"""
    TUPLAS

    Las tuplas son listas de elementos que no cambias de tamano.
    Las tuplas son listas inmutables.


    Se utilizan los parentesis () para definir la tupla.

    Ejemplo:

        Si tenemos un rectangulo (largo, ancho) que siempre va
        a tener cierto tamano, podemos asegurar que sus dimensiones
        no va a cambiar si colocamos sus valores en una tupla.
    
"""
dimensions = (200, 50) # 200 de largo x 50 de ancho
print(dimensions)

# Vamos a imprimir elementos de una tupla
# Se realiza de la misma forma que con una
print(dimensions[0])
print(dimensions[1])
print(dir(dimensions))

# vamos a modificar el valor de una lista
names = ["carlos", "charly", "juan", "wendy"]
print(names)
names [0] = "mercury"
names [1] = "mercury"
names [2] = "mercury"
print(names)


dimensions[0] = 500 # Esta operacion no esta permitida

# Looping through a tuple
for dimension in dimensions:
    print(dimension)

"""
    No podemos modificar una tupla,
    lo que si podemos hacer es cambiar
    la asignacion de una variable que 
    almacena una tupla.
"""
dimensions = (500, 1000, 20)
print("tupla original:", dimensions)

# Lista
dimensions_2 = [200, 50]
print(dir(dimensions_2))

# string
name = "Israel"
print(dir(name))

#
# age = 17
# print (dir(age))

# Tipos de datos Booleanos
answer = True
print(answer)
# print(dir(answer))
