# Diccionario vacío
aeronave = {}

# Diccionario con elementos
aeronave = {
    "modelo": "Boeing 787-9",
    "envergadura": 60.17,  # metros
    "longitud": 62.81,     # metros
    "mtow": 254000,        # kg
    "velocidad_max": 954   # km/h
}

# Diccionario con diferentes tipos de datos como valores
vuelo = {
    "numero": "AA123",
    "origen": "KLAX",
    "destino": "KJFK",
    "distancia": 3983,
    "a_tiempo": True,
    "tripulacion": ["Capitán Smith", "F/O Johnson", "F/E Williams"]
}

# Creación con dict()
motor = dict(fabricante="GE", modelo="GE9X", empuje=470, bypass_ratio=10)



asignaturas = {
    1 : "Matematicas" ,
    2 : "Ciencias"

}

# Acceso a valores
print(vuelo["tripulacion"])  

#modificar valores
vuelo["distancia"] =  4000
print(vuelo["distancia"])

# crear un nuevo par clave:valor
asignaturas[9] = "programacion"
print(asignaturas[9])


# Eliminar par clave-valor
del aeronave["velocidad_max"]

# Comprobar existencia de clave
if "alcance" in aeronave:
    print(f"El alcance es {aeronave['alcance']} km")

else:
    print("La clave no existe ")

# Método get() (devuelve None o un valor por defecto si la clave no existe)
velocidad = aeronave.get("velocidad_max", "No disponible")
print(velocidad)