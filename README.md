# Cajero Automatico(ATM)
Simulación de un cajero automático desarrollado en Python que permite registrar usuarios, iniciar sesión y realizar operaciones bancarias.
## Descripción

Este proyecto es una simulación de un cajero automático en consola.
Permite a los usuarios registrarse, iniciar sesión y realizar operaciones como:

- Depositar dinero
- Retirar dinero
- Consultar saldo
- consultar historial

La información de los usuarios se guarda en un archivo JSON para mantener los datos incluso después de cerrar el programa.

## funcionalidades
- ### Registra usuarios
#### registra
```
registrar_user=input("favor ingrese el nombre de usuario que desea registrar:  ")

if registrar_user in usuarios:
    print("el usuario ya existe")
    return

```
>El sistema solicita al usuario ingresar un nombre de usuario.
Luego verifica si el nombre ya existe dentro del diccionario `usuarios`.
Si el usuario ya está registrado, el sistema muestra un mensaje y cancela el proceso.

#### Validacion de PIN
```
registrar_pass=input("favor ingrersar la contraseña que desea ligar al nombre que registro:  ")

    while len(registrar_pass) != 6 or not registrar_pass.isdigit():
        print("el pin debe tener exactamente 6 numeros")
        registrar_pass = input("\033[31mingrese un PIN valido\033[0m: ")
```
>El sistema solicita un PIN de 6 dígitos numéricos.
>Para validar esto se utiliza un bucle `while` que se repite hasta que el usuario ingrese un PIN válido.

Condiciones:
- Debe tener exactamente 6 caracteres
- Solo debe contener números

- Inicio de sesión
- Depósitos
- Retiros
- Consulta de saldo
- consulta de movimientos(*historial*)
- Guardado de datos usando JSON
#### Creacion del usuario
```
 usuarios[registrar_user]={"pass":registrar_pass,
                             "saldo": 1000,
                             "historial":[] }
```
>Una vez validado el PIN, se crea un nuevo registro dentro del diccionario `usuarios`.

Cada usuario contiene:

- `pass`: PIN del usuario
- `saldo`: saldo inicial de 1000
- `historial`: lista vacía donde se guardarán las transacciones

#### Gurdado de datos
```
guardar_usuarios(usuarios)
```

>Finalmente se llama a la función `guardar_usuarios()` para almacenar la información en el archivo JSON.
---
- ### inicio de sesion
#### Control de intentos
```
for i in range(3):
```
>Se inicia un bucle que permite al usuario intentar iniciar sesión hasta tres veces antes de bloquear el acceso.

#### solicitud de credenciales 
```
user = input("ingrese el nombre al que se quiere logear: ")
pas = input("ingrese el PIN asociado: ")
```
>El sistema solicita al usuario el nombre de la cuenta y el PIN asociado para validar las credenciales.

#### Verificacion de credenciales
```
if user in usuarios and pas == usuarios[user]["pass"]:
 print("te pudiste logear")
            return user   # login exitoso
```
>Se verifica si el usuario existe en el diccionario usuarios y si el PIN ingresado coincide con el almacenado. una vez concidan el login sera exitoso

#### Contador de intentos
```
else:
            intentos = 2 - i
            print("\033[31m❌contraseña incorrecta\033[0m")

            if intentos > 0:
                print(f"\033[33m⚠️ Te quedan {intentos} intentos\033[0m")
            else:
                print("\033[1;31m🚫 ACCESO BLOQUEADO\033[0m")
                return None   # login fallido
```
>cada intento fallido descuenta 1 de los intentos ademas se le da el privilegio al usuario de saber cuantos intentos le quedan. una
>
>Una vez los intentos llegen a 0 se le bloquea el acceso al usuario, finalisando su proceso de inico de sesion
---

- ### depositos
#### Solicitud del monto a depositar
```
monto = float(input("ingresa el monto a depositar: "))

```
>Se solicita al usuario el monto que desea añadir a su saldo.

#### Validacion del monto
```
if monto < 0:
```
>El sistema valida que el monto ingresado sea válido, evitando depósitos con valores negativos.

#### Actualización del saldo
usuarios[registrar_user]["saldo"] += monto
>El monto ingresado se añade al saldo actual del usuario dentro del diccionario usuarios.

#### Registro en el historial
```
usuarios[registrar_user]["historial"].append(f"Depósito: +${monto}")
print("desposito existoso.")
```
>La transacción se registra en el historial para mantener un registro de los movimientos realizados. ademas le hace saber al usuario que su deposito fue exitoso

