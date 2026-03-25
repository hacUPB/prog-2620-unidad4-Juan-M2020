from random import randint
aviones = ["A320" , "A350" , "A380" , "A320" , "A220" ,"B787" ,"B747" ,"Antonov" ]

pasajero  = []

aviones.insert(1, "A220")

aviones.remove("B787")

aviones.pop(6)

for i in range (7):
    dato = randint (70,150)
    pasajero.append(dato)

print(pasajero)

mayor = max(pasajero)
veces = pasajero.count(mayor)

if veces > 1:
    aviones = []
    for i in range(len(pasajero)):
        if pasajero[i] == mayor:
           aviones.append(i)
    print("Ventas mayores en: ")
    for mes in aviones :
        print(f" {pasajeros[pasajero]}")

else:
    mes = pasajero.index(mayor)
    print(f"Mas lleno {pasajeros[pasajero]}")

print(aviones)