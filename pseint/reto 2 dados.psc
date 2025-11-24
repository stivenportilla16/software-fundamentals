Funcion lanzar_varios_dados
    Definir veces, numero, suma, i Como Entero
    
    Escribir "Cuantas veces quieres lanzar el dado?"
    Leer veces
    
    suma <- 0
    
    Para i <- 1 Hasta veces Hacer
        numero <- Aleatorio(1, 6)
        Escribir "Lanzamiento ", i, ": ", numero
        suma <- suma + numero
    FinPara
    
    Escribir ""
    Escribir "La suma total es: ", suma
FinFuncion

Algoritmo reto2
    lanzar_varios_dados
FinAlgoritmo