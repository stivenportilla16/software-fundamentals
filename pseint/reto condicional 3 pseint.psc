Algoritmo ValidadorParImpar
    // Declarar variable
    Definir numero Como Entero
    
    // Solicitar un número entero al usuario
    Escribir "Ingrese un número entero (positivo o negativo):"
    Leer numero
    
    // Validar si el número es positivo o negativo
    Si numero > 0 Entonces
        // Número positivo
        Si numero MOD 2 = 0 Entonces
            Escribir "El número ", numero, " es PAR POSITIVO"
        SiNo
            Escribir "El número ", numero, " es IMPAR POSITIVO"
        FinSi
    SiNo
        Si numero < 0 Entonces
            // Número negativo
            Si numero MOD 2 = 0 Entonces
                Escribir "El número ", numero, " es PAR NEGATIVO"
            SiNo
                Escribir "El número ", numero, " es IMPAR NEGATIVO"
            FinSi
        SiNo
            // Número es cero
            Escribir "El número ", numero, " es CERO (par y neutro)"
        FinSi
    FinSi
FinAlgoritmo
