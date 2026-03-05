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


##Segundo menu que le aparece al usuario.
MENU_MOVIMIENTOS = """
==============
=== CAJERO ===
==============
1. --> Consultar saldo.
2. --> Retirar saldo.
3. --> Depositar saldo.
4. --> Ver historial de movimientos
5. --> Salir."""


##Variable que controla cuantos movimientos desea hacer el usuario.
cantidad_movimientos = int(input("Cuantos movimientos desea hacer. \n"))

##Funcionalidad del MENU_MOVIMIENTOS.
def menu2 ():
    while True:
        ##Variable que guarda que movimientos desea hacer el usuario
        movimientos = input("Escoja una opción. \n")
        match movimientos:
            case "1": ##Consultar saldo
                pass
            case "2": ##Retirar saldo
                pass
            case "3": ##Depositar saldo
                pass
            case "4": ##Historial de movimientos
                pass
            case "5": ##Salir
                break
            case _: ##Caso de error
                print("Opción invalida. Intentelo de nuevo.")


##Mensaje de despedida.
print("Gracias por usar el cajero automático.")