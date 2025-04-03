from matriz import Matriz
# Prueba del cálculo del determinante
def main():
    # Matriz de ejemplo
    matriz_ejemplo = [
        [3, 1, 33],
        [4, 2, 62],
        [5, 83, 93]
    ]
    
    # Crear una instancia de la clase Matriz
    m = Matriz(matriz_ejemplo)
    
    print("Matriz:")
    print(m)
    print()
    
    # Calcular el determinante con el método recursivo
    det_recursivo = m.determinante_recursivo()
    print(f"Determinante (método recursivo): {det_recursivo}")
    
    # Calcular el determinante con el método iterativo
    det_iterativo = m.determinante_iterativo()
    print(f"Determinante (método iterativo): {det_iterativo}")

if __name__ == "__main__":
    main()