Algoritmo CalculadoraMenu
    // Declarar variables
    Definir num1, num2, res Como Real
    Definir opt Como Entero
    
    // Inicializar variables
    num1 <- 0
    num2 <- 0
    
    // Obtener el primer número
    Escribir "Enter value to number 1:"
    Leer num1
    
    // Obtener el segundo número
    Escribir "Enter value to number 2:"
    Leer num2
    
    // Mostrar menú de operaciones matemáticas
    Escribir "Math menu: [1]. Add - [2]. Subs - [3]. Mult - [4]. Div - [5] All"
    Escribir "Press any option [1-5]"
    Leer opt
    
    // Evaluar la opción seleccionada
    Si opt = 1 Entonces
        // Suma
        res <- num1 + num2
        Escribir "Addition: ", res
    SiNo
        Si opt = 2 Entonces
            // Resta
            res <- num1 - num2
            Escribir "Substraction: ", res
        SiNo
            Si opt = 3 Entonces
                // Multiplicación
                res <- num1 * num2
                Escribir "Multiplication: ", res
            SiNo
                Si opt = 4 Entonces
                    // División
                    Si num2 = 0 Entonces
                        Escribir "It is not possible to divide by zero"
                    SiNo
                        res <- num1 / num2
                        Escribir "Division: ", res
                    FinSi
                SiNo
                    Si opt = 5 Entonces
                        // Todas las operaciones
                        Si num2 = 0 Entonces
                            Escribir "Add: ", num1 + num2
                            Escribir "Subs: ", num1 - num2
                            Escribir "Mult: ", num1 * num2
                            Escribir "Div: El numero 2 no puede ser ", num2
                        SiNo
                            Escribir "Add: ", num1 + num2
                            Escribir "Subs: ", num1 - num2
                            Escribir "Mult: ", num1 * num2
                            Escribir "Div: ", num1 / num2
                        FinSi
                    SiNo
                        // Opción inválida
                        Escribir "Option invalid"
                    FinSi
                FinSi
            FinSi
        FinSi
    FinSi
FinAlgoritmo

