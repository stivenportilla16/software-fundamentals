Algoritmo VerificadorParidad
    // Declarar variables
    Definir num1, num2 Como Real
    
    // Obtener el primer número
    Escribir "Enter the number 1"
    Leer num1
    
    // Obtener el segundo número
    Escribir "Enter the number 2"
    Leer num2
    
    // Evaluar el primer número
    Si num1 > 0 Entonces
        // El número es positivo
        Si num1 MOD 2 = 0 Entonces
            Escribir "The first number positive ", num1, " its even"
        SiNo
            Escribir "The first number positive ", num1, " Its odd"
        FinSi
    SiNo
        // El número es negativo o cero
        Si (-num1) MOD 2 = 0 Entonces
            Escribir "The first number negative ", num1, " its even"
        SiNo
            Escribir "The first number negative ", num1, " Its odd"
        FinSi
    FinSi
    
    // Evaluar el segundo número
    Si num2 > 0 Entonces
        // El número es positivo
        Si num2 MOD 2 > 0 Entonces
            Escribir "The second number positive ", num2, " Its odd"
        SiNo
            Escribir "The second number positive ", num2, " its even"
        FinSi
    SiNo
        // El número es negativo o cero
        Si (-num2) MOD 2 > 0 Entonces
            Escribir "The second number negative ", num2, " Its odd"
        SiNo
            Escribir "The second number negative ", num2, " its even"
        FinSi
    FinSi
FinAlgoritmo

