# Set vacío (requiere constructor set())
aeropuertos = set()

# Set con elementos
aeropuertos = {"KLAX", "KJFK", "KORD", "KDEN", "KATL"}

# Crear set a partir de otra colección
codigos_IATA = set(["LAX", "JFK", "ORD", "DEN", "ATL"])

# Set para eliminar duplicados
vuelos_diarios = set(["AA123", "DL456", "UA789", "AA123", "DL456"])
print(vuelos_diarios)  # {'AA123', 'DL456', 'UA789'} (elimina duplicados)