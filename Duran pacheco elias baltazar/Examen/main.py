import paquete1.programa1 as programa1
import paquete2.programa2 as programa2
import paquete3.programa3 as programa3


def main():
    while True:
        print("\nMenú Principal:")
        print("1. Programa 1")
        print("2. Programa 2")
        print("3. Programa 3")
        print("4. Salir (EXIT con menú)")

        opcion = input("Elige una opción: ")

        if opcion == '1':
            print("Bienvenido al programa 1")
            programa1.main()
        elif opcion == '2':
            print("Bienvenido al programa 2")
            programa2.main()
        elif opcion == '3':
            print("Bienvenido al programa 3")
            programa3.main()
        elif opcion.lower() == 'exit con menú':
            break
        else:
            print("Opción no válida. Inténtalo de nuevo.")


if __name__ == "__main__":
    main()
