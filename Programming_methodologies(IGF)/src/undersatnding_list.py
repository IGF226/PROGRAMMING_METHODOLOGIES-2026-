"""
Las listas nos permiten almacenar infromacion en un lugar,
la cantidad que desee: ya sean pocos elementos 
o millones de elementos

Una lista es una coleccion de items (elementos) que tiene
un orden particular. Se pueden crear listas que incluyan








En Python, los corchetes [] indican una lista,
sus elementos se separan por comas.

Ejemplo:
"""
bycicles = ['trek', 'canondale', 'redline', 'specialized', "Razor"]
print(bycicles)

# Como podemos acceder a los elementos de una lista?
 
 """
 Las listas son colecciones ordenadas. Se pueden acceder
 a un elemento de una lista diciendole a Python la
 posicion o indice de un elemento deseado.

 Para obtener el valor deseado, se debe escribir
 el nombre de la lista, seguido del indice del elemento
 entre corchetes.
 """
 print(bycicles[0], bycicles[1], bycicles[2])

 print(bycicles[0].upper())

#Los indices comienzan en 0, no en 1
#bycicles = ['trek', 'cannondale', 'redline', 'specialized']
#Ejemplo:
print(bycicles[1]) #cannondale
print(bycicles[3]) #specialized

#Accediendo al ulrimo elemento de una lista
print(bycicles[-1])
print(bycicles[-2])

#Utilizando valores individuales de una lista
message = f"My first bycicle was a {bycicles[-1].upper()}"
print(message)