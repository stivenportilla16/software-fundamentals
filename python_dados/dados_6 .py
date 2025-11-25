import random

# Variables para guardar los resultados
total_tiros = 0
suma_total = 0
total_pares = 0
total_impares = 0

print("¡Bienvenido al juego de lanzar dados!")
print("-" * 40)

# Bucle principal del juego
continuar = "si"

while continuar.lower() == "si" or continuar.lower() == "s":
    # Lanzar el dado (número aleatorio entre 1 y 6)
    resultado = random.randint(1, 6)
    
    print(f"\n Lanzaste el dado y sacaste: {resultado}")
    
    # Actualizar contadores
    total_tiros = total_tiros + 1
    suma_total = suma_total + resultado
    
    # Verificar si es par o impar
    if resultado % 2 == 0:
        total_pares = total_pares + 1
    else:
        total_impares = total_impares + 1
    
    # Preguntar si quiere seguir jugando
    continuar = input("\n¿Quieres lanzar el dado otra vez? (si/no): ")

# Mostrar el reporte final
print("\n" + "=" * 40)
print(" REPORTE FINAL")
print("=" * 40)
print(f"Total de tiros efectuados: {total_tiros}")
print(f"Suma total de los tiros: {suma_total}")
print(f"Total de números pares: {total_pares}")
print(f"Total de números impares: {total_impares}")
print("=" * 40)
print("\n¡Gracias por jugar!")