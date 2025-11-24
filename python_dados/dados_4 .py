
import random

print("=== SIMULADOR DE LANZAMIENTO DE DOS DADOS ===")
print("El programa lanzará dos dados hasta obtener un PAR de SEIS (6,6)")
print()

# Contador de intentos
intentos = 0

# Variable para controlar el ciclo
par_de_seis = False

# Lanzar los dados hasta obtener doble 6
while par_de_seis == False:
    # Incrementar el contador de intentos
    intentos = intentos + 1
    
    # Lanzar los dos dados
    dado1 = random.randint(1, 6)
    dado2 = random.randint(1, 6)
    
    # Mostrar el resultado del lanzamiento
    print(f"Intento {intentos}: Dado 1 = {dado1}, Dado 2 = {dado2}")
    
    # Verificar si obtuvimos un par de seis
    if dado1 == 6 and dado2 == 6:
        par_de_seis = True
        print()
        print("¡FELICIDADES! ¡Obtuviste un PAR de SEIS! ")
        print()

# Mostrar estadísticas finales
print("=== RESULTADOS FINALES ===")
print(f"Total de intentos necesarios: {intentos}")
print()