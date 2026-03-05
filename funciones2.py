def consulta_tu_saldo(usuarios[registrar_user]["saldo"]):
    return usuarios[registrar_user]["saldo"]

def retirar_dinero(usuarios[registrar_user]["saldo"]):
    try:
        monto = float(input("ingresa el monto a retirar: "))

        if monto <0:
            print("El monto no puede ser negativo")

        if monto > usuarios[registrar_user]["saldo"]:
            print("el monto no puede ser mayor al disponible")
        
        usuarios[registrar_user]["saldo"] - monto

        usuarios[registrar_user]["historial"].append(f"Retiro: -${monto}")

        print("retiro existoso.")

    except: ValueError
    print("dato invalido. debe ingresar un numero.")


