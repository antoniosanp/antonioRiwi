from basecsv import *
import tkinter as tk
from tkinter import filedialog

#tkinter, lib parainterfaz grafica de usuario para facilitar la selección de archivo a guardar/cargar

def seleccionarArchivoAbrir():
    ruta_archivo = filedialog.askopenfilename(
        title="Select a file",
        filetypes=[("All files", "*.*")]
    )
    return ruta_archivo 

def seleccionarArchivoGuardar():
    ruta_nueva = filedialog.asksaveasfilename(
        title="Save file as...",
        defaultextension=".csv",
        filetypes=[("Files CSV", "*.csv"), ("All files", "*.*")]
    )
    return ruta_nueva

ventana = tk.Tk()
ventana.withdraw() 

#-------------------------------------------------------------------------------

def menuCargarArchivo():
    print("\n------------------------------------------Load new inventory......................................\n")
    archivo = seleccionarArchivoAbrir()
    
    while True:
        
        print("\n1: Load inventory")
        
        print("2: exit")
        opcion = input("choose an option: ")

        saltoDeLinea()

        match opcion:
          
            case "1":
                nuevoInventario = loadNuevoInventario(archivo)
                sobrescribirInventario(nuevoInventario)

            case "2":
                 saltoDeLinea();break

            case _:
                print("invalid option")
#-----------------------------------------------------------------------------------------

def menuGuardarArchivo():
    print("\n------------------------------------------Export inventory......................................\n")
    archivo = seleccionarArchivoGuardar()
    exportarArchivo(archivo)
    print(f"inventory saved as: {archivo}")

#TODO: Copiar y pegar esto para permitir al usuario cargar y guardar los clientes y las ventas
   