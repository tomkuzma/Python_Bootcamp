import day15 as cm

day = int(input("Which day would you like to load? "))

match day:
    case 15:
        cm.coffeeMachine()
    case _:
        print("Not an option")
