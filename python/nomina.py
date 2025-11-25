import datetime

def calcular_edad(ano_nacimiento):
    """Calcula la edad actual a partir del año de nacimiento."""
    ano_actual = datetime.date.today().year
    return ano_actual - ano_nacimiento

def ValidarTelefono():
    status = False
    z = 0
    
    while status == False:
        telefono = input("Ingrese su numero de telefono: ")
        telefono_size = len(telefono)
        i = 0
        cont = 0
        while i < telefono_size:
            if telefono[i] < '0' or telefono[i] > '9':
                cont += 1
            i += 1
        if cont == 0:
            if len(telefono) == 10:
                z = int(telefono)
                status = True
            else:
                print("Error! El telefono debe tener 10 digitos.")
        else:
            print("Error! No es un numero de telefono valido")
    
    return z

def ingresar_empleados():
    """Permite ingresar datos de múltiples empleados y calcula estadísticas."""
    empleados = []
    total_salarios = 0
    total_edades = 0
    total_feme = 0
    total_mas = 0
    total_ot = 0
    
    while True:
        print("\n--- Ingrese empleado ---")
        nombre = input("Ingrese nombre: ")
        email = input("Ingrese email: ")
        movil = ValidarTelefono()  # Aquí usas la función de validación
        
        # Validación de género
        while True:
            genero = input("Ingrese género (M/F/O): ").strip().upper()
            if genero in ['M', 'F', 'O']:
                break
            else:
                print("Género no válido. Por favor ingrese M, F o O.")
        
        # Validación y conversión de salario a flotante
        while True:
            try:
                salario = float(input("Ingrese salario: "))
                if salario >= 0:
                    break
                else:
                    print("El salario debe ser un número positivo.")
            except ValueError:
                print("Entrada no válida. Por favor ingrese un número para el salario.")
        
        # Validación y conversión de año de nacimiento a entero
        while True:
            try:
                ano_nacimiento = int(input("Ingrese año de nacimiento: "))
                if 1900 <= ano_nacimiento <= datetime.date.today().year:
                    break
                else:
                    print(f"Año de nacimiento no válido. Debe estar entre 1900 y {datetime.date.today().year}.")
            except ValueError:
                print("Entrada no válida. Por favor ingrese un año válido (número entero).")
        
        edad = calcular_edad(ano_nacimiento)
        
        empleado = {
            "nombre": nombre,
            "email": email,
            "movil": movil,
            "genero": genero,
            "salario": salario,
            "ano_nacimiento": ano_nacimiento,
            "edad": edad
        }
        
        empleados.append(empleado)
        total_salarios += salario
        total_edades += edad
        if genero == 'M':
            total_mas += 1
        if genero == 'F':
            total_feme += 1
        if genero == 'O':
            total_ot += 1
        
        # Preguntar si desea ingresar más empleados
        continuar = input("\n¿Desea ingresar otro empleado? (si/no): ").lower()
        if continuar != 'si':
            break
    
    # Calcular y mostrar resultados finales 
    num_empleados = len(empleados)
    if num_empleados > 0:
        promedio_edades = total_edades / num_empleados
        print("\n--- Nómina ---")
        print(f"Total de empleados ingresados: {num_empleados}")
        print(f"Total de empleados con genero Femenino: {total_feme}")
        print(f"Total de empleados con genero Masculino: {total_mas}")
        print(f"Total de empleados con genero Otro: {total_ot}")
        print(f"Suma total de salarios: {total_salarios:,.2f}")
        print(f"Promedio de edades: {promedio_edades:.2f} años")
    else:
        print("No se ingresaron empleados.")

if __name__ == "__main__":
    ingresar_empleados()