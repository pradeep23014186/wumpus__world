# WUMPUS GAME

wumpus = [
    ["Save", "Breeze", "PIT", "Breeze"],
    ["Smell", "Save", "Breeze", "Save"],
    ["WUMPUS", "GOLD", "PIT", "Breeze"],
    ["Smell", "Save", "Breeze", "PIT"]
]

# Initial Variables
row = 0
column = 0
arrow = True
player = True
score = 0

while(player):

    choice = input(
        "press u to move up\n"
        "press d to move down\n"
        "press l to move left\n"
        "press r to move right\n"
    )

    if choice == "u":
        if row != 0:
            row -= 1
        else:
            print("move denied")

        print("current location: ", wumpus[row][column], "\n")

    elif choice == "d":
        if row != 3:
            row += 1
        else:
            print("move denied")

        print("current location: ", wumpus[row][column], "\n")

    elif choice == "l":
        if column != 0:
            column -= 1
        else:
            print("move denied")

        print("current location: ", wumpus[row][column], "\n")

    elif choice == "r":
        if column != 3:
            column += 1
        else:
            print("move denied")

        print("current location: ", wumpus[row][column], "\n")

    else:
        print("move denied")

    # Check for Smell and arrow availability
    if wumpus[row][column] == "Smell" and arrow != False:

        arrow_choice = input(
            "do you want to throw an arrow-->\n"
            "press y to throw\n"
            "press n to save your arrow\n"
        )

        if arrow_choice == "y":

            arrow_throw = input(
                "press u to throw up\n"
                "press d to throw down\n"
                "press l to throw left\n"
                "press r to throw right\n"
            )

            # Throw arrow UP
            if arrow_throw == "u":

                if wumpus[row-1][column] == "WUMPUS":
                    print("wumpus killed!")
                    score += 1000
                    print("score: ", score)

                    wumpus[row-1][column] = "Save"
                    wumpus[1][0] = "Save"
                    wumpus[3][0] = "Save"

                else:
                    print("arrow wasted...")
                    score -= 10
                    print("score: ", score)

            # Throw arrow DOWN
            elif arrow_throw == "d":

                if wumpus[row+1][column] == "WUMPUS":
                    print("wumpus killed!")
                    score += 1000
                    print("score: ", score)

                    wumpus[row+1][column] = "Save"
                    wumpus[1][0] = "Save"
                    wumpus[3][0] = "Save"

                else:
                    print("arrow wasted...")
                    score -= 10
                    print("score: ", score)

            # Throw arrow LEFT
            elif arrow_throw == "l":

                if wumpus[row][column-1] == "WUMPUS":
                    print("wumpus killed!")
                    score += 1000
                    print("score: ", score)

                    wumpus[row][column-1] = "Save"
                    wumpus[1][0] = "Save"
                    wumpus[3][0] = "Save"

                else:
                    print("arrow wasted...")
                    score -= 10
                    print("score: ", score)

            # Throw arrow RIGHT
            elif arrow_throw == "r":

                if wumpus[row][column+1] == "WUMPUS":
                    print("wumpus killed!")
                    score += 1000
                    print("score: ", score)

                    wumpus[row][column+1] = "Save"
                    wumpus[1][0] = "Save"
                    wumpus[3][0] = "Save"

                else:
                    print("arrow wasted...")
                    score -= 10
                    print("score: ", score)

            arrow = False

    # Check if player reaches Wumpus
    if wumpus[row][column] == "WUMPUS":

        score -= 1000

        print(
            "\nWumpus here!!\n"
            "You Die\n"
            "And your score is: ",
            score,
            "\n"
        )

        break

    # Check if player reaches GOLD
    if wumpus[row][column] == "GOLD":

        score += 1000

        print(
            "\nYou found the GOLD!\n"
            "You Win!\n"
            "And your score is: ",
            score,
            "\n"
        )

        break

    # Check if player falls into PIT
    if wumpus[row][column] == "PIT":

        score -= 1000

        print(
            "Ahhhhh!!!!\n"
            "You fell in pit.\n"
            "And your score is: ",
            score,
            "\n"
        )

        break
