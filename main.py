# main.py
from hanoi import TorreHanoi

# Prueba con 3 piedras
print("Prueba con 3 piedras:")
juego_pequeno = TorreHanoi(3)
juego_pequeno.resolver_piramide()

# Para el caso completo de 74 piedras (comentado por practicidad)
# print("\nCaso completo con 74 piedras:")
# juego_grande = TorreHanoi(74)
# juego_grande.resolver_piramide()