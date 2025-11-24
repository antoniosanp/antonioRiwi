from funcionesInventario import addItemMenu, updateItemMenu, searchItemMenu, showInventario,deleteItemMenu

while True:
    print("1: add book")
    print("2: update book")
    print("3: delete book")
    print("4: search book")
    print("5: show all books")
    print("6: exit")
    opcion = input("choose an option: ")

    match opcion:
        case "1":
            addItemMenu()
        case "2":
            updateItemMenu()
        case "3":
            deleteItemMenu()
        case "4":
            searchItemMenu()
        case "5":
            showInventario()
        case "6":
            break
        case _: print("Invalid option")
    
    