import random
from turtle import width


def generar_correo():
    mayuscula = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"]
    minuscula = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]
    numeros = ["1", "2", "3", "4", "5", "6", "7", "8", "9",]

    caracteres = mayuscula + minuscula + numeros
    
    correo = []

    for i in range(10):
        caracter_random = random.choice(caracteres)
        correo.append(caracter_random)

    correo = "".join(correo)
    return correo


def generar_contrasena():
    mayuscula = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"]
    minuscula = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]
    numeros = ["1", "2", "3", "4", "5", "6", "7", "8", "9",]
    simbolos = ["!", "#", "$", "%", "&", "/", "(", ")", "=", "?¡"]

    caracteres = mayuscula + minuscula + simbolos + numeros

    contrasena = []

    for i in range(20):
        caracter_random = random.choice(caracteres)
        contrasena.append(caracter_random)

    contrasena = "".join(contrasena)
    return contrasena


def run():
    menu = """Bienvenido al generador de correo y contraseña

    1 - @gmail
    2 - @protonmail
    3 - @hotmail.com

    Elije una opción del (1 al 3): """
    opcion = int(input(menu))
    if opcion == 1:
        gmail = "@gmail.com"
        correo = generar_correo()
        print("======================================")
        print("Tu nuevo correo es: " + correo + gmail)
        print("======================================")
        resultado = ("Correo: " + correo + gmail)
        contrasena = generar_contrasena()
        print("======================================")
        print("Tu nueva contraseña es: " + contrasena)
        print("======================================")
        resultado1 = ("Contraseña: " + contrasena)
    elif opcion == 2:
        protonmail = "@protonmail.com"
        correo = generar_correo()
        print("======================================")
        print("Tu nuevo correo es: " + correo + protonmail)
        print("======================================")
        resultado = ("Correo: " + correo + protonmail)
        contrasena = generar_contrasena()
        print("======================================")
        print("Tu nueva contraseña es: " + contrasena)
        print("======================================")
        resultado1 = ("Contraseña: " + contrasena)
    elif opcion == 3:
        hotmail = "@hotmail.com"
        correo = generar_correo()
        print("======================================")
        print("Tu nuevo correo es: " + correo + hotmail)
        print("======================================")
        resultado = ("Correo: " + correo + hotmail)
        contrasena = generar_contrasena()
        print("======================================")
        print("Tu nueva contraseña es: " + contrasena)
        print("======================================")
        resultado1 = ("Contraseña: " + contrasena)
    else:
        print("Esta no es una opción valida")
    f = open("accounts_generator.txt", "a", encoding="utf-8")
    f.write(resultado+"\n")
    f.write(resultado1+"\n")
    firma = """
        ██╗      ██╗ █████╗  ██████╗ ██╗   ██╗ ██╗  ██╗    ██╗██╗ ██╗  ██╗ ███████╗ ██╗      ██╗       █████╗
        ██║      ██║ ██╔══██╗██╔════╝ ╚██╗██╔╝ ╚██╗██╔╝    ╚█║╚█║ ██║  ██║ ██╔════╝ ██║      ██║      ██╔══██╗
        ██║      ██║ ██║  ██║╚█████╗   ╚███╔╝   ╚███╔╝      ╚╝ ╚╝ ███████║ █████╗   ██║      ██║      ██║  ██║
        ██║      ██║ ██║  ██║ ╚═══██╗  ██╔██╗   ██╔██╗            ██╔══██║ ██╔══╝   ██║      ██║      ██║  ██║
        ███████╗ ██║ ╚█████╔╝██████╔╝ ██╔╝╚██╗ ██╔╝╚██╗           ██║  ██║ ███████╗ ███████╗ ███████╗ ╚█████╔╝
        ╚══════╝ ╚═╝ ╚════╝ ╚═════╝  ╚═╝  ╚═╝  ╚═╝  ╚═╝           ╚═╝  ╚═╝╚══════╝╚══════╝╚══════╝ ╚════╝

         ██╗       ██╗  █████╗  ██████╗  ██████╗  ██╗██╗
         ██║  ██╗  ██║ ██╔══██╗ ██╔══██╗ ██╔══██╗ ╚█║╚█║
         ╚██╗████╗██╔╝ ██║  ██║ ██████╔╝ ██║  ██║  ╚╝ ╚╝
          ████╔═████║  ██║  ██║ ██╔══██╗ ██║  ██║ 
          ╚██╔╝ ╚██╔╝  ╚█████╔╝ ██║  ██║ ██████╔╝ 
           ╚═╝   ╚═╝   ╚════╝╚═══════╝╚═════╝  
            """

if __name__ == "__main__":
    run()




     #               __███                                   #
    #               ___█▓█▓█                                #
     #               ___█▓▓█▓▓█                              #
      #              ___█▓▓▓██▓███_______ ██                  #
       #             ___████▓▓▓█████___ █▓▓█                   #
        #            _█▓▓▓▓▓██▓███▓███▓▓▓▓█                     #
         #           █░███▓▓▓▓▓█▓▓██▓█▓▓▓▓█                      #
          #          █░█o██▓▓▓█▓▓█▓▓▓▓█▓▓▓█                       #
           #         █░░░░█▓▓▓▓▓▓████▓▓▓▓█                      #
            #        █████▓▓▓▓▓█░█o███▓▓█                     #
             #       █▓▓▓▓█▓▓▓█░░██░██▓▓█                   #
              #      █▓▓▓▓███▓▓██░░██▓▓▓█                 #
               #     █▓▓▓▓▓█▓▓▓▓▓███▓▓▓▓█               #
                #    _█▓▓█▓█▓▓█▓▓▓▓▓▓▓▓ █_██          #
                 #   __██▓████▓▓▓▓▓▓▓▓▓ █_█▓█       #
                  #  ____███▓▓▓▓▓▓▓▓████__█▓█     #
                   # ______████▓▓▓▓▓▓▓██__█▓█   #
                    #___█▓▓▓▓▓█▓██▓▓▓▓███▓█   #
                     #__█▓█▓▓▓██▓▓▓▓▓▓█▓██  #
                      #_ █▓█▓▓▓██▓▓▓▓█▓██ #