print ("Hola mundo")

def OperacionesAritmeticas():
# colocar los numeros de a y b
    a = float(input("Ingrese el primer numero (a): "))
    b = float(input("Ingrese el segundo numero (b): "))

# Realizar operaciones aritmeticas
Multiplicacion = a * b
Suma = a + b
Resta = a - b

#Manejar la division por cero para evitar errores
if b != 0:    
    division = a / b
else:
    Division= "Division por cero no esta definida"
return suma, resta, Multiplicacion, Division

#Llamar a la funcion y obtener el resultado
resultado = OperacionesAritmeticas()

#Imprimir el resultado de cada operacion aritmetica
print:("Suma:", resultado [0])
print:("Resta:", resultado [1])
print:("Multiplicacion:", resultado [2])
print:("Division:", resultado [3])