#### Manejo de errores
```
except ValueError:
        print("dato invalido. debe ingresar un numero.")
```
>El sistema detecta entradas inválidas (por ejemplo texto) y muestra un mensaje indicando que se debe ingresar un número.
---
- ### retiros
#### Solicitud del monto a retirar
```
monto = float(input("ingresa el monto a retirar: "))
```
>Se solicita al usuario la cantidad de dinero que desea retirar de su cuenta.

#### Validación de monto negativo
```
if monto <0:
            print("El monto no puede ser negativo")
            return
```
> al ver que el usuario registra un numero negativo le hace saber que no puede ingresar es e monto

#### Validación de saldo disponible
```
if monto > usuarios[user]["saldo"]:
print("el monto no puede ser mayor al disponible")
return
```
>Se valida que el usuario tenga suficiente dinero en su cuenta para realizar el retiro.

#### Actualización del saldo
```
usuarios[user]["saldo"] -= monto
```
>El sistema descuenta el monto retirado del saldo almacenado en el diccionario usuarios.

#### Registro en historial
```
usuarios[user]["historial"].append(f"Retiro: -${monto}")
```
>El sistema registra el retiro en el historial de transacciones del usuario.

#### Manejo de errores
```
except ValueError:
        print("dato invalido. debe ingresar un numero.")
```
>El sistema detecta entradas inválidas y muestra un mensaje indicando que se debe ingresar un número.
---
- ### consultar saldo
```
def consulta_tu_saldo(usuarios, user):
    return usuarios[user]["saldo"]
```
>Retorna el saldo actual del usuario almacenado en el diccionario usuarios.
---
- ### consultar historial
#### Obtención del historial
```
historial = usuarios[registrar_user]["historial"]
```
>Se accede al historial de transacciones asociado al usuario que inició sesión.

- ### Verificación de historial vacío
```
 
    if len(historial) == 0:
        print("No hay movimientos registrados.")
```
>El sistema verifica si la lista de movimientos está vacía.
> ademas Se le notifica al usuario que aún no ha realizado transacciones.
---
#### Mostrar historial de movimientos
```
print("\n--- Historial de movimientos ---")
        for movimiento in historial:
            print(movimiento)
```

>Se recorre la lista de transacciones y se imprime cada movimiento realizado por el usuario.

- ### opcion salir
```
def salir():
    print("Gracias por usar el cajero automático.")
```
>Indica que el usuario ha salido del sistema del cajero automático.

- ### Guardado de datos con json
#### Importación de módulos
```
import json
import os
```
>json permite leer y guardar datos en formato JSON.

>os permite verificar si el archivo usuarios.json existe en el sistema.

#### carga de usuarios desde el archivo
```
def cargar_usuarios():
    if os.path.exists("usuarios.json"):
        with open("usuarios.json", "r") as archivo:
            return json.load(archivo)
    return {}
```
- ##### Verificación del archivo
```
os.path.exists("usuarios.json")
```
>Evita errores al intentar leer un archivo que no existe.

- ##### Lectura del archivo
```
with open("usuarios.json", "r") as archivo:
```
>Se accede al archivo para leer la información almacenada.

- ##### Conversión de JSON a diccionario
```
return json.load(archivo)
```
>Permite trabajar con los datos de los usuarios dentro del programa.

- ##### Inicialización si no existe archivo
```
return {}
```
>Permite iniciar el sistema sin usuarios registrados.

#### Guardado de usuarios
```
def guardar_usuarios(usuarios):
    with open("usuarios.json", "w") as archivo:
        json.dump(usuarios, archivo, indent=4)
```
- ##### Apertura del archivo en modo escritura
```
open("usuarios.json", "w")
``` 
>Abre o crea el archivo donde se almacenarán los usuarios.

- ##### Conversión de diccionario a JSON
``` 
json.dump(usuarios, archivo, indent=4)
``` 
>Convierte el diccionario usuarios en formato JSON y lo guarda en el archivo.

####  Inicialización de los usuarios
``` 
usuarios = cargar_usuarios()
``` 
>Se crea la variable usuarios con los datos cargados desde el archivo JSON para que el sistema pueda utilizarlos durante la ejecución.
---

## tecnologias
- Python
- JSON
- Git
- GitHub

## isntalacion 
1. clonar el repositorio
>git clone https://github.com/doctorpatitas/proyecto_en_grupo_ATM.git
2. entrar en la carpeta
> cd proyecto_en_grupo_ATM
3. ejecutar desde main.py

