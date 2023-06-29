def elegir_opcion():
    
    #ejercicio n1
    import string
    def ejercicio_n1():
        alfabeto = string.ascii_lowercase
        frase = input("Ingresa una frase: ").lower()

        ocurrencias = {letra: 0 for letra in alfabeto}

        for letra in frase:
            if letra in ocurrencias:
                ocurrencias[letra] += 1

        for letra, count in ocurrencias.items():
            if count > 0:
                print(f"La letra '{letra}' aparece {count} vez(es) en la frase.")

    #ejercicio n2
    def ejercicio_n2():
        num = int(input("Ingrese un numero: "))  
        
        if num < 0: 
            print("El numero ingresado es negativo")
        elif num > 0: 
            print("El numero ingresado es positivo") 
        else:
            print("El numero ingresado es igual a 0")

    #ejercicio n3 
    def ejercicio_n3():
        list_num = []
        num = int(input("Ingresa un número entero - ingresa 0 para salir: "))

        while num != 0:
            list_num.append(num)
            num = int(input("Ingresa un número entero - ingresa 0 para salir: "))

        sumatoria = sum(list_num)
        promedio = sumatoria / len(list_num) if len(list_num) > 0 else 0

        print("La sumatoria de los números es:", sumatoria)
        print("El promedio de los números es:", promedio) 
    
    #ejercicio n4
    def ejercicio_n4():
        list_num = []
        num = int(input("Ingresa un número (ingresa 0 para salir): "))

        while num != 0:
            list_num.append(num)
            num = int(input("Ingresa un número (ingresa 0 para salir): "))

        sum_dig = 0

        for num in list_num:
            num_abs = abs(num) 
            while num_abs != 0:
                dig = num_abs % 10
                sum_dig += dig
                num_abs //= 10

        print("La suma de los dígitos de los números ingresados es:", sum_dig)

    #ejercicio n4
    def menu():
        while True:
            print("\n------ EXAMEN N1 DE PROGRAMACION - PYTHON ------")
            print("1. Ejercicio N1")
            print("2. Ejercicio N2")
            print("3. Ejercicio N3")
            print("4. Ejercicio N4")
            print("5. Salir")
        
            opcion = input("Seleccione una opción: ")
            if opcion == "1":
                ejercicio_n1()
            elif opcion == "2":
                ejercicio_n2()
            elif opcion == "3":
                ejercicio_n3()
            elif opcion == "4":
                ejercicio_n4()
            elif opcion == "5":
                break
            else:
                print("Opcion invalida. Por favor, seleccione una opcion nuevamente.")

    menu()

elegir_opcion()