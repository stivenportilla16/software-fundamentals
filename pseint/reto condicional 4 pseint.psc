
// Función para mostrar el menú
SubProceso mostrar_menu
    Escribir "Math menu:"
    Escribir "  [1]. Add"
    Escribir "  [2]. Subs"
    Escribir "  [3]. Mult"
    Escribir "  [4]. Div"
    Escribir "  [5]. All"
    Escribir ""
FinSubProceso

// Función para calcular según la opción (opciones 1-4)
Funcion resultado <- calc(n1, n2, op)
    Definir resultado Como Real
    
    Segun op Hacer
        1:
            resultado <- n1 + n2
        2:
            resultado <- n1 - n2
        3:
            resultado <- n1 * n2
        4:
            Si n2 <> 0 Entonces
                resultado <- n1 / n2
            SiNo
                Escribir "It is not possible to divide by zero"
                resultado <- 0
            FinSi
        De Otro Modo:
            Escribir "Invalid option !!!"
            resultado <- 0
    FinSegun
FinFuncion

// Procedimiento para mostrar todas las operaciones (opción 5)
SubProceso calcAll(n1, n2)
    Escribir "Add: ", n1 + n2
    Escribir "Subs: ", n1 - n2
    Escribir "Mult: ", n1 * n2
    
    Si n2 <> 0 Entonces
        Escribir "Div: ", n1 / n2
    SiNo
        Escribir "Div: No division by zero"
    FinSi
FinSubProceso

// ============================================
// ALGORITMO PRINCIPAL
// ============================================
Algoritmo CalculadoraConFunciones
    Definir num1, num2, r Como Real
    Definir opt Como Entero
    
    // Limpiar pantalla
    Limpiar Pantalla
    
    // Obtener números
    Escribir Sin Saltar "Enter value to number 1: "
    Leer num1
    
    Escribir Sin Saltar "Enter value to number 2: "
    Leer num2
    
    // Mostrar menú
    mostrar_menu
    
    Escribir Sin Saltar "Press any option [1 - 5]: "
    Leer opt
    
    // Procesar según la opción
    Si opt >= 1 Y opt <= 4 Entonces
        r <- calc(num1, num2, opt)
        Escribir "Answer: ", r
    SiNo
        Si opt = 5 Entonces
            calcAll(num1, num2)
        SiNo
            Escribir "Invalid option !!!"
        FinSi
    FinSi
    
FinAlgoritmo