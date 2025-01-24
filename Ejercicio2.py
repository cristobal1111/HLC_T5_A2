numero1 = int(input("Ingresa el primer número: "))
numero2 = int(input("Ingresa el segundo número: "))
numero3 = int(input("Ingresa el tercer número: "))

if numero1 == numero2 == numero3:
    print("Todos los números son iguales.")
elif numero1 == numero2:
    print("El primer y segundo número son iguales.")
elif numero2 == numero3:
    print("El segundo y tercer número son iguales.")
elif numero1 == numero3:
    print("El primer y tercer número son iguales.")
elif numero1 > numero2 and numero1 > numero3:
    print("El primer número es el más grande.")
elif numero2 > numero1 and numero2 > numero3:
    print("El segundo número es el más grande.")
else:
    print("El tercer número es el más grande.")