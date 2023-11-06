from Ejer1 import Main
from Ejer2 import Main
from Ejer3 import Main

def mostrar_bienvenida(programa_nombre):
    print(f"Bienvenido al programa {programa_nombre}")

while True:
    print("Menú Principal:")
    print("1. Ejecutar Programa 1")
    print("2. Ejecutar Programa 2")
    print("3. Ejecutar Programa 3")
    print("4. Salir (EXIT)")

    opcion = input("Selecciona una opción: ")

    if opcion == "1":
        mostrar_bienvenida("Programa 1")
        Ejer1.main()
    elif opcion == "2":
        mostrar_bienvenida("Programa 2")
        programa2.main()
    elif opcion == "3":
        mostrar_bienvenida("Programa 3")
        programa3.main()
    elif opcion == "4" or opcion.lower() == "exit":
        print("Saliendo del Menú Principal...")
        break
    else:
        print("Opción no válida. Por favor, selecciona una opción válida.")
