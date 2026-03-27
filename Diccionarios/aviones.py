# Base de datos de flota
flota = {
    "N123AA": {
        "modelo": "Boeing 787-9",
        "año": 2018,
        "horas_vuelo": 12500,
        "ciclos": 1350,
        "estado": "En servicio",
        "base": "DFW",
        "proxima_revision": "2023-07-15"
    },
    "N456AA": {
        "modelo": "Boeing 777-300ER",
        "año": 2014,
        "horas_vuelo": 26800,
        "ciclos": 2940,
        "estado": "En mantenimiento",
        "base": "MIA",
        "proxima_revision": "2023-03-30"
    },
    "N789AA": {
        "modelo": "Airbus A321neo",
        "año": 2022,
        "horas_vuelo": 1200,
        "ciclos": 420,
        "estado": "En servicio",
        "base": "LAX",
        "proxima_revision": "2024-01-10"
    }
}

# Añadir nueva aeronave
placa = input("Ingrese la placa: ")
mod = input("ingrese el modelo: ")
añ = input("ingrese el año del avion: ")
hor = input("ingrese las horas de vuelo: ")
cic = input("ingrece los ciclos de vuelo: ")
est = input("ingrese el estado: ")
prox = input("ingrese la fecha de lo proxima revision: ")


temp = {}
temp["modelo"] = mod
temp["año"] = añ
temp["horas_vuelo"] = hor
temp["ciclos"] = cic
temp["estado"] = est
temp["proxima_revision"] = prox

 
flota[placa] = temp

# # Actualizar datos de mantenimiento
# flota["N456AA"]["estado"] = "En servicio"
# flota["N456AA"]["horas_vuelo"] += 12  # Después de un vuelo
# flota["N456AA"]["ciclos"] += 1

# Mostrar información detallada
for matricula, datos in flota.items():
    print(f"\\nAeronave: {matricula}")
    for clave, valor in datos.items():
        print(f"  {clave}: {valor}")




