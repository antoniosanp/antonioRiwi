from funcionesInventario import addItemMenu, updateItemMenu, searchItemMenu, showInventario,deleteItemMenu
from basecsv import *

def menuInventario():
    print("\n------------------------------------------Books Module......................................\n")
    while True:
        print("1: add book")
        print("2: update book")
        print("3: delete book")
        print("4: search book")
        print("5: show all books")
        print("6: exit")
        opcion = input("choose an option: ")

        saltoDeLinea()

        match opcion:
            case "1":
                addItemMenu()
                saltoDeLinea()
            case "2":
                updateItemMenu()
                saltoDeLinea()
            case "3":
                deleteItemMenu()
                saltoDeLinea()
            case "4":
                searchItemMenu()
                saltoDeLinea()
            case "5":
                showInventario()
                saltoDeLinea()
            case "6":
                saltoDeLinea(); break
            case _: print("Invalid option"); saltoDeLinea()
    
    