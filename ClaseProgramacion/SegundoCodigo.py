#Solicitar al usuario, ingresar el numero
numero = int(input("Ingrese un numero ent15ero: "))

# Verificar si el numero es par, impar o 0
if numero == 0:
    print("El numero ingresado es 0.")
elif numero % 2 == 0:
    print("El numero ingresado es par.")
else:
    print("El numero ingresado es impar.")

# Verificar si el numero impar es divisible entre 3
    if numero % 3 == 0:
        print("El numero par ingresado no es divisible entre .3")
    else:
        print("El numero impar ingresado no es divisible entre .3")

    Juan = 20
    Pedro = 10
    Javier = 50
    Junior = 1

    print(Juan > Pedro)
    print(Juan > Pedro < Junior)
    print(Juan < Pedro > Junior)
    print(Junior < Pedro < Juan < Javier)
    print(Pedro + Junior < Juan)
    print(Pedro + Junior <= Juan)
    print(Juan - Junior == Pedro)
