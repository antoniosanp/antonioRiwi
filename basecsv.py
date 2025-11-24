import csv
#---------------------------permanencia inventario------------------------------

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

#-----------------------------permanencia clientes-----------------------------
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