import csv

#---------------------------permanencia inventario------------------------------


def saltoDeLinea():
    print("\n---------------------------------------------------------------------\n")

def loadInventario() -> list[dict]:
    try:
        with open("inventario.csv", "r", encoding="utf-8") as file:
            reader = csv.DictReader(file)
            inventario = list(reader)         
    except:
        inventario = []
    return inventario

inventario = loadInventario()


def saveInventario(inventario : list[dict]):
    try:
        with open("inventario.csv", "w", newline="", encoding="utf-8") as file:
            if inventario:
                fields = inventario[0].keys()
                writer = csv.DictWriter(file, fieldnames=fields)
                writer.writeheader()
                writer.writerows(inventario)
    except: print("error updating inventory")

#-----------------------------Permanencia clientes-----------------------------
def loadClientList() -> list[dict]:
    try:
        with open("clientList.csv", "r", encoding="utf-8") as file:
            reader = csv.DictReader(file)
            clientList = list(reader)         
    except:
        clientList = []
    return clientList

clientList = loadClientList()


def saveClientList(clientList :list[dict]):
    try:
        with open("clientList.csv", "w", newline="", encoding="utf-8") as file:
            if clientList:
                fields = clientList[0].keys()
                writer = csv.DictWriter(file, fieldnames=fields)
                writer.writeheader()
                writer.writerows(clientList)
    except: print("error updating client list")

#-----------------------Permanencia Ventas-------------------------------------------

def loadSalesList() -> list[dict]:
    try:
        with open("salesList.csv", "r", encoding="utf-8") as file:
            reader = csv.DictReader(file)
            salesList = list(reader)         
    except:
        salesList = []
    return salesList

salesList = loadSalesList()


def saveSalesList(salesList :list[dict]):
    try:
        with open("salesList.csv", "w", newline="", encoding="utf-8") as file:
            if salesList:
                fields = salesList[0].keys()
                writer = csv.DictWriter(file, fieldnames=fields)
                writer.writeheader()
                writer.writerows(salesList)
    except: print("error updating sales list")

# TODO: tengo 3 veces la misma !"#" función, tengo que buscar la forma de pasar un argumento y solo dejar 1 función

#--------------------------------------------------------------------------------------------------------------------
def loadNuevoInventario(archivo):
    try:
        with open(archivo, "r", encoding="utf-8") as file:
            reader = csv.DictReader(file)
            nuevoInventario = list(reader)
            return nuevoInventario
    except:
            print("error")
            return None
    

def sobrescribirInventario(nuevoInventario):

    inventario.clear()
    inventario.extend(nuevoInventario)
    saveInventario(inventario)
    return inventario

def exportarArchivo(archivo):
    with open(archivo, "w", newline="", encoding="utf-8") as file:
        writer = csv.DictWriter(file,fieldnames=["title","author","category","price","quantity"])
        writer.writeheader()
        writer.writerows(inventario)
   
    