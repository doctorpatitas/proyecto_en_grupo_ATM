##Importaciones
import login
import funciones2


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
        ##Mostrar menu de registro
        print(MENU_LOGIN)

        ##Variable que guarda la opción que escoja el usuario.
        menu_registro = input("Escoja una opción. \n")

        match menu_registro:
            case "1": ##Registrarse.
                login.registrar()
            case "2": ##Iniciar sesión.
                user = login.sesion()
                if user:
                    menu2(user)
            case "3": ##Salir.
                break
            case _: ##Caso de error.
                print("Opción invalida. Intentelo de nuevo.")
                continue


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


##Funcionalidad del MENU_MOVIMIENTOS.
def menu2 (user):
    ##Variable que controla cuantos movimientos desea hacer el usuario.
    while True:
        try:
            cantidad_movimientos = int(input("Cuantos movimientos desea hacer. \n"))
            break
        except ValueError:
            print("Ingrese un número valido.")

    for i in range(cantidad_movimientos):
        ##Mostrar menu de movimientos
        print(MENU_MOVIMIENTOS)


        ##Variable que guarda que movimientos desea hacer el usuario
        movimientos = input("Escoja una opción. \n")
        match movimientos:
            case "1": ##Consultar saldo
                print(funciones2.consulta_tu_saldo(login.usuarios, user))
            case "2": ##Retirar saldo
                funciones2.retirar_dinero(login.usuarios, user)
            case "3": ##Depositar saldo
                funciones2.depositar_dinero(login.usuarios, user)
            case "4": ##Historial de movimientos
                funciones2.ver_historial(login.usuarios, user)
            case "5": ##Salir
                break
            case _: ##Caso de error
                print("Opción invalida. Intentelo de nuevo.")


##Llamar a la primera función
menu1()


##Mensaje de despedida.
print("Gracias por usar el cajero automático.")