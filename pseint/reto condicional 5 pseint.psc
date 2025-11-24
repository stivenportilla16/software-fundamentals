
Algoritmo CalculadoraSalarial
    // Declaración de variables
    Definir tiDo, nume, noms, apels, gen, direc, tel Como Caracter
    Definir aNa Como Entero
    Definir sala, nueSala, inc Como Real
    
    // Entrada de datos en las variables
    Escribir "Enter document type"
    Leer tiDo
    
    Escribir "Enter ID number"
    Leer nume
    
    Escribir "Enter names"
    Leer noms
    
    Escribir "Enter last names"
    Leer apels
    
    Escribir "Enter gender"
    Leer gen
    
    Escribir "Year of birth"
    Leer aNa
    
    Escribir "Address"
    Leer direc
    
    Escribir "Phone"
    Leer tel
    
    Escribir "Salary"
    Leer sala
    
    // Comparación de variable salario para realizar operaciones
    Si sala >= 2000000 Entonces
        // Salario mayor o igual a 2,000,000
        Si gen = "female" Entonces
            // Mujer: incremento del 3%
            inc <- (sala * 3) / 100
            nueSala <- sala + inc
            Escribir "The salary of ", noms, " ", apels, " is ", nueSala
        SiNo
            // Hombre: incremento del 2.5%
            inc <- (sala * 2.5) / 100
            nueSala <- sala + inc
            Escribir "The salary of ", noms, " ", apels, " is ", nueSala
        FinSi
    SiNo
        // Salario menor a 2,000,000
        Si sala > 1200000 O sala > 2000000 Entonces
            // Salario entre 1,200,000 y 2,000,000: incremento del 5%
            inc <- (sala * 5) / 100
            nueSala <- sala + inc
            Escribir "The salary of ", noms, " ", apels, " is ", nueSala
        SiNo
            // Salario menor o igual a 1,200,000
            Si gen = "female" Entonces
                // Mujer: incremento del 10%
                inc <- (sala * 10) / 100
                nueSala <- sala + inc
                Escribir "The salary of ", noms, " ", apels, " is ", nueSala
            SiNo
                // Hombre: incremento del 8%
                inc <- (sala * 8) / 100
                nueSala <- sala + inc
                Escribir "The salary of ", noms, " ", apels, " is ", nueSala
            FinSi
        FinSi
    FinSi
FinAlgoritmo