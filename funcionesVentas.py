from basecsv import *
from funcionesClientes import *
from funcionesInventario import *


def createNewSale(cliente: dict, book: dict, price: float, amout :int) -> dict:
    client = cliente['name']
    title = book['title']
    newSale = {
        "client" : client,
        "title" : title,
        "amout" : amout,  # si me da tiempo, hago la correción por amount
        "total" : amout*price
    }

    book['quantity'] = int(book["quantity"]) - amout
    return newSale



def calculateNewSale(client:str,title:str,amout:int):
    cliente = findClient(client)
    book = findItem(title)

    if not cliente or not book:
        print("error")
        return None
    if int(book['quantity']) < amout: #csv no manejra tipo de dato, me da miedo que me rompa el programa
        print("error")
        return None
    
    normalPrice = float(book['price'])
    descuento = int(cliente['level'])

    if descuento > 0:
        descuento  *= 10
        normalPrice = normalPrice - (normalPrice/100)*descuento

    return createNewSale(cliente,book,normalPrice,amout)

def addNewSale(sale:dict):

    salesList.append(sale)
    print(sale)
    saveSalesList(salesList)
    saveInventario(inventario)

#-----------------------------------------------------------------------------------------------------

def newSaleMenu():

    print("new sale ")
    client = validarNombreClient("name")
    book = validarNombre("title")
    amount = validarEntero()

    newSale = calculateNewSale(client,book,amount)

    if not newSale:
        print("error")
        return
    
    addNewSale(newSale)

def showSales():
    for sale in salesList:
        print(f"Book: {sale['title']:<20} | amount: {sale['amout']:<8} | total: {sale['total']:<10} | client: {sale['client']}")

#-----------------------------------------------------------------------------------------------------------
#------------------------------------Funciones para Bestsellers---------------------------------------------

def bestSellers():
    bestSell = {}

    for sale in salesList:
        book = sale['title']
        amount = sale['amout']
        if book not in bestSell:
            bestSell[book] = 0
        bestSell[book] = int(bestSell[book])
        bestSell[book] += int(amount)
    sortedBySells = dict(sorted(bestSell.items(), key=lambda item: item[1], reverse=True))

    if len(sortedBySells) >= 3:
        contador = 1
        for  key, value in sortedBySells.items():
            print(f"{contador}:  Book: {key} | Sells: {value}   ")
            contador += 1
            if contador >= 4: break
        print("\n----------------------------------------")
    else: print("there are not enough books for statistics")

def totalSells():
    totalBooks = len(inventario)
    totalBooksSold = 0
    totalProfit = 0

    for sale in salesList:
        totalBooksSold += int(sale['amout'])
        totalProfit += float(sale['total'])
    
    print("Sales Inform: \n")

    print(f"Unic Books: {totalBooks} ")
    print(f"Total books sold: {totalBooksSold}")
    print(f"Todal profit: {totalProfit}\n")

# TODO: refactorizar la estructura de las ventas, como las ventas no registran autor, me es muy difícil hacer un set/dict con las ventas por autor



   


def salesMenu():
    print("\n------------------------------------------Sales Module......................................\n")
    while True:
        print("1: Register new sale")
        print("2: Sales history")
        print("3: Top bestsellers" )
        print("4: Total sales")
        print("5: Exit")

        opcion = input("choose an option: ")
        saltoDeLinea()

        match opcion:
            case "1":
                newSaleMenu()
                saltoDeLinea()
            case "2":
                showSales()
                saltoDeLinea()
            case "3":
                bestSellers()
                saltoDeLinea()
            case "4":
                totalSells()
                saltoDeLinea()
            case "5":
                saltoDeLinea(); break
            case _: print("invalid option"); saltoDeLinea()
