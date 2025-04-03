# main.py
from hanoi import TorreHanoi
def main():
    # Prueba con 10 piedras
    print("Prueba con 1 piedra:")
    juego_uno = TorreHanoi(10)
    juego_uno.resolver_piramide()

    # Solicitar al usuario el número de piedras
    numero = int(input("Ingrese el número de piedras (1-74): "))
    if 1 <= numero <= 74:
        juego = TorreHanoi(numero)
        juego.resolver_piramide()
    else:
        print("Número de piedras fuera del rango permitido (1-74).")
if __name__ == "__main__":
    main()
