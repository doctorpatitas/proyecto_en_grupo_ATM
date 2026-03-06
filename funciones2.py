def consulta_tu_saldo(usuarios, user):
    return usuarios[user]["saldo"]

def retirar_dinero(usuarios, user):
    try:
        monto = float(input("ingresa el monto a retirar: "))

        if monto <0:
            print("El monto no puede ser negativo")

        if monto > usuarios[user]["saldo"]:
            print("el monto no puede ser mayor al disponible")
        
        usuarios[user]["saldo"] -= monto

        usuarios[user]["historial"].append(f"Retiro: -${monto}")

        print("retiro existoso.")

    except ValueError:
        print("dato invalido. debe ingresar un numero.")

def depositar_dinero(usuarios, registrar_user):
    try:
        monto = float(input("ingresa el monto a depositar: "))

        if monto <0:
            print("El monto no puede ser negativo")
            return

        usuarios[registrar_user]["saldo"] += monto

        usuarios[registrar_user]["historial"].append(f"Depósito: +${monto}")

        print("desposito existoso.")
    except ValueError:
        print("dato invalido. debe ingresar un numero.")

def ver_historial(usuarios, registrar_user):

    historial = usuarios[registrar_user]["historial"]
    
    if len(historial) == 0:
        print("No hay movimientos registrados.")
    else:
        print("\n--- Historial de movimientos ---")
        for movimiento in historial:
            print(movimiento)

def salir():
    print("Gracias por usar el cajero automático.")

