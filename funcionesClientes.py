from basecsv import *

#-----------------------------------------------------------------------------------

def validarNombreClient(nombre:str) -> str:
    while True:
        texto = input(f"enter client {nombre}: ")
        texto = texto.strip()
        if texto == "":
            print("can not be empty")
            continue
        return texto

def validarNivel() -> int:
    while True:
        try:
            nivel = int(input("Client level: "))
            if nivel >= 0 and nivel <= 5:
                return nivel
            else:
                print("level must be more than 0 and less or equal to 5")
        except: continue
    
#-------------------------------------------------------------------------------------
#------------------------Agregar cliente---------------------------------------------

def createClient(_name:str,_level: int) -> dict:
    newClient ={
        "name" : _name,
        "level" : _level
    }
    return newClient

def findClient(_name: str) -> dict:
    for client in clientList:
        if client["name"] == _name:
            return client
    return None

def addClient(_name:str, _level:int):
    encontrado = findClient(_name)
    if not encontrado:
        client = createClient(_name,_level)
        clientList.append(client)
        print("succes")
        saveClientList(clientList)
        return
    print("error"); return

def addClientMenu():
    print("adding a new client")
    name = validarNombreClient("name")
    level = validarNivel()

    addClient(name,level)
#---------------------------------------------------------------------------------------
#-----------------------Leer Clientes---------------------------------------------------


def printClient(client: dict):
    print(f"name: {client['name']:<20} | level: {client['level']:<20} ")



def showClientList():
    for client in clientList:
        printClient(client)

#------------------------------------------------------------------------------------
#----------------------Modificar Producto--------------------------------------------


def clietMenu():
    print("\n------------------------------------------Client Module......................................\n")
    while True:
        print("1: add new client ")
        print("2: client list")
        print("3: exit")

        opcion = input("choose an option: ")

        match opcion:
            case "1":
                addClientMenu()
            case "2":
                showClientList()
            case "3":
                break
            case _:
                print("invalid option")

#clietMenu()