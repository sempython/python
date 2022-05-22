# Player who scores most points win...

# Enter player1 name

# Enter player2 name

# Hi player1 and player2, the game is starting..
# There will be 3 rounds

# player1 is rolling a dice between 1-10
# player1 rolls: 7

# player2 is rolling a dice between 1-10
# player2 rolls: 4

# Round 1 is over... player1 has 7 points, player2 has 4 points

# player1 is rolling a dice between 1-10
# player1 rolls: 3

#w player2 is rolling a dice between 1-10
# player2 rolls: 5

# Round 2 is over... player1 has 10 points, player2 has 9 points

# player1 is rolling a dice between 1-10
# player1 rolls: 1

# player2 is rolling a dice between 1-10
# player2 rolls: 7

# Round 3 is over... player1 has 11 points, player2 has 16 points
# Game is over...
# player2 won with 16 points

total1 = 0
total2 = 0
roundNumber = 0
import random
print ("Welcome to Dice game!")
print ("Player one type your Name")
player1 = str(input())
print ("Know Player two type your Name")
player2 = str(input())
while (roundNumber < 3):
    total1 = total1 + (random.randint(1,10))
    print (player1 + " has " + str(total1)  + " Points")
    total2 = total2 + (random.randint(1,10))
    print (player2 + " has " + str(total2)  + " Points")
    roundNumber = roundNumber + 1
print ("Game is over")
if (total1 > total2):
    print (player1 + " Wins with " + str(total1) + " points")
if (total1 < total2):
    print (player2 + " Wins with " + str(total2) + " points")
if (total1 == total2):
    print ("Tie")
