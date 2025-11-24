def reto2():
    print("\n=== RETO 2: Suma de Lanzamientos ===")
    
    veces = int(input("Cuantas veces quieres lanzar el dado? "))
    suma = 0
    
    for i in range(veces):
        numero = random.randint(1, 6)
        print(f"Lanzamiento {i+1}: {numero}")
        suma = suma + numero
    
    print(f"\nLa suma total es: {suma}")
