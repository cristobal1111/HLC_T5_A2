import random

def adivina_numero():
    secreto = random.randint(1, 50)
    encontrado = False
    print("Intenta adivinar el número secreto (entre 1 y 50):")
    while not encontrado:
        intento = int(input("Introduce tu número: "))
        if intento < secreto:
            print("El número es mayor.")
        elif intento > secreto:
            print("El número es menor.")
        else:
            print("¡Has acertado!")
            encontrado = True

adivina_numero()