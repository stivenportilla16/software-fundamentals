Funcion contar_numeros
    Definir veces, numero, i Como Entero
    Definir cont1, cont2, cont3, cont4, cont5, cont6 Como Entero
    
    Escribir "Cuantas veces quieres lanzar el dado?"
    Leer veces
    
    cont1 <- 0
    cont2 <- 0
    cont3 <- 0
    cont4 <- 0
    cont5 <- 0
    cont6 <- 0
    
    Para i <- 1 Hasta veces Hacer
        numero <- Aleatorio(1, 6)
        Escribir "Lanzamiento ", i, ": ", numero
        
        Segun numero Hacer
            1: cont1 <- cont1 + 1
            2: cont2 <- cont2 + 1
            3: cont3 <- cont3 + 1
            4: cont4 <- cont4 + 1
            5: cont5 <- cont5 + 1
            6: cont6 <- cont6 + 1
        FinSegun
    FinPara
    
    Escribir ""
    Escribir "--- Resultados ---"
    Escribir "El numero 1 salio ", cont1, " veces"
    Escribir "El numero 2 salio ", cont2, " veces"
    Escribir "El numero 3 salio ", cont3, " veces"
    Escribir "El numero 4 salio ", cont4, " veces"
    Escribir "El numero 5 salio ", cont5, " veces"
    Escribir "El numero 6 salio ", cont6, " veces"
FinFuncion

Algoritmo reto3
    contar_numeros
FinAlgoritmo