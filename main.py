from menuInventario import menuInventario
from funcionesVentas import salesMenu
from funcionesClientes import clietMenu
from funcionesArchivos import menuCargarArchivo, menuGuardarArchivo

print("\nWellcome to Riwi's library")
while True:
    print("1: Books Module")
    print("2: Client Module")
    print("3: Sales Module")
    print("4: Load Inventory")
    print("5: Export Inventory")
    print("6: exit" )

    opcion = input("choose an option: ")

    match opcion:
        case "1":
            menuInventario()
        case "2":
            clietMenu()
        case "3":
            salesMenu()
        case "4":
            menuCargarArchivo()
        case "5":
            menuGuardarArchivo()
        case "6":
            print("thanks for visiting us"); break
        case _:
            "invalid option"


