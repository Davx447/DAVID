def OperacionesAritmeticas():
    a = float(input("Ingrese el primer numero(a)"))
    b = float(input("Ingrese el primer numero(b)"))

    #Operacion 
    suma = a + b
    resta = a - b 
    multiplicacion = a+ b 

    #Division entre 0
    if b != 0:
        division = a / b 
    else: 
        division = "Division por cero no esta definida"
    return suma, resta, multiplicacion, division

    #Obtener resultado 
resultado = OperacionesAritmeticas()

print("Suma", resultado[0])
print("Resta", resultado[1])
print("Multiplicacion", resultado[2])
print("Division", resultado[3]) 
