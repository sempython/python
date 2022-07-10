# Vacation planning
# destination as array
# hotel as array

# Enter your name

# What destination do you want to travel to?
# 1. Paris - $550
# 2. Madird - $400
# 3. Rome - $500
# 4. New York - $450
# =====================
# >>> Madrid - $400

# How many days do you plan to stay?
# (do not allow input over 14)
# >>> 7

# What kind of hotel do you want to stay in?
# 1. One-star hotel ($50 a day)
# 2. Two-star hotel ($100 a day)
# 3. Three-star hotel ($150 a day)
# 4. Four-star hotel ($200 a day)
# >>> Two-star

# How many people are in your family?
# >>> 2

# Here is your total bill..
# ==================================
# Tickets to Madrid - $800 (destination * number of people that are traveling)
# Hotel - $700 (hotel * days)
# ==================================
# Total - $1500 (tickets + hotel)
# ==================================

# Is this too expensive?
# >>> Yes

# Ok Lets start again..
# What destination do you want to travel to?
# 1. Paris - $550
# 2. Madird - $400
# 3. Rome - $500
# 4. New York - $450

# ....

# Here is your total bill..
# ==================================
# Tickets to Madrid - $800 (destination * number of people that are traveling)
# Hotel - $200 (hotel * days)
# ==================================
# Total - $1000 (tickets + hotel)
# ==================================

# Is this too expensive?
# >>> No
# Done booking...

Doller = 0
endBooking = "No"
print ("Welcome to Vacation Plan")
print ("What is Your Name")
Name = input()
while (endBooking != "Yes"):
    print ("So Where do you Want to Go")
    print("1. USA - $500")
    print("2. Obama Land - $750")
    print("3. Minecraft - $100")
    print("4. Armenia - $250")
    Land = input()
    if (Land == "USA"):
        Doller = Doller + 500
    if (Land == "Obama Land"):
        Doller = Doller + 750
    if (Land == "Minecraft"):
        Doller = Doller + 100        
    if (Land == "Armenia"):
        Doller = Doller + 250
    print ("How many days do you plan to stay, it can only be 14 or Less")
    Day = int(input())
    print ("What kind of hotel do you want to stay in")
    print ("Type the Number of Stars you Want to Stay")
    print ("1. One-Star Hotel - $10 a day")
    print ("2. Two-Star Hotel - $25 a day")
    print ("3. Three-Star Hotel - $50 a day")
    print ("4. Four-Star Hotel - $100 a day")
    print ("5. Five-Star Hotel - $200 a day")
    Star = int(input())
    Y = Day * Star
    Doller = Doller + Y
    print ("How many people are in your family")
    (People) = input()
    (Doller) = int(Doller) * int(People)
    print ("Okay this is your Bill")
    print ("==================================")
    print ("Blah Blah Blah + Blah")
    print ("==================================")
    print ("Total - " + str(Doller))
    print ("==================================")
    print ("Is this too Expensive")
    endBooking = input()
    if (endBooking == true):
        print ("Okay lets Try Agian")
    if (endBooking != true):
        print ("Done Booking")
        break
