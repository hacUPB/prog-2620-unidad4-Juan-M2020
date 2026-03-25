#crea una lista con 100 numeros aleatorios entre 100 y 200
import random

print(random.randint(100,200))

lista = []
for i in range(100):
    lista.append(random.randint(100, 200))

print (lista)
mayor = max(lista)
print (f"el numero mas grande de la lista {mayor}")

# Implementar la funcion max usando un bucle

indice = 0
may = lista[0]
while indice < 99:
    if may < lista[indice +1]:
        may = lista[indice +1]
        indice += 1

print(f"El mayor calculado a mano es: {may}")

#calcular el menor de todos

indice = 0
min = lista[0]
while indice < 99:
    if min < lista[indice -1]:
        min = lista[indice -1]
        indice -= 1

print(f"El mayor calculado a mano es: {min}")