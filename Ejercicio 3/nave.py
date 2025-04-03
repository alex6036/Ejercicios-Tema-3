class NaveEspacial:
    def __init__(self, nombre, longitud, tripulantes, pasajeros):
        """
        Inicializa una nave espacial.
        Parametros:
        - nombre: nombre de la nave (str)
        - longitud: longitud de la nave en metros (float)
        - tripulantes: cantidad de tripulantes (int)
        - pasajeros: cantidad de pasajeros (int)
        """
        self.nombre = nombre
        self.longitud = longitud
        self.tripulantes = tripulantes
        self.pasajeros = pasajeros

    def __str__(self):
        """Representación en cadena de la nave."""
        return (f"Nave: {self.nombre}, Longitud: {self.longitud}m, "
                f"Tripulantes: {self.tripulantes}, Pasajeros: {self.pasajeros}")