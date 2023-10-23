#Validador de direcciones de correo electrónico:
#BUSCA CADENAS DE TEXTO QUE CORRESPONDAN A UN CORREO ELECTRONICO


import re
import tkinter as tk


#crear ventana de dialogo 
def crear_ventana_dialogo():
    ventana = tk.Tk()
    scrollbar = tk.Scrollbar(ventana)
    scrollbar.grid(row=0, column=4, sticky='ns')
    entrada_texto = tk.Text(ventana, height=20, width=80, wrap="word", yscrollcommand=scrollbar.set)
    entrada_texto.grid(row=0, columnspan=3)
    scrollbar.config(command=entrada_texto.yview)
    ventana.title("buscador de correos electronicos")
    
    return ventana, entrada_texto
    


def buscarCorreo(texto):
    """
    función que busca en una cadena de texto correos electronicos sin importar su tamaño

    explicacion:
    \b: Coincide con el límite de una palabra (para asegurarnos de que estamos capturando direcciones de correo independientes).
    [A-Za-z0-9._+-]+: Coincide con uno o más caracteres que pueden ser letras, números, puntos, guiones bajos.
    @: Coincide con el símbolo '@'.
    [A-Za-z0-9.-]+: Coincide con uno o más caracteres que pueden ser letras, números, puntos o guiones.
    \.: Coincide con un punto.
    [A-Z|a-z]{2,7}: Coincide con un minimo de 2 caracteres que pueden ser letras mayúsculas o minúscula

    Return: list 
    """
    print("analizado texto...")
    
    # Definir el patrón de la expresión regular
    patron = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9._%+-]+\.[A-Z|a-z]{2,7}\b'

    # Buscar todas las coincidencias // quedan en una variable con forma de lista
    direcciones = re.findall(patron, texto)


    return direcciones

def copiarPegar(ventana, entrada_texto):
    #funcion que copia el clipboard y lo inserta en el  cuadro de dialogo
    texto_pegado=ventana.clipboard_get()
    entrada_texto.insert(tk.END, texto_pegado)


def lista(texto, entrada_texto):

    print("texto ingresado correctamente...")
    lista= buscarCorreo(texto)
    entrada_texto.delete("1.0", tk.END)

    #contar las coinicdencias almacenadas
    cantidad=str(len(lista))
    
    if len(lista) >1:
        entrada_texto.insert("1.0","SE HAN ENCONTRADO "+cantidad+" CORREOS: \n\n" )
    elif len(lista)==1:
        entrada_texto.insert("1.0","SE HA ENCONTRADO "+cantidad+" CORREO: \n\n" )
    else:
        entrada_texto.insert("1.0","NO EXISTEN CORREOS EN LA CADENA DE TEXTO INGRESADA: \n\n" )
    
    #desempaquetamos la lista de modo que se muestren de forma ordenada para su fácil comprensión
    for direccion in lista:
        entrada_texto.insert(tk.END,direccion+"\n" )

    print("generando lista de resultados...") 


def ingresarTexto():

    # capa interaccion con el usuario
    ventana, entrada_texto = crear_ventana_dialogo()

    etiqueta = tk.Label(ventana, text="pega el texto aquí")
    etiqueta.grid(row=1, column=1)


    marco = tk.Frame(ventana, padx=10, pady=10)
    marco.grid(row=2, columnspan=3)

    boton_pegar = tk.Button(marco, text="pegar texto", width=15, command=lambda:copiarPegar(ventana, entrada_texto ))
    boton_pegar.grid(row=0, column=0)
    
    boton_buscar = tk.Button(marco, text="Buscar Correos", width=15, command=lambda: lista(entrada_texto.get("1.0",tk.END), entrada_texto))
    boton_buscar.grid(row=0, column=1 )

    boton_limpiar = tk.Button(marco, text="borrar", width=15, command=lambda:entrada_texto.delete("1.0", tk.END))
    boton_limpiar.grid(row=0, column=2)
    ventana.mainloop()


if __name__=="__main__":
    
    ingresarTexto()        
    
    
    
        
        



        
        

    
