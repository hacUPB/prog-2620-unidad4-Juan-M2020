print("✈️  Flota de Aeronaves ✈️")

# Lista de aeronaves
flota = []

for i in range(3):

    print(f"\nAeronave #{i+1}")
    matricula = input("Ingrese la Matricula de la Aeronave: ")
    modelo = input("Ingrese el Modelo de la Aeronave: ")
    horas = float(input("Ingrese las Horas de uso de la Aeronave: "))

    aeronave = {
        "matricula": matricula,
        "modelo": modelo,
        "horas": horas,
        "componentes": {}  # diccionario de componentes
    }

    n_componentes = int(input("¿Cuántos componentes desea registrar?: "))

    for j in range(n_componentes):
        print(f"\nComponente #{j+1}")
        nombre = input("Ingrese el Nombre del componente: ")
        horas_uso = float(input("Ingrese las horas de uso: "))
        h_limite = float(input("Ingrese las horas limite del componente: "))

        # Guardar cada componente usando el nombre como clave
        aeronave["componentes"][nombre] = {
            "horas_uso": horas_uso,
            "limite": h_limite
        }

    flota.append(aeronave)


# ============================
# REPORTE DE MANTENIMIENTO
# ============================

print("\n⚙️  REPORTE FINAL DE MANTENIMIENTO ⚙️")

for aeronave in flota:
    print(f"\nAeronave: {aeronave['matricula']} - {aeronave['modelo']}")

    for nombre, datos in aeronave["componentes"].items():
        if datos["horas_uso"] >= datos["limite"]:
            print(f"⚠️ {nombre} REQUIERE mantenimiento")
        else:
            print(f"✅ {nombre} en buen estado")


while True:
    print("\n=== MENÚ DE MODIFICACIONES ===")
    print("1. Agregar nueva aeronave")
    print("2. Eliminar aeronave")
    print("3. Agregar componente a una aeronave")
    print("4. Eliminar componente de una aeronave")
    print("5. Ver reporte de mantenimiento")
    print("6. Salir")

    opcion = input("Seleccione una opción: ")

    # AGREGAR AERONAVE
    if opcion == "1":
        matricula = input("Ingrese la Matricula: ")
        modelo = input("Ingrese el Modelo: ")
        horas = float(input("Horas de vuelo: "))

        nueva = {
            "matricula": matricula,
            "modelo": modelo,
            "horas": horas,
            "componentes": {}
        }

        flota.append(nueva)
        print("Aeronave agregada correctamente.")

    # ELIMINAR AERONAVE
    elif opcion == "2":
        mat = input("Ingrese la matrícula a eliminar: ")

        for aeronave in flota:
            if aeronave["matricula"] == mat:
                flota.remove(aeronave)
                print("Aeronave eliminada.")
                break
        else:
            print("No se encontró la aeronave.")

    # AGREGAR COMPONENTE
    elif opcion == "3":
        mat = input("Ingrese la matrícula de la aeronave: ")

        for aeronave in flota:
            if aeronave["matricula"] == mat:

                nombre = input("Nombre del componente: ")
                horas_uso = float(input("Horas de uso: "))
                limite = float(input("Límite: "))

                aeronave["componentes"][nombre] = {
                    "horas_uso": horas_uso,
                    "limite": limite
                }

                print("Componente agregado.")
                break
        else:
            print("Aeronave no encontrada.")

    # ELIMINAR COMPONENTE
    elif opcion == "4":
        mat = input("Ingrese la matrícula: ")

        for aeronave in flota:
            if aeronave["matricula"] == mat:

                nombre = input("Nombre del componente a eliminar: ")

                if nombre in aeronave["componentes"]:
                    del aeronave["componentes"][nombre]
                    print("Componente eliminado.")
                else:
                    print("Componente no encontrado.")
                break
        else:
            print("Aeronave no encontrada.")

    # REPORTE
    elif opcion == "5":
        print("\n⚙️ REPORTE DE MANTENIMIENTO ⚙️")

        for aeronave in flota:
            print(f"\nAeronave: {aeronave['matricula']} - {aeronave['modelo']}")

            for nombre, datos in aeronave["componentes"].items():
                if datos["horas_uso"] >= datos["limite"]:
                    print(f"⚠️ {nombre} REQUIERE mantenimiento")
                else:
                    print(f"✅ {nombre} en buen estado")

    # SALIR
    elif opcion == "6":
        print("Saliendo del sistema...")
        break

    else:
        print("Opción inválida.")
