
def main_menu():
    while True:
        print("\nMenú Principal")
        print("1. Programa 1")
        print("2. Programa 2")
        print("3. Programa 3")
        print("4. Salir (EXIT)")

        choice = input("Elija un programa (1/2/3/4): ")

        if choice == "1":
            print("Bienvenido al programa 1")
            ejer()  
        elif choice == "2":
            print("Bienvenido al programa 2")
            ejer2()  ¿
        elif choice == "3":
            print("Bienvenido al programa 3")
            ejer3()  
        elif choice == "4" or choice.lower() == "exit":
            print("Saliendo del menú principal...")
            break
        else:
            print("Opción no válida. Por favor, seleccione una opción válida.")

if __name__ == "__main__":
    main_menu()

    from ejer import ejer
from ejer2 import ejer2
from ejer3 import ejer3


