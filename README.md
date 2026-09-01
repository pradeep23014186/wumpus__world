<h1>ExpNo 9: Solve Wumpus World Problem using Python demonstrating Inferences from Propositional Logic</h1> 
<h3>Name: Pradeep Kumar G</h3>
<h3>Register Number: 212223230150</h3>
<H3>Aim:</H3>
<p>
    To solve  Wumpus World Problem using Python demonstrating Inferences from Propositional Logic
</p>
<h1>Problem Description</h1>
<hr>
<h2>Wumpus World</h2>
<hr>
The Wumpus world is a simple world example to illustrate the worth of a knowledge-based agent and to represent knowledge representation.

The figure below shows a Wumpus world containing one pit and one Wumpus. There is an agent in room [1,1]. The goal of the agent is to exit the Wumpus world alive. The agent can exit the Wumpus world by reaching room [4,4]. The wumpus world contains exactly one Wumpus and one pit. There will be a breeze in the rooms adjacent to the pit, and there will be a stench in the rooms adjacent to Wumpus.

![image](https://github.com/natsaravanan/19AI405FUNDAMENTALSOFARTIFICIALINTELLIGENCE/assets/87870499/cd6b68dc-c79f-4dcb-8126-04da90d65912)

<center>Wumpus World Representation</center>
<p>
This is a python program that uses propositional logic sentences to check which rooms are safe. 

It is assumed that there will always be a safe path that the agent can take to exit the Wumpus world. The logical agent can take four actions: Up, Down, Left and Right. These actions help the agent move from one room to an adjacent room. The agent can perceive two things: Breeze and Stench.
</p>

<hr>
<h1>Sample Input and Output:</h1>
<hr>

![image](https://github.com/natsaravanan/19AI405FUNDAMENTALSOFARTIFICIALINTELLIGENCE/assets/87870499/8696111a-a4a7-47cb-ba4b-43a4ef88573f)
![image](https://github.com/natsaravanan/19AI405FUNDAMENTALSOFARTIFICIALINTELLIGENCE/assets/87870499/4be5bf06-79fa-4fa0-9334-38a33f06060b)

<hr>
<h1>Program:</h1>

```py
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
```


<hr>
<h1>Output:</h1>
<img width="665" height="587" alt="output (1)" src="https://github.com/user-attachments/assets/4f1ee46c-4a03-4c39-a4a6-43d0131c3c06" />


<hr>


<h1>Result:</h1>

<p>
Thus, the Wumpus World problem was successfully solved using Python by applying propositional logic to navigate safely, avoid hazards, kill the Wumpus, and reach the gold.
</p>

<hr>
