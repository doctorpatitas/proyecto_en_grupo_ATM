##Importaciones
import login



def consulta_tu_saldo(usuarios, user):
    return usuarios[user]["saldo"]

def retirar_dinero(usuarios, user):
    try:
        monto = float(input("Ingresa el monto a retirar: "))

        if monto < 0:
            print("El monto no puede ser negativo.")
            return False

        if monto > usuarios[user]["saldo"]:
            print("El monto no puede ser mayor al disponible.")
            return False
        
        usuarios[user]["saldo"] -= monto

        usuarios[user]["historial"].append(f"Retiro: -${monto}")

        ##GUARDAR CAMBIOs
        login.guardar_usuarios(usuarios)

        print("Retiro existoso.")
        return True

    except ValueError:
        print("Dato invalido. Debe ingresar un numero.")
        return False

def depositar_dinero(usuarios, registrar_user):
    try: 
        monto = float(input("Ingresa el monto a depositar: "))

        if monto <0:
            print("El monto no puede ser negativo.")
            return False

        usuarios[registrar_user]["saldo"] += monto

        usuarios[registrar_user]["historial"].append(f"Depósito: +${monto}")

        ##GUARDAR CAMBIOS
        login.guardar_usuarios(usuarios)

        print("Deposito existoso.")
        return True
    
    except ValueError:
        print("Dato invalido. Debe ingresar un numero.")
        return False

def ver_historial(usuarios, registrar_user):

    historial = usuarios[registrar_user]["historial"]
    
    if len(historial) == 0:
        print("No hay movimientos registrados.")
    else:
        print("\n--- Historial de movimientos ---")
        for movimiento in historial:
            print(movimiento)

