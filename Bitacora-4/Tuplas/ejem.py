# Tupla vacía
coordenada = ()

# Tupla con elementos
coordenada = (33.9425, -118.4081)  # LAX (Aeropuerto de Los Ángeles)

# Tupla con un solo elemento (requiere coma al final)
rumbo = (270,)  # Sin la coma sería tratado como un entero entre paréntesis

# Tupla sin paréntesis (empaquetado implícito)
avion_info = "Boeing 787", "Dreamliner", 2009, 242

print(f"coordenadas: {coordenada[0]}")




fleet_data = [
    ("Airbus A320", 35.80, 37.57, 78000, 871),
    ("Boeing 737-800", 35.79, 39.47, 79010, 853),
    ("Embraer E190", 28.72, 36.24, 51800, 871),
    ("Bombardier CRJ-900", 24.85, 36.40, 38330, 870)
]


print(fleet_data[2][0])