Funcion lanzar_con_reporte
    Definir numero, total_tiros, suma_total, total_pares, total_impares Como Entero
    Definir seguir Como Caracter
    
    total_tiros <- 0
    suma_total <- 0
    total_pares <- 0
    total_impares <- 0
    seguir <- "si"
    
    Mientras seguir == "si" O seguir == "s" Hacer
        numero <- Aleatorio(1, 6)
        total_tiros <- total_tiros + 1
        suma_total <- suma_total + numero
        
        Escribir ""
        Escribir "Tiro #", total_tiros, ": ", numero
        
        Si numero % 2 == 0 Entonces
            total_pares <- total_pares + 1
        SiNo
            total_impares <- total_impares + 1
        FinSi
        
        Escribir "Deseas volver a lanzar? (si/no): "
        Leer seguir
    FinMientras
    
    Escribir ""
    Escribir "========================================"
    Escribir "REPORTE FINAL"
    Escribir "========================================"
    Escribir "Total de tiros efectuados: ", total_tiros
    Escribir "Suma total de los tiros: ", suma_total
    Escribir "Total de pares generados: ", total_pares
    Escribir "Total de impares generados: ", total_impares
    Escribir "========================================"
FinFuncion

Algoritmo reto6
    lanzar_con_reporte
FinAlgoritmo
