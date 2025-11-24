import random

print("=== SIMULADOR DE LANZAMIENTO DE DADO ===")
print("Lanza el dado y decide si quieres continuar")
print()

# Contadores para cada número del dado (1 al 6)
contador_1 = 0
contador_2 = 0
contador_3 = 0
contador_4 = 0
contador_5 = 0
contador_6 = 0

# Contador total de lanzamientos
total_lanzamientos = 0

# Variable para controlar si el jugador quiere seguir
continuar = "si"

# Ciclo principal del juego
while continuar == "si" or continuar == "s":
    # Lanzar el dado
    resultado = random.randint(1, 6)
    total_lanzamientos = total_lanzamientos + 1
    
    # Mostrar el resultado
    print(f"🎲 Lanzamiento #{total_lanzamientos}: ¡Salió {resultado}!")
    
    # Contar el resultado
    if resultado == 1:
        contador_1 = contador_1 + 1
    elif resultado == 2:
        contador_2 = contador_2 + 1
    elif resultado == 3:
        contador_3 = contador_3 + 1
    elif resultado == 4:
        contador_4 = contador_4 + 1
    elif resultado == 5:
        contador_5 = contador_5 + 1
    elif resultado == 6:
        contador_6 = contador_6 + 1
    
    # Preguntar si quiere continuar
    print()
    continuar = input("¿Deseas lanzar de nuevo? (si/no): ").lower()
    print()

# Mostrar el reporte final
print("=" * 50)
print("=== REPORTE FINAL ===")
print("=" * 50)
print()
print(f"Total de lanzamientos realizados: {total_lanzamientos}")
print()
print("Frecuencia de cada número:")
print(f"  Número 1: {contador_1} veces")
print(f"  Número 2: {contador_2} veces")
print(f"  Número 3: {contador_3} veces")
print(f"  Número 4: {contador_4} veces")
print(f"  Número 5: {contador_5} veces")
print(f"  Número 6: {contador_6} veces")
print()

# Encontrar el número que más salió
numero_mas_frecuente = 0
veces_mas_frecuente = 0

if contador_1 > veces_mas_frecuente:
    numero_mas_frecuente = 1
    veces_mas_frecuente = contador_1

if contador_2 > veces_mas_frecuente:
    numero_mas_frecuente = 2
    veces_mas_frecuente = contador_2

if contador_3 > veces_mas_frecuente:
    numero_mas_frecuente = 3
    veces_mas_frecuente = contador_3

if contador_4 > veces_mas_frecuente:
    numero_mas_frecuente = 4
    veces_mas_frecuente = contador_4

if contador_5 > veces_mas_frecuente:
    numero_mas_frecuente = 5
    veces_mas_frecuente = contador_5

if contador_6 > veces_mas_frecuente:
    numero_mas_frecuente = 6
    veces_mas_frecuente = contador_6

print(f"Número que más salió: {numero_mas_frecuente} ({veces_mas_frecuente} veces)")
print()