from menuInventario import menuInventario
from funcionesVentas import newSaleMenu
from funcionesClientes import clietMenu

print("\nWellcome to Riwi's library")
while True:
    print("1: Books Module")
    print("2: Client Module")
    print("3: Sales Module")
    print("4: exit" )

    opcion = input("choose an option: ")

    match opcion:
        case "1":
            menuInventario()
        case "2":
            clietMenu()
        case "3":
            newSaleMenu()
        case "4":
            print("thanks for visiting us"); break
        case _:
            "invalid option"


