import turtle
import random

one=turtle.Turtle()
two=one.clone()
one.shape("turtle")
one.penup()
one.goto(0,120)

two.shape("turtle")
two.penup()
two.goto(0,-120)

die=[1,2,3,4,5,6]

print("!!!-----------------------WELCOME----------------------!!!")
print("!!!-------------------TO TURTLE RACE-------------------!!!")

print("----------------------------------------------------------")
print("|   **************************************************   |")
print("|   *                  1.    START                   *   |")
print("|   *                  2. HOW TO PLAY?               *   |")
print("|   *                  3.     QUIT                   *   |")
print("|   **************************************************   |")
print("----------------------------------------------------------")

ch=int(input("\nEnter your option!!!\n"))

if ch==2:
    print("AIM :\n"
          "The player whosee turtle reaches its home firs wins the game.\n")
    print("HOW TO PLAY?\n"
          "* Each player rolls a dice to get a number.\n"
          "* The player then moves their turtle by that many steps.\n"
          "* the players alternate turns until one of them wins!.\n")

elif ch==3:
    exit()

elif ch==1 :
    col1=input("\nPlayer1 choose your turtle colour\n"
               "* red       * blue      * green     * yellow\n\n\n")
    if col1=="red" or col1=="blue" or col1=="green" or col1=="yellow":
        one.fillcolor(col1)
    else :
        print("Colour not available......continue with violet colour !!!\n\n ")
        one.fillcolor("violet")

    col2=input("\nPlayer2 choose your turtle colour\n"
               "* red       * blue      * green     * yellow\n\n\n")
    if col2=="red" or col2=="blue" or col2=="green" or col2=="yellow":
        two.fillcolor(col2)
    else :
        print("Colour not available......continue with sky blue colour !!!\n\n ")
        two.fillcolor("sky blue")

    #creating homes for the turles

    #player_one home
    one.goto(300, 100)
    one.pendown()
    if col1 == "red" or col1 == "blue" or col1 == "green" or col1 == "yellow":
        one.pen(pencolor=col1,speed=10)
    else:
        one.pen(pencolor="violet")
    one.circle(40.0)
    one.penup()
    one.goto(0,140)
    one.pendown()
    one.pen(speed=2)

    #player_two home
    two.goto(300, -100)
    two.pendown()
    if col2 == "red" or col2 == "blue" or col2 == "green" or col2 == "yellow":
        two.pen(pencolor=col2,speed=10)
    else:
        two.pen(pencolor="sky blue")
    two.circle(40.0)
    two.penup()
    two.goto(0,-60)
    two.pendown()
    two.pen(speed=2)

    for i in range(40):
        if one.pos()>=(260,140):
            print("\n\nHURRAY!........PLAYER1 WINS!!!\n"
                  "   CONGRATULATIONS PLAYER1 :)\n\n"
                  "--------------------------------THANK YOU FOR PLAYING--------------------------------")
            break
        elif two.pos()>=(260,-60):
            print("\n\nHURRAY!........PLAYER2 WINS!!!\n"
                  "   CONGRATULATIONS PLAYER2 :)\n\n"
                  "--------------------------------THANK YOU FOR PLAYING--------------------------------")
            break
        else:
            one_turn=input("Player1 press 'Enter' to roll the die...!!!\n\n")
            outcome1=random.choice(die)
            print(outcome1)
            print("Steps to move ",10*outcome1,"\n\n")
            one.fd(10*outcome1)
            one.stamp()

            two_turn = input("Player2 press 'Enter' to roll the die...!!!\n\n")
            outcome2 = random.choice(die)
            print(outcome2)
            print("Steps to move ",10*outcome2, "\n\n")
            two.fd(10 * outcome2)
            two.stamp()

else:
    print("SORRY :( WRONG INPUT TRY NEXT TIME...!!!")
    exit()


C=input("PRESS ENTER TO EXIT...")


