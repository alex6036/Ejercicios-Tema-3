class Polinomio:
    def __init__(self, coeficientes):
        """
        Inicializa un polinomio con una lista de coeficientes.
        Parametros:
        - coeficientes: lista de coeficientes [a0, a1, ..., an] para a0 + a1*x + ... + an*x^n
        """
        # Eliminar ceros finales para normalizar el polinomio
        while len(coeficientes) > 1 and coeficientes[-1] == 0:
            coeficientes.pop()
        self.coeficientes = coeficientes

    def grado(self):
        """
        Devuelve el grado del polinomio.
        """
        if not self.coeficientes or all(coef == 0 for coef in self.coeficientes):
            return -1  # Polinomio nulo
        return len(self.coeficientes) - 1

    def __str__(self):
        """
        Representación en cadena del polinomio.
        """
        if not self.coeficientes or all(coef == 0 for coef in self.coeficientes):
            return "0"
        
        terminos = []
        for i, coef in enumerate(self.coeficientes):
            if coef == 0:
                continue
            if i == 0:
                terminos.append(f"{coef}")
            elif i == 1:
                if coef == 1:
                    terminos.append("x")
                elif coef == -1:
                    terminos.append("-x")
                else:
                    terminos.append(f"{coef}x")
            else:
                if coef == 1:
                    terminos.append(f"x^{i}")
                elif coef == -1:
                    terminos.append(f"-x^{i}")
                else:
                    terminos.append(f"{coef}x^{i}")
        
        # Unir términos con signos
        resultado = ""
        for i, termino in enumerate(terminos):
            if i == 0:
                resultado += termino
            else:
                if termino.startswith("-"):
                    resultado += termino
                else:
                    resultado += f"+{termino}"
        return resultado if resultado else "0"

    def restar(self, otro):
        """
        Resta otro polinomio de este polinomio.
        Devuelve un nuevo polinomio.
        """
        max_len = max(len(self.coeficientes), len(otro.coeficientes))
        coef1 = self.coeficientes + [0] * (max_len - len(self.coeficientes))
        coef2 = otro.coeficientes + [0] * (max_len - len(otro.coeficientes))
        resultado = [coef1[i] - coef2[i] for i in range(max_len)]
        return Polinomio(resultado)

    def dividir(self, otro):
        """
        Divide este polinomio entre otro polinomio.
        Devuelve el cociente y el resto como una tupla (cociente, resto).
        """
        if otro.grado() < 0 or all(coef == 0 for coef in otro.coeficientes):
            raise ValueError("No se puede dividir por un polinomio nulo")

        dividendo = self.coeficientes[:]
        divisor = otro.coeficientes[:]
        cociente = []
        grado_dividendo = self.grado()
        grado_divisor = otro.grado()

        while grado_dividendo >= grado_divisor:
            coef = dividendo[grado_dividendo] / divisor[grado_divisor]
            grado = grado_dividendo - grado_divisor
            cociente.extend([0] * (grado - len(cociente) + 1))
            cociente[grado] = coef
            for i in range(len(divisor)):
                dividendo[grado_dividendo - grado_divisor + i] -= coef * divisor[i]
            while grado_dividendo >= 0 and dividendo[grado_dividendo] == 0:
                grado_dividendo -= 1
                dividendo.pop() if dividendo else None

        resto = Polinomio(dividendo if dividendo else [0])
        return Polinomio(cociente), resto

    def eliminar_termino(self, grado):
        """
        Elimina el término de un grado específico.
        Devuelve un nuevo polinomio.
        """
        nuevos_coeficientes = self.coeficientes[:]
        if 0 <= grado < len(nuevos_coeficientes):
            nuevos_coeficientes[grado] = 0
        return Polinomio(nuevos_coeficientes)

    def existe_termino(self, grado):
        """
        Determina si existe un término de un grado específico con coeficiente no nulo.
        """
        if grado < 0 or grado >= len(self.coeficientes):
            return False
        return self.coeficientes[grado] != 0