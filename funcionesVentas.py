from basecsv import *
from funcionesClientes import *
from funcionesInventario import *


def createNewSale(cliente: dict, book: dict, price: float, amout :int) -> dict:
    client = cliente['name']
    title = book['title']
    newSale = {
        "client" : client,
        "title" : title,
        "amout" : amout,
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
    client = validarNombreClient("client")
    book = validarNombre("title")
    amount = validarEntero()

    newSale = calculateNewSale(client,book,amount)

    if not newSale:
        print("error")
        return
    
    addNewSale(newSale)

