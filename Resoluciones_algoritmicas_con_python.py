                                #ejercicio n1
        
"""import string

alfabeto = string.ascii_lowercase
frase = input("Ingresa una frase: ").lower()

ocurrencias = {letra: 0 for letra in alfabeto}

for letra in frase:
    if letra in ocurrencias:
        ocurrencias[letra] += 1

for letra, count in ocurrencias.items():
    if count > 0:
        print(f"La letra '{letra}' aparece {count} vez(es) en la frase.") """

                        #ejercicio n2

"""num = int(input("Ingrese un numero: "))  
    
if num < 0: 
    print ("el numero ingresado es negativo")
if num > 0: 
    print ("el numero ingresado es positivo") 
if num == 0:
    print ("el numero ingresado es igual a  0")"""

    
                            #ejercicio n3 

"""list_num = []
num = int(input("Ingresa un número entero - ingresa 0 para salir: "))

while num != 0:
    list_num.append(num)
    num = int(input("Ingresa un número entero - ingresa 0 para salir: "))

sumatoria = sum(list_num)
promedio = sumatoria / len(list_num) if len(list_num) > 0 else 0

print("La sumatoria de los números es:", sumatoria)
print("El promedio de los números es:", promedio) """
    
                            #ejercicio n4
                            
"""list_num = []
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
        num_abs //= 

print("La suma de los dígitos de los números ingresados es:", sum_dig)"""
