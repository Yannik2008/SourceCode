from colorama import Fore, Back, Style
import time
import random

J_N = ["y", "n", "Y", "N"]
S_F = ["S", "F", "Quit"]
Y_N =["Y", "N"]
Wald_zahl = ["10", "1", "2", "3", "4", "5", "6", "7", "8", "9", "10"]
richtung = ["Norden", "Süden", "Osten", "Westen"]

name = input("Wie heißt du tapferer Held: ")
print(Fore.CYAN + f"Willkommen", Fore.MAGENTA + f"{name}", Fore.CYAN + "ich hoffe, du wirst auf deiner Reise in Dhalion viel Spaß haben!", Fore.GREEN)

time.sleep(2)

print("Hauptmenü:\n", Fore.MAGENTA + " Storymode: \n" "  Farmwelt: ")

Modus = " "
while Modus not in S_F:
    Modus = input("Wähle bitte einen Spielmodus aus (S/F):   ")

if Modus == "S":
    print("Du hast den Storymodus ausgewählt!")
    
    time.sleep(2)
    
    print(Fore.GREEN + "Bist du bereit den den Storymodus zu betreten?\n\n", Fore.RED + "Achtung, dein Spielstand wird weder gespeichert noch beim zweiten Mal bereitgestellt!", Fore.RESET)
    Start_S = ""
    while Start_S not in Y_N:
        Start_S = input(Fore.YELLOW + "Gibt bitte an ob du bereit bist (Y/N): ")
    
    if Start_S == "Y":
        print(Fore.GREEN + "Ok, du bist bereit!", Fore.RESET)
        print(Fore.BLACK + "Willkommen in der Welt von Dhalion.\nDu befindest dich am Anfang deiner Reise. Dein erstes Ziel wird sein,", Fore.MAGENTA + "den Stein von Leblian", Fore.BLACK + "zu finden.")
        time.sleep(7)
        print("Du wachst auf! Deine Augen schmerzen und deine Muskeln sind wie aus Blei. Als du richtig zudir kommst, merkst du, dass du auf einer Wiese gelegen hast.") 
        time.sleep(8)
        print("Du merkst, dass in Richtung", Fore.RED + "Norden", Fore.BLACK + "ein großer Wald beginnt.")
        time.sleep(5)
        print("In Richtung", Fore.RED + "Osten", Fore.BLACK + "schießen Berge in die Höhe.")
        time.sleep(5)
        print("Im", Fore.RED + "Süden", Fore.BLACK + "erblickst ein kleines Dorf mit einem Markt und")
        time.sleep(5)
        print("Im", Fore.RED + "Westen", Fore.BLACK + "beginnt ein Ozean.")
        Erste_Entscheidung = ""
        while Erste_Entscheidung not in richtung:
            Erste_Entscheidung = input("Bitte entscheide dich, wohin du gehen möchtest: ")
        if Erste_Entscheidung == "Norden":
            print(Fore.WHITE + "Du begibst dich in die Nähe des Waldes und schaust dich erstmal um.", Fore.RESET)
            print("Die Baume ragen über dir auf wie Riesen.")
            time.sleep(1.5)
            print("Auf einmal ertönt ein lautes Gebrüll!")
            time.sleep(2)
            print("Du drehst dich um und erblickst einen wütenden Wolf")
            time.sleep(2)
            print("Wie aus dem Nichts attackiert er dich.")
            time.sleep(1)
            Wald_GesuchteZahl = random.randint(1, 10)
            Wald_GesuchteZahl_geraten = int(input("Du hast nur eine Chance, errate die gesuchte Zahl von 1 bis 10:"))
            while Wald_GesuchteZahl_geraten not in range(1, 11):
                Wald_GesuchteZahl_geraten = int(input("Du hast nur eine Chance, errate die gesuchte Zahl von 1 bis 10:  "))
            if Wald_GesuchteZahl_geraten == Wald_GesuchteZahl:
                print("Super gemacht, du hast den Wolf besiegt.") 
            elif Wald_GesuchteZahl_geraten != Wald_GesuchteZahl:
                print(f"Tut mir leid, du hast die falsche Zahl genannt. Es war {Wald_GesuchteZahl}. Der Wolf hat dich erlegt. Vielleicht hast du beim nächste Mal mehr Glück.")
                quit()
        elif Erste_Entscheidung == "Osten":
            print("Noch in der Entwicklung")
        elif Erste_Entscheidung == "Süden":
            print("Noch in der Entwicklung")
        elif Erste_Entscheidung == "Westen":
            print("Noch in der Entwicklung")

        
    elif Start_S == "N":
        print(Fore.RED + "Schade, dass du nicht bereit bist, wir sehen uns wieder, wenn du es dir anders überlegt hast.", Fore.RESET)
        quit()

elif Modus == "F":
    print("Du hast den Farmmodus ausgewählt!")

elif Modus == "Quit":
    print(Fore.RED + "Programm beendet!", Fore.RESET)
    quit()