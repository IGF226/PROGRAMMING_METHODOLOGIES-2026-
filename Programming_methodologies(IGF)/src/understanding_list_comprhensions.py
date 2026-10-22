"""
Una lista comprehension combina
el for loop y la reacion de nuevos elementos
en una sola linea y automaticamente agrega
cada nuevo elemento a  la lista, es decir,
sin utilizar el metodo append.
"""
squares = [value**2 for value in range(0,11)]
print(squares)