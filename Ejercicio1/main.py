# main.py
from hanoi import TorreHanoi

if __name__ == "__main__":
    # Prueba con 10 piedra
    print("Prueba con 1 piedra:")
    juego_uno = TorreHanoi(10)
    juego_uno.resolver_piramide()
    numero = int(input("Ingrese el número de piedras (1-74): "))
    if 1 <= numero <= 74:
        juego = TorreHanoi(numero)
        juego.resolver_piramide()
    else:
        print("Número de piedras fuera del rango permitido (1-74).")
