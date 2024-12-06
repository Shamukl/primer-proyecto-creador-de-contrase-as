import string
import random

longitud = int(input("inrese el tamaño de la cntraseña: "))

caracteres = string.ascii_letters + string.digits + string.punctuation

contraseña = "".join(random.choice(caracteres) for i in range(longitud))

print("la contraseña generada es: " + contraseña )