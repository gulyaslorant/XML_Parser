import sys

import Werte_verketten
import functions

def weiter():
    while True:
        eingabe = input("Fortfahren?(J/N): ")
        if eingabe == "J":
            break
        elif eingabe == "N":
            print("Schade")
            sys.exit()
    return True

print("Skriptsammlung zur Unterstützung PM")
print("---------------------------------------------------")
print("1. Werte Verketten für Settexte")
print("2. Zählen von Chained Produkten")
print("1. Werte Verketten für Settexte")
print("1. Werte Verketten für Settexte")

print("___")
auswahl = int(input("Welches Skript möchten Sie ausführen? "))

if auswahl == 1:
    print("-------------------------")
    print("Möchtest Du Werte für ein Set verketten? ")
    print("")
    print("Hierfür muss folgende Datei korrekt hinterlegt sein!")
    print("... /Source/Kurzbeschreibung.xlsx muss im vorgegebenen Format vorhanden sein")
    weiter()
    functions.verketten()
elif auswahl == 2:
    print("-------------------------")
    print("Möchtest Du die Anzahl der Artikel für Chained Produkts in den Sets zählen? ")
    print("")
    print("Hierfür muss folgende Datei korrekt hinterlegt sein!")
    print("... /Source/Test_Matrix.xlsx muss im vorgegebenen Format vorhanden sein")
    weiter()
    functions.chained()

print("Vielen Dank und auf wiedersehen!")
