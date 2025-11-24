Funcion par_de_seis
    Definir dado1, dado2, lanzamientos Como Entero
    
    lanzamientos <- 0
    
    Repetir
        dado1 <- Aleatorio(1, 6)
        dado2 <- Aleatorio(1, 6)
        lanzamientos <- lanzamientos + 1
        
        Escribir "Lanzamiento ", lanzamientos, ": Dado 1 = ", dado1, ", Dado 2 = ", dado2
        
    Hasta Que dado1 == 6 Y dado2 == 6
    
    Escribir ""
    Escribir "PAR DE SEIS! El juego termina"
FinFuncion

Algoritmo reto4
    par_de_seis
FinAlgoritmo