## uso 
el usuario vera en consola
``` 
==============
=== CAJERO ===
==============
1. --> Registrarse.
2. --> Iniciar sesión.
3. --> Salir."""

Escoja una opción.
``` 
#
tendra que registrarse primero
``` 
==============
=== CAJERO ===
==============
1. --> Registrarse.
2. --> Iniciar sesión.
3. --> Salir."""

Escoja una opción.
1
``` 
#
eso deplegara el menu de registro junto al primer input
``` 
("\033[32m=======Menu de registro=======\033[0m"
favor ingrese el nombre de usuario que desea registrar:
``` 
#
una vez ingrese el usuario a registrar le pedira la contraseña a crear
``` 
("\033[32m=======Menu de registro=======\033[0m"
favor ingrese el nombre de usuario que desea registrar: milton
favor ingrersar la contraseña que desea ligar al nombre que registro: 123456
``` 
>como antes se explico la contraseña debe tener 6 digitos **numericos** como minimo

#


una vez registrado se volvera desplegar el primer menu
``` 
==============
=== CAJERO ===
==============
1. --> Registrarse.
2. --> Iniciar sesión.
3. --> Salir."""

Escoja una opción.
``` 
#
el usuario debera escoger la opcion relacionada con el inicio de sesion
``` 
==============
=== CAJERO ===
==============
1. --> Registrarse.
2. --> Iniciar sesión.
3. --> Salir."""

Escoja una opción.
2
``` 
#
esto desplegara el munu de inicio de sesion con con el primer input
``` 
\033[32m=======Menu de inicio de sesion=======\033[0m
ingrese el nombre al que se quiere logear:
``` 
>posdata: los numeros en los nombres son los que definen el color a mostrar en la consola

#
una vez ingresado el nombre al que se quiere logear debera ingresar su PIN registrado anterior mente

``` 
\033[32m=======Menu de inicio de sesion=======\033[0m
ingrese el nombre al que se quiere logear: milton
ingrese el PIN asociado: 123456
``` 
#
una vez el usuario se pudo loegear desplegara el menu del cajero donde debera digitar el numero de movimientos que desea hacer
``` 
Cuantos movimientos desea hacer: 3

==============
=== CAJERO ===
==============
1. --> Consultar saldo.
2. --> Retirar saldo.
3. --> Depositar saldo.
4. --> Ver historial de movimientos
5. --> Salir."""

Escoja una opción 2
``` 
#
cada movimiento le enviara a su respectivo menu
donde se le pedria la cantidad que desea depositar o retirar
``` 
ingresa el monto a retirar: 500
retiro existoso
``` 
#
una vez el usuario haga su movimiento lo devolvera a el menu del cajero y si este quiere consultar su saldo debera elegir la opcion 1
``` 

==============
=== CAJERO ===
==============
1. --> Consultar saldo.
2. --> Retirar saldo.
3. --> Depositar saldo.
4. --> Ver historial de movimientos
5. --> Salir."""

Escoja una opción 1

``` 
#
y esto le mostrara su saldo actual
``` 
 500 
``` 

#
cuando el usuario desee ver su saldo
``` 

==============
=== CAJERO ===
==============
1. --> Consultar saldo.
2. --> Retirar saldo.
3. --> Depositar saldo.
4. --> Ver historial de movimientos
5. --> Salir."""

Escoja una opción 4
``` 

#
aparecera la cantidad de dinero retirado y depositado
``` 
Retiro: -$500.0
Depósito: +$0.0
``` 

#
si al usuario le sobraron movimientos puede escoger la opcion salir
``` 

==============
=== CAJERO ===
==============
1. --> Consultar saldo.
2. --> Retirar saldo.
3. --> Depositar saldo.
4. --> Ver historial de movimientos
5. --> Salir."""

Escoja una opción 5
``` 

#
esto lo de volvera al menu de del login
``` 
==============
=== CAJERO ===
==============
1. --> Registrarse.
2. --> Iniciar sesión.
3. --> Salir.
Escoja una opción.
``` 
# 
si el usuario se siente satisfecho o ya realiso los movimientos que queria puede escoger la opcion salir
``` 
==============
=== CAJERO ===
==============
1. --> Registrarse.
2. --> Iniciar sesión.
3. --> Salir.
Escoja una opción.
3
``` 
# 
esto imprimira el mensaje 
``` 
Gracias por usar el cajero automático.
``` 

y cerrara el programa

----

- ## Estructura del proyecto
proyecto_en_grupo_ATM/
│
├── main.py          # menú principal
├── funciones2.py    # funciones de un ATM
├── login.py         # registro e inicio de sesión
├── usuarios.json    # base de datos de usuarios
└── README.md        # documentación
> 1. proyecto_en_grupo_ATM/

>2. main.py          ( menú principal)
>3. funciones2.py     (funciones de un ATM)
>4. login.py         ( registro e inicio de sesión)
>5. usuarios.json    (base de datos de usuarios)
>6. README.md        ( documentación)
---
# gracias por leer

