import json
import os




def cargar_usuarios():
    if os.path.exists("usuarios.json"):
        with open("usuarios.json", "r") as archivo:
            return json.load(archivo)
    return {}

def guardar_usuarios(usuarios):
    with open("usuarios.json", "w") as archivo:
        json.dump(usuarios, archivo, indent=4)

usuarios = cargar_usuarios()

def registrar():
    
    print("\033[32m=======Menu de registro=======\033[0m")

    registrar_user=input("favor ingrese el nombre de usuario que desea registrar:  ")
    

    if registrar_user in usuarios:
        print("el usuario ya existe")
        return
    
    registrar_pass=input("favor ingrersar la contraseña que desea ligar al nombre que registro:  ")

    while len(registrar_pass) != 6 or not registrar_pass.isdigit():
        print("el pin debe tener exactamente 6 numeros")
        registrar_pass = input("\033[31mingrese un PIN valido\033[0m: ")

    
    usuarios[registrar_user]={"pass":registrar_pass,
                             "saldo": 1000,
                             "historial":[] }
    guardar_usuarios(usuarios)


def sesion():
    
    for i in range(3):
        print("\033[32m=======Menu de inicio de sesion=======\033[0m")
        user=input("ingrese el nombre al que se quiere logear: ")
        pas=input("ingrese el PIN asociado: ")
        if user in usuarios and pas ==usuarios[user]["pass"]:
            print("te pudiste logear")
            break
        else:
            intentos= 2-i
            print("\033[31m❌contraseña incorrecta\033[0m")
            print(f"\033[33m⚠️ Te quedan {intentos} intentos\033[0m")

            
        
        if i==2:
            print("\033[1;31m🚫 ACCESO BLOQUEADO\033[0m")
            break
        
    return user
