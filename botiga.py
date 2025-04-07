# Autor - Miguel Rico
# Importem CSV (Per llegir els arxius CSV)
import csv

# Funcio que fa llegir el CSV
def llegir_dades_botiga(nom_csv):
    dades=[]
    with open(nom_csv,mode='r', encoding='utf-8') as fitxer:
        lector=csv.DictReader(fitxer)
        for i in lector:
            dades.append(i)
    return dades    


# Autor - Miguel Rico
# Funció que ens mostra el menu visualment       
def mostrar_menu():
    print("====Benvingut a la APP de facturacio TechPlay====")
    print("1 - Calcular la facturacio mensual")    
    print("2 - Stock disponible")
    print("3 - Tres productes mes facturats")    
    print("4 - Sortir de l'APP")    



# Autor - Miguel Rico
# Funció demana mostrar el "mostrar_menu" i dona la posiblitat de eligir una opció del 1-4
def menu():
    while True:
        mostrar_menu()
        opcio=input("Tria una opció 1-4: ")
        match opcio:
            case "1":
                print("En construccio")
            case "2":
                print("En construccio")
            case "3":
                print("En construccio")
            case "4":
                print("Sortin del programa, fins un altre!")
                break
            case _:
                print("Opció invalida, siusplau seleccioni del 1-4")
menu()        
               
        