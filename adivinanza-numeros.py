# # * Línea sin color

# # * Aquí empieza el juego
# # * Este juego trata de adivinar un número al azar con pistas

import os
import random
import platform
adivinado = False

def limpiar_consola():
    """Limpia la pantalla de la consola, compatible con Windows y Linux/macOS."""
    # Detecta el sistema operativo
    if platform.system() == "Windows" :
        os.system('cls') # Comando para Windows
    else:
        os.system('clear') # Comando para Linux y macOS

def juego_adivinanza ():
    # TODO: Generar un número del 1 al 100 ✅
    numero_secreto = random.randint(1,100)
    intentos = 0

    # TODO: Bienvenido al juego ✅

    print('¡Bienvenido al juego de adivinanza de números!')
    print('Debes adivinar un número del 1 al 100')
    print('DATO: Si colocas un dato inválido tus intentos no aumentan')
    print('Intenta adivinarlo siguiendo las pistas')
    print('Si no quieres jugar más ingresa \'salir\'')

    while not adivinado:
        # TODO: Solicitar un número del 1 al 100 ✅
        numero_ingresado = input('Introduzca un número del 1 al 100: ')

        # TODO: Verificar que el el valor ingresado sea un número ✅
        if numero_ingresado.isdigit() and int(numero_ingresado) <= 100 and int(numero_ingresado) >= 1:
            numero_ingresado = int(numero_ingresado) # ? Lo Lo pasamos de String a number
            intentos += 1

            if numero_ingresado < numero_secreto:
                print(f'El número secreto es mayor a {numero_ingresado}')
                if intentos == 1:
                    print(f'Llevas {intentos} intento')
                else:
                    print(f'Llevas {intentos} intentos')
            elif numero_ingresado > numero_secreto:
                print(f'El número secreto es menor a {numero_ingresado}')
                if intentos == 1:
                    print(f'Llevas {intentos} intento')
                else:
                    print(f'Llevas {intentos} intentos')
            else:
                print(f'¡Felicitaciones, has ganado!. El número {numero_ingresado} era el secreto')
                if intentos == 1:
                    print(f'Y lo lograste en {intentos} intento')
                else:
                    print(f'Y lo lograste en {intentos} intentos')
                break
        elif numero_ingresado == 'salir':
            siONo = input('Estas seguro de querer salir Presiona enter y si no quieres salir escribe no: ')
            if platform.system() == "Windows" and not siONo:
                os.system('cls') # Comando para Windows
                break
        else:
            print('Has ingresado un dato inválido')
            if intentos == 1:
                print(f'Llevas {intentos} intento')
            else:
                print(f'Llevas {intentos} intentos')

if not adivinado:
    juego_adivinanza()

