import random

print("=== SIMULADOR DE LANZAMIENTO DE DADO ===")
print("Este programa cuenta cuántos tiros son PARES y cuántos IMPARES")
print()

# Solicitar al usuario el número de lanzamientos
num_lanzamientos = int(input("¿Cuántos lanzamientos deseas realizar? "))
print()

# Contadores para pares e impares
contador_pares = 0
contador_impares = 0

# Realizar los lanzamientos
print(f"Lanzando el dado {num_lanzamientos} veces...")
print()

for i in range(num_lanzamientos):
    # Generar número aleatorio entre 1 y 6
    resultado = random.randint(1, 6)
    
    # Mostrar el resultado del lanzamiento
    print(f"Lanzamiento {i + 1}: salió {resultado}", end=" - ")
    
    # Verificar si el número es par o impar
    if resultado % 2 == 0:
        # El número es PAR (2, 4, 6)
        contador_pares = contador_pares + 1
        print("PAR")
    else:
        # El número es IMPAR (1, 3, 5)
        contador_impares = contador_impares + 1
        print("IMPAR")

# Mostrar los resultados finales
print()
print("=== RESULTADOS FINALES ===")
print()
print(f"Total de lanzamientos: {num_lanzamientos}")
print(f"Tiros PARES: {contador_pares}")
print(f"Tiros IMPARES: {contador_impares}")
print()

# Calcular porcentajes (opcional, pero se ve bien)
porcentaje_pares = (contador_pares * 100) / num_lanzamientos
porcentaje_impares = (contador_impares * 100) / num_lanzamientos

print(f"Porcentaje de PARES: {porcentaje_pares:.2f}%")
print(f"Porcentaje de IMPARES: {porcentaje_impares:.2f}%")
print()
