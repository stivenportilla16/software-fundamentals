def reto5():
    print("\n=== RETO 5: Conteo de Pares e Impares ===")
    
    veces = int(input("Cuantos lanzamientos vas a efectuar? "))
    
    pares = 0
    impares = 0
    
    for i in range(veces):
        numero = random.randint(1, 6)
        print(f"Lanzamiento {i+1}: {numero}")
        
        if numero % 2 == 0:
            pares = pares + 1
        else:
            impares = impares + 1
    
    print(f"\nTotal de tiros PARES: {pares}")
    print(f"Total de tiros IMPARES: {impares}")

