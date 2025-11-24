import random

# Solicitar al usuario cuántas veces quiere lanzar el dado
print("=== SIMULADOR DE LANZAMIENTO DE DADOS ===")
print()
num_lanzamientos = int(input("¿Cuántas veces deseas lanzar el dado? "))
print()

# Crear contadores para cada número del dado (1 al 6)
contador_1 = 0
contador_2 = 0
contador_3 = 0
contador_4 = 0
contador_5 = 0
contador_6 = 0

# Realizar los lanzamientos
print(f"Lanzando el dado {num_lanzamientos} veces...")
print()

for i in range(num_lanzamientos):
    # Generar un número aleatorio entre 1 y 6
    resultado = random.randint(1, 6)
    
    # Contar cuántas veces sale cada número
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

# Mostrar los resultados
print("=== RESULTADOS ===")
print()
print(f"El número 1 salió: {contador_1} veces")
print(f"El número 2 salió: {contador_2} veces")
print(f"El número 3 salió: {contador_3} veces")
print(f"El número 4 salió: {contador_4} veces")
print(f"El número 5 salió: {contador_5} veces")
print(f"El número 6 salió: {contador_6} veces")
print()
print(f"Total de lanzamientos: {num_lanzamientos}")
print()
print("¡Gracias por usar el simulador!")