players = ["charly", "juan", "iancarlo", 'lisandro']
print("Lista original: ", players)

# Slicing
print(players[0:2]) # ["charly", "juan"]

# El slicing me permite trabajar con un grupo
# especifico de una lista: al resultado se le conoce como
# "un selice."

print("1:4 ", players[1:4]) # ["juan", "iancarlo", 'lisandro']
print(":3", players[:3]) # ['charly', 'juan', 'iancarlo']
print("", players[2:]) # ['iancarlo', 'lisandro']
print("[-3:]", players[-3:]) # ['juan', 'iancarlo', 'lisandro']

# players = ["charly", "juan", "iancarlo", 'lisandro']
# Casos especiales de slicing
print(players[1:6]) # ['juan', 'iancarlo', 'lisandro']
print(players[6:1])
print(players[:0])

# Looping through a slice3
print("Looping through a slice")
students = ["charly", "juan", "iancarlo", 'lisandro']

# Slicing [::]
for student in students[2:4]:
    print(f"El estudiante {student}, va a pasar la materia.")

print(students)


# Como podemos copiar una lista?
my_food = ["pizza", "tacos", 'flautas']
my_friend_food = my_food # Manera erronea de copiar una lista

# Tres maneras de copiar una lista
# metodo 1 - utilizando slicing
my_friend_food_2 = my_food[:]
# metodo 2 - utilizando el metodo de las listas .copy()
my_friend_food_3 = my_food.copy()
# metodo 3 - utilizando el metodo build-in list()
my_friend_food_4 = list(my_food)