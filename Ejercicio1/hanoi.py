# hanoi.py
class TorreHanoi:
    """Clase que resuelve el puzzle de la Torre de Hanói."""
    
    def __init__(self, n):
        """
        Inicializa el puzzle con n piedras.
        Parametros:
        - n: número de piedras (discos)
        """
        self.num_piedras = n
        self.movimientos = 0  # Contador de movimientos

    def mover(self, n, origen, destino, auxiliar):
        """
        Resuelve la Torre de Hanói con n discos de forma recursiva.
        Parametros:
        - n: número de discos a mover
        - origen: columna de origen (ej. 'A')
        - destino: columna de destino (ej. 'C')
        - auxiliar: columna auxiliar (ej. 'B')
        """
        if n == 1:
            self.movimientos += 1
            print(f"Mover piedra 1 de {origen} a {destino}")
            return
        # Paso 1: Mover n-1 discos de origen a auxiliar
        self.mover(n - 1, origen, auxiliar, destino)
        # Paso 2: Mover el disco n de origen a destino
        self.movimientos += 1
        print(f"Mover piedra {n} de {origen} a {destino}")
        # Paso 3: Mover n-1 discos de auxiliar a destino
        self.mover(n - 1, auxiliar, destino, origen)

    def resolver_piramide(self):
        """
        Resuelve el puzzle de la pirámide con el número de piedras especificado.
        """
        total_movimientos = 2 ** self.num_piedras - 1
        print(f"Resolviendo el puzzle de la pirámide con {self.num_piedras} piedras...")
        print(f"Total de movimientos necesarios: {total_movimientos}")
        print("Iniciando los movimientos:")
        self.mover(self.num_piedras, "A", "C", "B")
        print(f"Puzzle resuelto en {self.movimientos} movimientos.")