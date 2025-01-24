def verificar_caracter():
    palabra = input("Introduce una palabra: ")
    for caracter in palabra:
        if "@" == caracter:
            print("La palabra contiene el carácter @")
        elif "#" == caracter:
            print("La palabra contiene el carácter #")
        elif "$" == caracter:
            print("La palabra contiene el carácter $")
        else "%" == caracter:
            print("La palabra contiene el carácter %")
        
verificar_caracter()