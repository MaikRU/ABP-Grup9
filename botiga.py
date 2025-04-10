# Autor - Miguel Rico
# Importem CSV (Per llegir els arxius CSV)
import csv

# Funcio que fa llegir el CSV
def lleguir_dades_botiga(nom_csv):
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

#Autor - Marc Sánchez i Miguel Rico
#Funció per calcular la facturaió mensual 
def calcular_facturacio():
    #Preparem el increment del valor perque crearem un "for", el valor començara des de 0
    total_sense_iva=0
    total_amb_iva=0 
    #Llegim la funció del csv, per llegir el arxiu 
    nom_arxiu_csv = "dades_botiga.csv"    
    lector=lleguir_dades_botiga(nom_arxiu_csv)
    #Començem el bucle perque fasi la operacio i sumi els valors introduits al inici 
    for i in lector:
        quantitat=int(i["Quantitat_Venuda"])
        preu_unitari = float(i["Preu_Unitari"])
        iva_percent = float(i["IVA"]) / 100
        subtotal = quantitat * preu_unitari
        iva=subtotal * iva_percent
        total=subtotal + iva
        #Fem el increment desde 0 amb subtotal i el total 
        total_sense_iva += subtotal 
        total_amb_iva += total
        round_sense_iva=round(total_sense_iva,2)
        round_amb_iva=round(total_amb_iva,2)
    #Mostra un titol i el valor total amb un "round" per a per arrodonir la xifra 
    print("\n===Facturació mensual===")
    print("Aquest mes s'ha facturat sense IVA:", round_sense_iva, "€")
    print("Total amb IVA", round_amb_iva, "€")

# Autor - Santiago Pirela i Miguel Rico
#Creem la funcio per calcular el stock disponible
def mostrar_stock():
    stockd= {}
    nom_arxiu_csv = "dades_botiga.csv"
    lector=lleguir_dades_botiga(nom_arxiu_csv)
    for i in lector:
        producte = i ["Producte"]
        stock = int(i["Estoc_Disponible"])
        if producte in stockd:
            stockd[producte] += stock
        else:
            stockd[producte] =stock

    print("\n--- Stock Disponible per a cada producte ---\n")
    for producte, stock in stockd.items():
        print(producte, stock, "unitats")

# Autor - Pedro Zamora i Miguel Rico        
# Diccionari per acumular la facturació per cada producte

def mostrar_3_millors():
    # Diccionari per acumular la facturació per cada producte
    producte_facturacio = {}
    nom_arxiu_csv = "dades_botiga.csv"
    lector = lleguir_dades_botiga(nom_arxiu_csv)
    for i in lector:
        producte = i["Producte"]
        quantitat = int(i["Quantitat_Venuda"])
        preu_unitari = float(i["Preu_Unitari"])
        # Calcular la facturació per aquesta línia
        facturacio = quantitat * preu_unitari
        if producte in producte_facturacio:
            producte_facturacio[producte] += facturacio
        else:
            producte_facturacio[producte] = facturacio
    # Inicialitzar una llista per als tres millors productes
    tres_millors = []
    # Cerca el diccionari per trobar els tres productes amb més facturació
    for producte, facturacio in producte_facturacio.items():
        # Afegir el producte actual a la llista
        tres_millors.append((producte, facturacio))
        # Ordenar la llista en ordre descendent segons la facturació
        tres_millors.sort(key=lambda x: x[1], reverse=True)
        # Mantenir només els tres primers elements a la llista
        tres_millors = tres_millors[:3]
    print("\n--- Tres productes amb més facturació ---")
    for producte, facturacio in tres_millors:
        print(producte,facturacio,"€")

# Autor - Miguel Rico
# Funció demana mostrar el "mostrar_menu" i dona la posiblitat de eligir una opció del 1-4
def menu():
    while True:
        mostrar_menu()
        opcio=input("Tria una opció 1-4: ")
        match opcio:
            case "1":
                calcular_facturacio()
            case "2":
                mostrar_stock()
            case "3":
                mostrar_3_millors()
            case "4":
                print("Sortin del programa, fins un altre!")
                break
            case _:
                print("Opció invalida, siusplau seleccioni del 1-4")
menu()        
               
        