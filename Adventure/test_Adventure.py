S_F = ["S", "F"]
Modus = ""
while Modus not in S_F:
    Modus = input("Wähle bitte einen Spielmodus aus (S/F):   ")

if Modus == "S":
    print("Du hast den Storymodus ausgewählt!")
    
elif Modus == "F":
    print("Du hast den Farmmodus ausgewählt!")

