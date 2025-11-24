# Programa: Validador de paridad y signo
# Descripción: Determina si un número es par/impar y positivo/negativo

# Solicitar un número entero al usuario
print("Ingrese un número entero (positivo o negativo):")
numero = int(input())

# Validar si el número es positivo o negativo
if numero > 0:
    # Número positivo
    if numero % 2 == 0:
        print(f"El número {numero} es PAR POSITIVO")
    else:
        print(f"El número {numero} es IMPAR POSITIVO")
        
elif numero < 0:
    # Número negativo
    if numero % 2 == 0:
        print(f"El número {numero} es PAR NEGATIVO")
    else:
        print(f"El número {numero} es IMPAR NEGATIVO")
        
else:
    # Número es cero
    print(f"El número {numero} es CERO (par y neutro)")