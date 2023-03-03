
# Desarrolle un algoritmo para hallar el área de un circulo, 
# el usuario debe ingresar el radio

import math
print("ingrese el radio del circulo: ")
r = float(input()) # el  radio
a = math.pi * (r *r)
print("el area del circulo es: ",round(a, 2))