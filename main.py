##Importaciones
import login
import funciones2


##Primer menu que le aparece al usuario.
MENU_LOGIN = """
━━━━━━━━━━━━━━━━━━━━━━━━━
🏦  TechBank Riwi Digital
━━━━━━━━━━━━━━━━━━━━━━━━━
1️⃣ Registrarse.
2️⃣ Iniciar sesión.
3️⃣ Salir.
━━━━━━━━━━━━━━━━━━━━━━━━━"""


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
━━━━━━━━━━━━━━━━━━━━━━━━━━━━
🏦  TechBank Riwi Digital
━━━━━━━━━━━━━━━━━━━━━━━━━━━━
1️⃣ Consultar saldo.
2️⃣ Retirar dinero.
3️⃣ Depositar dinero.
4️⃣ Historial de movimientos.
5️⃣ Salir.
━━━━━━━━━━━━━━━━━━━━━━━━━━━━"""


##Funcionalidad del MENU_MOVIMIENTOS.
def menu2 (user):
    ##Variable que controla cuantos movimientos desea hacer el usuario.
    while True:
        try:
            cantidad_movimientos = int(input("Cuantos movimientos desea hacer. \n"))
            break
        except ValueError:
            print("Ingrese un número valido.")
            continue


    
    movimientos_restantes = cantidad_movimientos


    while movimientos_restantes > 0:
        ##Mostrar menu de movimientos
        print(MENU_MOVIMIENTOS)


        ##Variable que guarda que movimientos desea hacer el usuario
        movimientos = input("Escoja una opción. \n")


        match movimientos:
            case "1": ##Consultar saldo
                print(funciones2.consulta_tu_saldo(login.usuarios, user))
                movimientos_restantes -= 1

            case "2": ##Retirar saldo
                if funciones2.retirar_dinero(login.usuarios, user):
                    movimientos_restantes -= 1

            case "3": ##Depositar saldo
                if funciones2.depositar_dinero(login.usuarios, user):
                    movimientos_restantes -= 1

            case "4": ##Historial de movimientos
                funciones2.ver_historial(login.usuarios, user)
                movimientos_restantes -= 1

            case "5": ##Salir
                break
            
            case _: ##Caso de error
                print("Opción invalida. Intentelo de nuevo.")

        if movimientos_restantes == 0:
            seguir = input("¿Desea hacer mas movimientos? (sí/no): \n")

            if seguir.lower() == "sí":
                return menu2(user)
            else:
                break


##Llamar a la primera función
menu1()


##Mensaje de despedida.
print("Gracias por usar el cajero automático.")