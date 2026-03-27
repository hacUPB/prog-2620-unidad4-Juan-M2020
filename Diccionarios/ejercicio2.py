# Diccionario con diferentes tipos de datos como valores
vuelo = {
    "aerolinea": "Avianca",
    "vuelo": "AV123",
    "origen": "BOG",
    "destino": "MED",
}
# crear un nuevo par clave:valor
ciudad_llegada = vuelo.get("destino", "No disponible")
print(ciudad_llegada)

#modificar valores
vuelo["destino"] =  "CLO"
print(f"La ciudad de destino es: {vuelo["destino"]}")


# crear un nuevo par clave:valor
vuelo["estado"] = "En el aire"
print(f"El avion esta en : {vuelo["estado"]}")

# Método get() (devuelve None o un valor por defecto si la clave no existe)
piloto = vuelo.get("piloto", "piloto no asignado")
print(f"pilotos de este avion : {piloto}")

