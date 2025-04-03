from polinomio import Polinomio

def main():
    # Definir dos polinomios
    p = Polinomio([1, 1, 2, 3])  # 3x^3 + 2x^2 + x + 1
    q = Polinomio([1, 2])        # 2x + 1

    print(f"Polinomio P(x): {p}")
    print(f"Polinomio Q(x): {q}")
    print()

    # 1. Restar dos polinomios
    resta = p.restar(q)
    print("Resta P(x) - Q(x):")
    print(resta)
    print()

    # 2. Dividir dos polinomios
    cociente, resto = p.dividir(q)
    print("División P(x) / Q(x):")
    print(f"Cociente: {cociente}")
    print(f"Resto: {resto}")
    print()

    # 3. Eliminar un término (por ejemplo, el término de grado 2)
    p_sin_grado_2 = p.eliminar_termino(2)
    print("P(x) sin el término de grado 2:")
    print(p_sin_grado_2)
    print()

    # 4. Determinar si un término específico existe
    grado = 2
    existe = p.existe_termino(grado)
    print(f"¿Existe un término de grado {grado} en P(x)? {existe}")
    grado = 4
    existe = p.existe_termino(grado)
    print(f"¿Existe un término de grado {grado} en P(x)? {existe}")

if __name__ == "__main__":
    main()