##Primer menu que le aparece al usuario.
MENU_LOGIN = """
==============
=== CAJERO ===
==============
1. --> Registrarse.
2. --> Iniciar sesión.
3. --> Salir."""


##Funcionalidad del MENU_LOGIN.
def menu1 ():
    while True:
        ##Mostrar menu
        print(MENU_LOGIN)

        ##Variable que guarda la opción que escoja el usuario.
        menu_registro = input("Escoja una opción. \n")

        match menu_registro:
            case "1": ##Registrarse.
                pass
            case "2": ##Iniciar sesión.
                pass
            case "3": ##Salir.
                break
            case _: ##Caso de error.
                print("Opción invalida. Intentelo de nuevo.")


##Mensaje de despedida.
print("Gracias por usar el cajero automático.")