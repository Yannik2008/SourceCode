import random
import time

dice_len = 0
points = 0
dice = []

def main():
    if input("Throw: ") == "y":
        dice = throw_dice(6)
    else:
        dice = dice_input()
    print(dice)

    while True:
        obj_remove_dice()
        
        print(f"points: {points}")
        if points >= 350:
            if check_play() == False:
                print(f"Exited! {points}")
                break
        throw_dice(dice_len)
        print(f"points: {points}")
        print(f"dice: {dice}")
        
        time.sleep(2)
        

    return dice, points

    
def dice_input():
    global dice_len
    dice = [] #input list
    valid_input = ["1","2","3","4","5","6"]

    while len(dice) <6:
        input_dice = input("One of your dice: ")
        if input_dice in valid_input:
            dice.append(input_dice)
            print("valid")
            dice_len += 1
        else:
            print("No valid Input!")
    print(f"dice were input successfully: {dice}")
    
    dice.sort()
   
    return(dice)



def search_engine():
    global dice
    i1 = 0
    i2 = 0
    i3 = 0
    i4 = 0
    i5 = 0
    i6 = 0
    F4 = ["1","2","3","4","5","6"]
    
    

    for i in dice:
        if i == "1":
            i1 += 1
        if i == "2":
            i2 += 1
        if i == "3":
            i3 += 1
        if i == "4":
            i4 += 1
        if i == "5":
            i5 += 1
        if i == "6":
            i6 += 1
        else:
            pass

    if i1 == 6 or i2 == 6 or i3 == 6 or i4 == 6 or i5 == 6 or i6 == 6:
        return "F7"
    elif i1 == 5 or i2 == 5 or i3 == 5 or i4 == 5 or i5 == 5 or i6 == 5:
        return "F6"
    elif i1 == 4:
        return "F5_6"
    elif i6 == 4:
        return "F5_5"
    elif i5 == 4:
        return "F5_4"
    elif i4 == 4:
        return "F5_3"
    elif i3 == 4:
        return "F5_2"
    elif i2 == 4:
        return "F5_1"
    elif sorted(dice) == F4:
        return "F4"
    elif i1 == 3:
        return "F3_6"
    elif i6 == 3:
        return "F3_5"
    elif i5 == 3:
        return "F3_4"
    elif i4 == 3:
        return "F3_3"
    elif i3 == 3:
        return "F3_2"
    elif i2 == 3:
        return "F3_1"
    elif "1" in dice:
        return "F2"
    elif "5" in dice:
        return "F1"
        
    else:
        return None
        

def obj_remove_dice():
    global points 
    global dice_len
    global dice
    F_F = search_engine()
    
    if F_F != None:
        match F_F:
            case "F1":
                dice.remove("5")
                points += 50
                dice_len -= 1
                
            case "F2":
                dice.remove("1")
                points += 100
                dice_len -= 1

            case "F3_1":
                i = 0
                for i in range(3):
                    dice.remove("2")
                points += 200
                dice_len -= 3

            case "F3_2":
                i = 0
                while i < 3:
                    dice.remove("3")
                    i += 1
                points += 300
                dice_len -= 3

            case "F3_3":
                i = 0
                while i < 3:
                    dice.remove("4")
                    i += 1
                points += 400
                dice_len -= 3

            case "F3_4":
                i = 0
                while i < 3:
                    dice.remove("5")
                    i += 1
                points += 500
                dice_len -= 3

            case "F3_5":
                i = 0
                while i < 3:
                    dice.remove("6")
                    i += 1
                points += 600
                dice_len -= 3

            case "F3_6":
                i = 0
                while i < 3:
                    dice.remove("1")
                    i += 1
                points += 1000
                dice_len -= 3

            case "F4":
                points += 2000
                dice.clear()

            case "F5_1":
                i = 0
                while i < 4:
                    dice.remove("2")
                    i += 1
                points += 2000
                dice_len -= 4

            case "F5_2":
                i = 0
                while i < 4:
                    dice.remove("3")
                    i += 1
                points += 3000
                dice_len -= 4

            case "F5_3":
                i = 0
                while i < 4:
                    dice.remove("4")
                    i += 1
                points += 4000
                dice_len -= 4

            case "F5_4":
                i = 0
                while i < 4:
                    dice.remove("5")
                    i += 1
                points += 5000
                dice_len -= 4

            case "F5_5":
                i = 0
                while i < 4:
                    dice.remove("6")
                    i += 1
                points += 6000
                dice_len -= 4

            case "F5_6":
                points += 10000
                dice.clear()
                trigger_points()

            case "F6":
                points += 50000
                dice.clear()
                trigger_points()

            case _:
                print("lost")
                exit()                
    else:
        print("lost")
        exit()
    
    
    
        

def throw_dice(a):
    global dice_len
    dice_len = a
    dice.clear()
    for i in range(a):
        random_i = str(random.randint(1,6))
        dice.append(random_i)
    


def check_play():
    if input(f"Check for play: dice number {dice_len} ") == "N":
        return False
        
def trigger_points():
    print(points)
    exit()

    



print(main())
