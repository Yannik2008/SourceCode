# Dies ist ein Test
def Datenabfrage (**Daten):
    Vorname = Daten.get("Vorname")
    Nachname = Daten.get("Nachname")
    Alter = Daten.get("Alter")
    print(f"{Vorname} {Nachname} {Alter}")


x = str(input("Vorname: "))

Datenabfrage()
#Vorname=x, Vorname=y, Nachname=z 
#Nachname = str(input("Nachname: "))
#Alter = int(input("Alter: "))