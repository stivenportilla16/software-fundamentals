Funcion contar_pares_impares
    Definir veces, numero, i, pares, impares Como Entero
    
    Escribir "Cuantos lanzamientos vas a efectuar?"
    Leer veces
    
    pares <- 0
    impares <- 0
    
    Para i <- 1 Hasta veces Hacer
        numero <- Aleatorio(1, 6)
        Escribir "Lanzamiento ", i, ": ", numero
        
        Si numero % 2 == 0 Entonces
            pares <- pares + 1
        SiNo
            impares <- impares + 1
        FinSi
    FinPara
    
    Escribir ""
    Escribir "Total de tiros PARES: ", pares
    Escribir "Total de tiros IMPARES: ", impares
FinFuncion

Algoritmo reto5
    contar_pares_impares
FinAlgoritmo