class Matriz:
    def __init__(self, matriz):
        """
        Inicializa la matriz.
        Parametros:
        - matriz: lista de listas representando una matriz cuadrada
        """
        self.matriz = matriz
        self.n = len(matriz)  # Dimensión de la matriz (n x n)

    def obtener_submatriz(self, fila, columna):
        """
        Devuelve una submatriz eliminando la fila y columna especificadas.
        """
        return [
            [self.matriz[i][j] for j in range(self.n) if j != columna]
            for i in range(self.n) if i != fila
        ]

    def determinante_recursivo(self):
        """
        Calcula el determinante de la matriz usando el método recursivo (expansión de Laplace).
        """
        # Caso base: matriz 1x1
        if self.n == 1:
            return self.matriz[0][0]
        
        # Caso base: matriz 2x2
        if self.n == 2:
            return self.matriz[0][0] * self.matriz[1][1] - self.matriz[0][1] * self.matriz[1][0]
        
        # Expansión de Laplace por la primera fila
        det = 0
        for j in range(self.n):
            cofactor = self.matriz[0][j] * ((-1) ** j) * Matriz(self.obtener_submatriz(0, j)).determinante_recursivo()
            det += cofactor
        return det

    def determinante_iterativo(self):
        """
        Calcula el determinante de una matriz 3x3 usando el método iterativo (fórmula directa).
        """
        if self.n != 3:
            raise ValueError("El método iterativo está implementado solo para matrices 3x3.")
        
        a, b, c = self.matriz[0]
        d, e, f = self.matriz[1]
        g, h, i = self.matriz[2]
        
        # Fórmula: a(ei - fh) - b(di - fg) + c(dh - eg)
        det = (a * (e * i - f * h) -
               b * (d * i - f * g) +
               c * (d * h - e * g))
        return det

    def __str__(self):
        """Representación en cadena de la matriz."""
        return "\n".join([" ".join(map(str, fila)) for fila in self.matriz])