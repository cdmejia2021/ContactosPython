import os

CARPETA = 'contactos/'  #Creando directorio
EXTENSION = '.txt'      #Extensión del archivo

class Contacto:
    def __init__(self, nombre, telefono, categoria):
        self.nombre = nombre
        self.telefono = telefono
        self.categoria = categoria

def app():

    #Revisa si la carpeta ya existe
    crear_directorio()

    mostrar_menu()

    #Ejecutar opción 
    preguntar = True

    while preguntar:
        opcion = input('Escoja la opción: \r\n')
        opcion = int(opcion)

        if opcion == 1:
            agregar_contacto()
            preguntar = False
        elif opcion == 2:
            editar_contacto()
            preguntar = False
        elif opcion == 3:
            mostrar_contactos()
            preguntar = False
        elif opcion == 4:
            buscar_contacto()
            preguntar = False
        elif opcion == 5:
            eliminar_contacto()
            preguntar = False
        else:
            print('Opción incorrecta. Intentalo de nuevo')

def eliminar_contacto():
    nombre_delete = input('Ingrese el nombre del contacto que desea eliminar: \r\n')
    
    try:
        os.remove(CARPETA + nombre_delete + EXTENSION)
        print('Eliminado correctamente')
    except:
        print('No se encontro el contacto')

def buscar_contacto():
    nombre_busqueda = input('Ingrese el nombre del contacto que desea buscar: \r\n')

    try:
        with open(CARPETA + nombre_busqueda + EXTENSION) as contacto:
            print('\r\n Información del contacto: \r\n')
            for linea in contacto:
                print(linea.rstrip())   #No doble salto de linea
            print('\r\n')
    except IOError: 
        print('El archivo no existe')
        print(IOError)

    #Reiniciar al menu
    app()

def mostrar_contactos():
    archivos = os.listdir(CARPETA)

    archivos_txt = [i for i in archivos if i.endswith(EXTENSION)]

    for archivo in archivos_txt:
        with open(CARPETA + archivo) as contacto:
            for linea in contacto:
                #Imprime los contenidos
                print(linea.strip())
            #Imprime un separador entre contactos
            print('\r\n')

def editar_contacto():
    nombre_edit = input('Escriba el nombre del contacto que desea editar: \r\n')

    #Revisar si el archivo ya existe antes de editarlo
    existe = existe_archivo(nombre_edit)

    if existe:
        with open(CARPETA + nombre_edit + EXTENSION, 'w') as archivo:
            #Editando campos
            nombre_contacto = input('Agregar nuevo nombre de contacto: \r\n')
            telefono_contacto = input('Agregar nuevo telefono: \r\n')
            categoria = input ('Agregar nueva categoria: \r\n')

            #Instanciar la clase
            contacto = Contacto(nombre_contacto, telefono_contacto, categoria)

            #Escribiendo el archivo
            archivo.write('Nombre: ' + contacto.nombre + '\n')
            archivo.write('Telefono: ' + contacto.telefono + '\n')
            archivo.write('Categoria: ' + contacto.categoria + '\n')

        #Renombrar el archivo CUIDADO CON LA IDENTACIÓNN PORQUE SI NO, NO CIERRA EL ARCHIVO
        os.rename(CARPETA + nombre_edit + EXTENSION, CARPETA + nombre_contacto + EXTENSION)

        #Contacto editado correctamente
        print('\r\nContacto editado correctamente\r\n')

    else:
        print('Ese contacto no existe')

    #Reiniciar la aplicación
    app()

def agregar_contacto():
    print('Escribir los datos para agregar el contacto: \r\n')
    nombre_contacto = input('Nombre contacto: \r\n')
    
    #Revisar si el archivo ya existe o no 
    existe = existe_archivo(nombre_contacto)
    if not existe:

        with open(CARPETA + nombre_contacto + EXTENSION, 'w') as archivo:   #Lo crea y lo asigna en carpeta  

            #Resto de los campos
            telefono_contacto = input('Telefono: \r\n')
            categoria = input('Categoria: \r\n')

            #Instanciar la clase
            contacto = Contacto(nombre_contacto, telefono_contacto, categoria)

            #Escribiendo el archivo
            archivo.write('Nombre: ' + contacto.nombre + '\n')
            archivo.write('Telefono: ' + contacto.telefono + '\n')
            archivo.write('Categoria: ' + contacto.categoria + '\n')

            #Mostrar un mensaje de texto
            print('\r\n Contacto creado correctamente \r\n')
    else:
        print('Ese contacto ya existe')

    app()

def mostrar_menu():
    print('Escoge una opción:')
    print('1) Agregar contacto')
    print('2) Editar contactos')
    print('3) Ver contactos')
    print('4) Buscar contactos')
    print('5) Eliminar contactos')

def crear_directorio():
    if not os.path.exists(CARPETA):
        #crear la carpeta
        os.makedirs(CARPETA)

def existe_archivo(nombre):
    return os.path.isfile(CARPETA + nombre + EXTENSION)

app()