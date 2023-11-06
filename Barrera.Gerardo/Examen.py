import ejercicio1
import ejercicio3
import ejercicio2


#import ejercicio2
#import ejercicio3


def show_menu():
    print("1. ejercicio 1")
    print("2. ejercicio 2")
    print("3. ejercicio 3")
    print("EXIT para salir")



def main():
    show_menu()
    while True:
        option = input("Ingrese el número del programa a ejecutar: ")
        if option == "1":
            print("Bienvenido al ejercicio 1")
            ejercicio1.main()
        elif option == "2":
            print("Bienvenido al ejercicio 2")
            ejercicio2.main()
        elif option == "3":
            print("Bienvenido al ejercicio 3")
            ejercicio3.main()
        elif option.upper() == "EXIT":
            break
        else:
            print("Opción inválida, por favor intente de nuevo.")


main()