# Ejercicio 1 ANAGRAMAS
# Escribe una función que determine si dos cadenas son anagramas (tienen las mismas letras en el mismo número pero en un orden diferente).


import sys   


def ingresarCadena():

    """
    función que pide al usuario ingresar dos cadenas de texto,
    las compara y evalua si son identicas.

    Returns:
    Una tupla con las dos cadenas de texto ingresadas si son válidas, o False si son idénticas.
    """

    

    try:
        cadenaUno=input("\ningrese primera palabra: \n")

        #eliminar espacios vacíos y volver las letras mayúsculas en la primera variable
        cadenaUno=cadenaUno.upper().strip()

        cadenaDos=input("ingrese segunda palabra: \n")
            
        #eliminar espacios vacíos y volver las letras mayúsculas en la segunda variable
        cadenaDos=cadenaDos.upper().strip()

        print("\n validando cadenas de texto...")

        #validar si los caracteres ingresados son letras
        while cadenaUno.isalpha()==False or cadenaDos.isalpha()==False:
                
            print("\n cadena de texto no válida")
            print("\n intente nuevamente\n")
            cadenaUno=input("\ningrese primera palabra: \n")
            cadenaUno=cadenaUno.upper().strip()
                
            cadenaDos=input("ingrese segunda palabra: \n")
            cadenaDos=cadenaDos.upper().strip()


        print("\n datos ingresados correctamente...")

        #verificar si son iguales
        if cadenaUno== cadenaDos:
            print(" Las cadenas de texto ingresadas son idénticas")
            return False
                
        else:
            return (cadenaUno, cadenaDos)
            
    except ValueError:
        print("valor ingresado inválido")

        return None 


def compararLetras():

    """
    función que compara el largo de las cadenas de texto ingresadas en la
    funcion ingresarCadena() ademas revisa si las letras son coincidentes 

    Returns:
    None
    """

    #pasar resultado de la funcion ingresarCadena() a variable
    resulttadoFuncion = ingresarCadena()

    #validar retorno de la funcion ingresarCadena() distinto de falso
    if resulttadoFuncion!=False:

        #separar la tupla en dos variables
        cadenaUno, cadenaDos = resulttadoFuncion
        
        print("\n analizando datos...\n")

        #contador para ubicar las letras en la lista
        contador=0

        #lista vacía donde se alojarán las letras coinicdentes
        lista=[]

        #bucle anidado para recorrer las dos cadenas de texto
        for i in cadenaUno:

            for n in cadenaDos:
            
                if i==n:
                    #agregar las letras coindidentes
                    lista.append(i)
                    
                    #incrementar contador
                    contador+=1

        #contar el largo de la lista      
        largo=len(lista)

        #comparar primera y segunda cadena de texto
        if largo==len(cadenaUno):
            print("\nLas cadenas ingresadas son anagramas")
            print("\nEVALUACIÓN FINALIZADA")
        else:
            print("\nLas cadenas ingresadas no son anagramas")
            print("\nEVALUACIÓN FINALIZADA")
    else:
        print("\nLas cadenas ingresadas no son anagramas")
        print("\nEVALUACIÓN FINALIZADA")
            

#menu para interactuar con usuario
def menu():
    print("\n______MENU_______\n")
    print("1. Ingresar cadenas de texto a comparar")
    print("2. Manual")
    print("3. Salir\n")

#manual de uso
def manual():

    print("\n______Manual______\n\n.- Este programa compara únicamente\n cadenas de texto, para utilizarlo\n primero debe seleccionar la \n opción 1 del menú e ingresar los textos\n a comparar, este sin importar el orden\n de las letras evaluará como correcta\n la prueba si existen las mismas letras\n en las dos cadenas de texto.\n\n")
    

#control del programa
def main():
    
    while True:
        menu()

        try:
            opcion=int(input("Seleccione una opción: \n"))
            if opcion==1:
                compararLetras()
                
            elif opcion==2:
                manual()
            elif opcion==3:
                print("Has salido del programa")
                sys.exit()
            else:
                print("Ingrese una opcion de la lista")
        except ValueError:
            print("Valor ingresado no válido")
            
#punto de inicio
if __name__=="__main__":
    main()
    
        
        
