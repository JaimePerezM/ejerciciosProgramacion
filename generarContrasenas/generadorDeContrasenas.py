"""
Generador de contraseñas seguras:
Crea un programa que genere contraseñas seguras que incluyan letras 
mayúsculas y minúsculas, números y caracteres especiales.
"""
import re
import random
import string
import sys
import random
import string
import re


def crearClaveSegura():

    largo = 0

    while largo < 4:

        try:
            largo = int(input(
                "\ningrese el largo de la contraseña (debe ser igual o mayor a 4 dígitos): \n").strip())

            if largo < 4:
                print("\nLa contraseña debe tener al menos 4 caracteres.\n")
        except ValueError:
            print("\nsolo puede ingresar números\n")


    while True:
        # El bucle es persistente hasta encontrar una combinación que coincida con los 4 parámetros para crear la contraseña: mayúsculas, minúsculas, números y símbolos

        clave = [random.choice(
            string.ascii_letters + string.punctuation + string.digits) for _ in range(largo)]
        clave = "".join(clave)

        expReg = "[" + re.escape(string.punctuation) + "]"
        expRegResul = re.findall(expReg, clave)

        expReg2 = "[" + re.escape(string.ascii_uppercase) + "]"
        expRegResul2 = re.findall(expReg2, clave)

        expReg3 = "[" + re.escape(string.ascii_lowercase) + "]"
        expRegResul3 = re.findall(expReg3, clave)

        expReg4 = "[" + re.escape(string.digits) + "]"
        expRegResul4 = re.findall(expReg4, clave)

        if len(expRegResul) > 0 and len(expRegResul2) > 0 and len(expRegResul3) > 0 and len(expRegResul4) > 0:
            break

    print("\nSu contraseña de", largo, "caracteres es:", clave, "\n")


def crearClaveLetras():

    clave = []  # se inicializa una lista vacía donde se guardarán los caracterees seleccionados
    # se crea una lista de referencia con letras mayúsculas, minúsculas, números y símbolos
    referencia = string.ascii_letters
    referencia = "".join(referencia)  # se une toda la lista

    try:
        # se le pide al usuario ingresar el largo de la contraseña
        largo = int(input("\ningrese el largo de la contraseña: \n").strip())
    except ValueError:
        print("\nsolo puede ingresar números\n")

    for i in range(largo):
        # se selecciona un caracter de la lista unida tantas veces como venga establecido por parametro
        digitoSeleccionado = random.choice(referencia)
        clave.append(digitoSeleccionado)  # se pasa el caracter a la lista

    clave = "".join(clave)  # unir la lista

    print("\nsu contraseña de ", largo, " caracteres es : " +
          clave+"\n")  # mostrar resultado por consola


def crearClaveNumerosLetras():

    clave = []  # se inicializa una lista vacía donde se guardarán los caracterees seleccionados
    referencia = string.ascii_letters+string.digits # se crea una lista de referencia con letras mayúsculas, minúsculas y números
    referencia = "".join(referencia)  # se une toda la lista

    try:
        # se le pide al usuario ingresar el largo de la contraseña
        largo = int(input("\ningrese el largo de la contraseña: \n").strip())
    except ValueError:
        print("\nsolo puede ingresar números\n")

    for i in range(largo):
        # se selecciona un caracter de la lista unida tantas veces como venga establecido por parametro
        digitoSeleccionado = random.choice(referencia)
        clave.append(digitoSeleccionado)  # se pasa el caracter a la lista

    clave = "".join(clave)  # unir la lista

    print("\nsu contraseña de ", largo, " caracteres es : " +
          clave+"\n")  # mostrar resultado por consola


def manual():

    return None


def menu():

    print("\n______GENERADOR DE CONTRASEÑAS V1.0_____")
    print("\n1.- Generador de contraseñas seguras")
    print("2.- Manual")
    print("3.- Salir\n")


def submenu():
    while True:
        print("\n ingrese el tipo de contraseña que necesita\n")
        print("\n1.- Solo Letras")
        print("2.- Letras y números")
        print("3.- Letras, núumeros y símbolos (recomendado)")
        print("4.- Volver al menú principal\n")

        try:
            opcion = int(input().strip())

            if opcion == 1:
                crearClaveLetras()        
        
            elif opcion == 2:
                crearClaveNumerosLetras()

            elif opcion == 3:
                crearClaveSegura()
            elif opcion == 4:
                selector()
            else:
                print("\nIngrese una opcion de la lista\n")

        except ValueError:
            print("\nValor ingresado no válido\n")


def selector():

    while True:
        menu()

        try:
            opcion = int(input("\nSeleccione una opción: \n").strip())

            if opcion == 1:
                submenu()

            elif opcion == 2:
                manual()

            elif opcion == 3:
                print("Has salido del programa")
                sys.exit()
            else:
                print("Ingrese una opcion de la lista")

        except ValueError:
            print("Valor ingresado no válido")


if __name__ == "__main__":
    selector()
