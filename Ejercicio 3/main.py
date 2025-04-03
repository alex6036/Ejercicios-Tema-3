from nave import NaveEspacial
naves = [
    NaveEspacial("Cometa Veloz", 150.5, 10, 20),
    NaveEspacial("Titán del Cosmos", 300.0, 25, 50),
    NaveEspacial("GX-Alpha", 120.0, 8, 10),
    NaveEspacial("Estrella Fugaz", 200.0, 15, 30),
    NaveEspacial("GX-Beta", 180.0, 12, 15),
    NaveEspacial("Nebulosa", 250.0, 20, 40),
    NaveEspacial("Aurora", 90.0, 5, 5),
    NaveEspacial("GX-Zeta", 160.0, 10, 8),
    NaveEspacial("Centella", 110.0, 7, 6),
    NaveEspacial("Galaxia", 280.0, 22, 45),
]
def main():
    # Mostrar la lista original
    print("Lista original de naves:")
    for nave in naves:
        print(nave)
    print()

    # 1. Ordenar por nombre (ascendente) y por longitud (descendente)
    naves_ordenadas = sorted(naves, key=lambda x: (x.nombre, -x.longitud))
    print("Naves ordenadas por nombre (ascendente) y longitud (descendente):")
    for nave in naves_ordenadas:
        print(nave)
    print()

    # 2. Mostrar información de "Cometa Veloz" y "Titán del Cosmos"
    print("Información de 'Cometa Veloz' y 'Titán del Cosmos':")
    for nave in naves:
        if nave.nombre in ["Cometa Veloz", "Titán del Cosmos"]:
            print(nave)
    print()

    # 3. Determinar las cinco naves con mayor cantidad de pasajeros
    naves_por_pasajeros = sorted(naves, key=lambda x: x.pasajeros, reverse=True)[:5]
    print("Las cinco naves con mayor cantidad de pasajeros:")
    for nave in naves_por_pasajeros:
        print(nave)
    print()

    # 4. Nave con mayor cantidad de tripulación
    nave_mayor_tripulacion = max(naves, key=lambda x: x.tripulantes)
    print("Nave que requiere la mayor cantidad de tripulación:")
    print(nave_mayor_tripulacion)
    print()

    # 5. Naves cuyo nombre comienza con "GX"
    naves_gx = [nave for nave in naves if nave.nombre.startswith("GX")]
    print("Naves cuyo nombre comienza con 'GX':")
    for nave in naves_gx:
        print(nave)
    print()

    # 6. Naves que pueden llevar seis o más pasajeros
    naves_seis_pasajeros = [nave for nave in naves if nave.pasajeros >= 6]
    print("Naves que pueden llevar seis o más pasajeros:")
    for nave in naves_seis_pasajeros:
        print(nave)
    print()

    # 7. Nave más pequeña y más grande (por longitud)
    nave_mas_pequena = min(naves, key=lambda x: x.longitud)
    nave_mas_grande = max(naves, key=lambda x: x.longitud)
    print("Nave más pequeña:")
    print(nave_mas_pequena)
    print("Nave más grande:")
    print(nave_mas_grande)

if __name__ == "__main__":
    main()