# Trabajando con listas
print("El dia de hoy voy a aprender a trabajar con listas")
# Lista de strings con nombres de magos
magicians = ['harry', 'ron', 'hermonie', 'snape']
print(magicians)

print(magicians[0], magicians[1], magicians[2], magicians[3])

# cilco for
for magician in magicians:
    print(magician)

# A esto se le conoce como looping
# for cat in cats:
# for dog in dogs:
# for item in items:

# Ahora vamos a imprimir un mensaje para cada mago
for magician in magicians:
    print(f"{magician.title()} ese fue un gran hechizo.")
    print(f"no puedo esperar a ver el siguiente hechizo, {magician.upper()}")
print("Gracias a todos. Fue un gran espectaculo")