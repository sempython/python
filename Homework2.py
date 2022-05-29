PlayerPoints1 = 0
PlayerPoints2 = 0
import random
print ("Welcom to Dice Wars")
print ("Player who Scores most points Wins")
print ("Player 1 Type your Name")
Player1 = str(input())
print ("Player 2 Type your Name")
Player2 = str(input())
print ("The Game is Starting")
while (PlayerPoints1 < 3) and (PlayerPoints2 < 3):
    Random1 = str(random.randint(1,10))
    print (Player1 + " has " + Random1 + " Points")
    Random2 = str(random.randint(1,10))
    print (Player2 + " has " + Random2 + " Points")
    if (Random1 > Random2):
        print (Player1 + " Won the First Round by " + Random1 + " Points")
        PlayerPoints1 = PlayerPoints1 + 1
    if (Random2 > Random1):
        print (Player2 + " Won the First Round by " + Random2 + " Points")
        PlayerPoints2 = PlayerPoints2 + 1
    if (Random1 == Random2):
        print ("Tie Nobody Wins")  
if (PlayerPoints1 > PlayerPoints2):
    print (Player1 + " Has Won the Game")
if (PlayerPoints2 > PlayerPoints1):
    print (Player2 + " Has Won the Game")
