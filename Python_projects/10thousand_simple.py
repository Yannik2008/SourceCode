import random, time
def main():
    input_dice()
    number_count()
    
    return points_evaluation()


dice = []

ranking = {
    "x2": 0,
    "x3": 0,
    "x4": 0,
    "x6": 0,
    "x5": 0,
    "x1": 0
}

def input_dice():
    global dice
    x = 1
    for i in range(0,6):
        dice_input = 0
        while True:
            try:
                dice_input = int(input(f"Dice {x}: ")) 
                if dice_input not in [1,2,3,4,5,6]:
                    raise ValueError("Invalid input!")

            except ValueError:
            
                print("Please input a number 1 through 6!")
            except:
                print("Please input a number 1 through 6!")
            else: 
                break
        dice.append(dice_input)
        x += 1
    return dice



# counts the different possible numbers and stores it in variables (x1-x6)
def number_count(): 
    global ranking

    # Reset ranking before counting
    for key in ranking:
        ranking[key] = 0

    # Count occurrences
    for i in dice:
        ranking[f"x{i}"] += 1

    return ranking  # Return the unmodified ranking


# finds the highest count of the inputted numbers depending on the ranking
def find_highest(): 
    highest_variable = None
    current_highest_value = 0  

    for key, value in ranking.items():
        adjusted_value = 1 if value == 2 else value  # Reduce 2 → 1
        if adjusted_value >= current_highest_value:
            current_highest_value = adjusted_value
            highest_variable = key
        if ranking.get("x5") == ranking.get("x1"):
            ranking["x5"] = 0
        if (ranking.get("x5") == 2) and (ranking.get("x1") == 1):
            ranking["x5"] = 0
    return highest_variable, current_highest_value



    return highest_variable, current_highest_value # Return only the variable name

    

def points_evaluation():
    highest_variable, count = find_highest()

    # Standard evaluation logic
    if highest_variable == "x1" and count in [1,2]:
        return 100
    
    elif highest_variable == "x5" and count in [1,2]:
        return 50  # Should give at least 50 points for two fives
    
    elif count == 2:
        return 0  # Only applies when no 1s or 5s exist
    
    elif highest_variable == "x1" and count >= 3:
        return 10**count
    
    elif highest_variable in ["x2","x3","x5","x4","x6"] and count >= 3:
        match highest_variable:
            case "x2":
                return 2 * (10 ** (count - 1))
            case "x3":
                return 3 * (10 ** (count - 1))
            case "x4":
                return 4 * (10 ** (count - 1))
            case "x5":
                return 5 * (10 ** (count - 1))
            case "x6":
                return 6 * (10 ** (count - 1))

    # Ensure 1s or 5s always give points even if they are not the highest_variable
    if ranking["x1"] >= 1:
        return 100
    elif ranking["x5"] >= 1:
        return 50  # This should fix the issue!

    return 0


    


def stress_test(total_iterations=10000, batch_size=1000):
    p10000 = 0
    best = 0
    best_list = []
    total_time = 0
    errors = 0
    iterations = 0

    while iterations < total_iterations:
        # Generate a new dice roll combination every batch_size runs
        dice_combination = [random.randint(1, 6) for _ in range(6)]
        
        for _ in range(batch_size):
            global dice, ranking
            dice = dice_combination.copy()  # Use the same combination for batch_size runs
            
            # Reset ranking dictionary before each evaluation
            ranking = {f"x{i}": 0 for i in range(1, 7)}

            # Measure execution time
            start_time = time.time()
            try:
                number_count()
                points = points_evaluation()
            except Exception as e:
                errors += 1
                print(f"Error on iteration {iterations}: {e}")
                points = "Error"

            total_time += time.time() - start_time
            iterations += 1

            # Print progress every batch_size iterations
            if iterations % batch_size == 0:
                print(f"Iteration {iterations}: Dice = {dice_combination}, Points = {points}")
            if points >=10000:
                p10000 += 1
            if points ==1000000:
                best += 1
                best_list.append(int(iterations))    # Stop if total_iterations reached
            if iterations >= total_iterations:
                break

    # Summary of test

    print(f"\nTotal execution time for {total_iterations} iterations: {total_time:.4f} seconds")
    print(f"Average time per run: {total_time / total_iterations:.6f} seconds")
    print(f"Total errors encountered: {errors}")
    print(f"Total iterations over/equal to 10000: {p10000}")
    print(f"Total iterations at the max: {best} \n at {best_list}")
    print(f"Ratio max to Hole: {best/(total_iterations/batch_size)}")

# Run stress test at 10000 tests a 1000 with the same combination
stress_test(10000000, 1)

# Run main()
#print(main())
