import os
import json
from os import system

# Verificar si el archivo 'libros.json' existe en el directorio actual
if not os.path.exists('libros.json'):
    # Si no existe, crear un archivo vacío
    with open('libros.json', 'w') as file:
        file.write('[]')

def select_option(options):

    for section in options:
        
        system('cls')
        
        
def menu():
    print("Bienvenidos a nuestra plataforma.\n¿Qué desea realizar?: ")
    print("1- Entrar a la librería")
    print("2- Salir de la librería")

    option_str = input("Ingrese la opción deseada: ")
    option = int(option_str)

    if option == 2:
        print("Ha salido de la plataforma. Hasta luego")
    else:
        print("Esa no es una opción válida")
        
    
    
    
    if option == 1:
        print("Estamos en la librería.\nQué desea realizar: ")
        print("1- Agregar un libro")
        print("2- Ver listado de libros")
        print("3- Modificar un libro")
        print("4- Borrar un libro")
        print("5- Salir")

   


        while True:
            search_option_str = input("Ingrese la opción de búsqueda: ")
            try:
                search_option = int(search_option_str)  # Intenta convertir la opción en un entero
                break  # Sal del bucle si la conversión tiene éxito
            except ValueError:
                print("Ingrese un número válido.")

        libros = guardar_libros()

    if search_option == 1:
            titulo = input("Ingrese el título del libro: ")
            libros.append({"titulo": titulo})
            print("Ha agregado el libro:", titulo)
            guardar_libros(libros)

           

    elif search_option == 2:
            print("Este es el listado de libros")
        
    
            
    elif search_option == 3:
        Modificar = input("Qué quiere modificar?: ")
        print("Ha modificado:", Modificar)

            

    elif search_option == 4:
            Borrar = input("Cuál quiere borrar?: ")
            print("Ha borrado:", Borrar)

            

    elif search_option == 5:
            print("Ha salido de la plataforma. Hasta luego")
    

 



def cargar_libros():
    try:
        with open('libros.json', 'r') as file:
            libros = json.load(file)
        return libros
    except FileNotFoundError:
        return []
    
    cargar_libros()




def guardar_libros(libros):
    with open('libros.json', 'w') as file:
        json.dump(libros, file)

        guardar_libros(libros)


       
        list_options = option['options']

        for index, option in enumerate(list_options):
            number = index + 1
            print(f'{index + 1} - {option}')
        print('0 - Salir\n')
        
        
        
        while not valid_option:
            selected = input('Ingrese su opción: ')
            
            try:
            
                selected = int(selected) -1
                
                if(selected < 0):
                    exit()
                    
                if(selected < len(list_options)):
                    print('Si')
                    valid_option = True
                    
                else:
                    print('Opción inválida. Ingrese una opción válida\n')
                    continue
                
            except:
                print('Ups, tipeaste un caracter. Ingresá una opción válida\n')
                continue

      

#Limpiar_pantalla()
#cargar_libros():
#guardar_libros():

