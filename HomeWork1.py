# Dice wars...
# Player who scores most points win...

# Enter player1 name

# Enter player2 name

# Hi player1 and player2, the game is starting..

# There will be 5 rounds

# player1 is rolling a dice between 1-10
# player1 rolls: 7

# player2 is rolling a dice between 1-10
# player2 rolls: 4

# Round 1 is over... player1 has 1 points, player2 has 0 points

# player1 is rolling a dice between 1-10
# player1 rolls: 3

#w player2 is rolling a dice between 1-10
# player2 rolls: 5

# Round 2 is over... player1 has 1 points, player2 has 1 points

# player1 is rolling a dice between 1-10
# player1 rolls: 1

# player2 is rolling a dice between 1-10
# player2 rolls: 7

# Round 3 is over... player1 has 2 points, player2 has 1 points
# Game is over...
# player2 won by 2-1

# OR
# Game is over...
# Tie, score is 1-1

PlayerPoints1 = 0
PlayerPoints2 = 0
import random
print ("Welcom to Dice Wars")
print ("The Player who Scores most points Wins")
print ("Player 1 Type your Name")
Player1 = str(input())
print ("Player 2 Type your Name")
Player2 = str(input())
print ("The Game is Starting")
while (PlayerPoints1 < 3) and (PlayerPoints2 < 3):
    Random1 = int(random.randint(1,10))
    print (Player1 + " has " + str(Random1) + " Points")
    Random2 = int(random.randint(1,10))
    print (Player2 + " has " + str(Random2) + " Points")
    if (Random1 > Random2):
        print (Player1 + " Won this Round by " + str(Random1) + " Points")
        PlayerPoints1 = PlayerPoints1 + 1
    if (Random2 > Random1):
        print (Player2 + " Won this Round by " + str(Random2) + " Points")
        PlayerPoints2 = PlayerPoints2 + 1
    if (Random1 == Random2):
        print ("Tie Nobody Wins")  
if (PlayerPoints1 > PlayerPoints2):
    print (Player1 + " Has Won the Game")
if (PlayerPoints2 > PlayerPoints1):
    print (Player2 + " Has Won the Game")
