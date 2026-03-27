asientos = [
    ["O", "O", "X", "O"], 
    ["O", "X", "O", "O"], 
    ["O", "O", "O", "X"]   
]

# Mostrar los asientos
for i in range(3):          
    for j in range(4):      
       print(asientos[i][j])
    

fila = int(input("Ingrese la fila del asiento: "))
columna= int(input("Ingrese la columna del asiento: "))

if asientos[fila][columna] == "O":
    print("El asiento está libre")
else:
    print("El asiento está ocupado")
