from basecsv import *

#-----------------------------Validaciones--------------------------------------

def validarNombre(nombre:str) -> str:
    while True:
        texto = input(f"enter {nombre} name: ")
        texto = texto.strip()
        if texto == "":
            print("can not be empty")
            continue
        return texto
    
def validarEntero() -> int:
    while True:
        try:
            val = int(input("enter quantity: "))
            if val > 0:
                return val
            else: print("quantity must be positive"); continue
        except ValueError:
            print("invalid entry")

def validarFloat() -> float:
    while True:
        try:
            val = float(input("enter value: "))
            if val > 0:
                return val
            else: print("value must be positive"); continue
        except ValueError:
            print("invalid entry")

#-------------------------------------------------------------------------------------
#------------------------Agregar Producto---------------------------------------------

def createItem(_titulo:str,_autor:str, _categoria:str, _precio: float, _cantidad: int) -> dict:
    newItem ={
        "title":_titulo,
        "author": _autor,
        "category": _categoria,
        "price": _precio,
        "quantity": _cantidad
    }
    return newItem

def findItem(_titulo: str) -> dict:
    for item in inventario:
        if item["title"] == _titulo:
            return item
    return None

def addItem(_titulo:str,_autor:str, _categoria:str, _precio: float, _cantidad: int):
    encontrado = findItem(_titulo)
    if not encontrado:
        item = createItem(_titulo,_autor,_categoria,_precio,_cantidad)
        inventario.append(item)
        print("succes")
        saveInventario(inventario)
        return
    print("error"); return

def addItemMenu():
    print("adding a new book")
    titulo = validarNombre("title")
    autor = validarNombre("author")
    categoria = validarNombre("categoty")
    precio = validarFloat()
    cantidad = validarEntero()

    addItem(titulo,autor,categoria,precio,cantidad)

#---------------------------------------------------------------------------------------
#-----------------------Leer Producto---------------------------------------------------


def printBook(item: dict):
    print(f"title: {item['title']:<20} | author: {item['author']:<20} | category: {item['category']:<20} | price: {item['price']:<10} | quantity {item['quantity']}")


def searchItemMenu():
    print("sarch a book: ")
    titulo = validarNombre("title")

    encontrado = findItem(titulo)

    if not encontrado:
        print(f"there is no book: {titulo}")

    else:
        printBook(encontrado)

def showInventario():
    for item in inventario:
        printBook(item)

#------------------------------------------------------------------------------------
#----------------------Modificar Producto--------------------------------------------

def updateItem(item : dict, _author = None , _category = None, _price = None, _quantity = None):

    if _author:
        item['author'] = _author
    if _category:
        item['categoty'] = _category
    if _price:
        item['price'] = _price
    if _quantity:
        item['quantity'] = _quantity

    print("Book updated: ")
    printBook(item)
    saveInventario(inventario)

def updateItemMenu():

    print("update a book")
    title = validarNombre("title")
    item = findItem(title)
    if not item:
        print(f"there is not book: {title}")
        return

    opcion = input(f"update author (y/n): ")
    if opcion == "y" or opcion == "Y":
        author = validarNombre("author")
    else: author = None

    opcion = input(f"update category (y/n): ")
    if opcion == "y" or opcion == "Y":
        category = validarNombre("category")
    else: category = None
    
    opcion = input(f"update price (y/n): ")
    if opcion == "y" or opcion == "Y":
        price = validarFloat()
    else: price = None

    opcion = input(f"update quantity (y/n): ")
    if opcion == "y" or opcion == "Y":
        quantity = validarEntero()
    else: quantity = None

    updateItem(item,author,category,price,quantity)
    
#-------------------------------------------------------------------------------------------
#------------------------Eliminar Producto--------------------------------------------------

def deleteItem(title: str):
    item = findItem(title)
    if item:
        inventario.remove(item)
        print(f"book {title} removed")
        saveInventario(inventario)
        return
    else: print(f"there ir no book: {title}")

def deleteItemMenu():
    print("delete a book")
    title = validarNombre(title)
    deleteItem(title)

#------------------------------------------------------------------------------------------





        