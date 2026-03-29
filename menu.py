# Lista donde se guardan los datos
datos = []

#  FUNCIONES 

def agregar():
    nombre = input("Ingrese el nombre: ")
    datos.append(nombre)
    print(" Agregado correctamente")

def eliminar():
    nombre = input("Ingrese el nombre a eliminar: ")
    
    if nombre in datos:
        datos.remove(nombre)
        print("Eliminado correctamente")
    else:
        print(" No se encontró")

def buscar():
    nombre = input("Ingrese el nombre a buscar: ")
    
    if nombre in datos:
        print(" Sí existe en la lista")
    else:
        print(" No existe")

def mostrar():
    print("\n Lista actual:")
    for d in datos:
        print("-", d)

#MENÚ 

while True:
    print("\n--- MENÚ ---")
    print("1. Agregar")
    print("2. Eliminar")
    print("3. Buscar")
    print("4. Mostrar")
    print("5. Salir")

    opcion = input("Elige una opción: ")

    if opcion == "1":
        agregar()

    elif opcion == "2":
        eliminar()

    elif opcion == "3":
        buscar()

    elif opcion == "4":
        mostrar()

    elif opcion == "5":
        print(" Saliendo del programa...")
        break

    else:
        print(" Opción inválida")