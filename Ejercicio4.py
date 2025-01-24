def verificar_contraseña():
    contraseña_sistema = "1234"
    intentos = 0
    while intentos < 3:
        contraseña_usuario = input("Introduce la contraseña: ")
        if contraseña_usuario == contraseña_sistema:
            print("Bienvenido")
            break
        else:
            print("Contraseña incorrecta")
            intentos += 1

verificar_contraseña()