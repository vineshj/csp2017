
# coding: utf-8

# In[ ]:

import random
def monty():
    start =  raw_input("""Welcome to the Monty Hall Riddle!
    
    My name is Vinesh. I will be your host for this game.
    
    Here's how it works. So there are three doors as you can see down below.
    Behind two of the doors, there is a goat. Behind one of the doors, there a
    brand new car! I will ask you which door you would like to choose. After I
    reveal a goat that is behind another door other than the one that you have
    selected, you have the option to stick with the door that you chose or 
    switch to one of the other doors.
    _____________________________
    |        |         |        |
    |  DOOR  |  DOOR   |  DOOR  |
    |    1   |    2    |    3   |
    |________|_________|________|
    
    ready to play? (yes)""") #This is the monty python riddle explanation with a little diagram
    while start == 'yes': #The player must agree to play the game before beginning
        prizedoor = int(random.randint(1,3)) #This selects the random door that the car is behind     
        guess1 =  int(raw_input("""Would you like to open door 1, door 2, or door 3? (just type the door number)"""))
        opendoor = int(random.randint(1,3)) #This is the door that the host opens
        while opendoor == prizedoor or opendoor == guess1: #Must make sure that the door that the host opens isn't the door that the player chose or the door that holds the car
            opendoor = int(random.randint(1,3))
        print """
        
        *****Your host opens door """ + str(opendoor) + """*****"""
        switchdoor = 0
        if prizedoor != guess1: #If door with car is not equal to the player's guess, then the door with the car becomes the switch door
            switchdoor = prizedoor
        else:
            switchdoor = int(random.randint(1,3))
            while switchdoor == prizedoor or switchdoor == opendoor:
                switchdoor = int(random.randint(1,3)) #creates the only door that the play can switch to
       
        switch =  int(raw_input(""" 
                You chose to open door """ + str(guess1) +""".
                Do you choose to swtich to door """ + str(switchdoor) + """ or stick with door """ + str(guess1) + """? (just type the door number)"""))
        #switch is the second input from the player
        if switch == prizedoor: #if the player wins
            print """
            
            Congratulations! You just won a car! You are so lucky!"""
        else: #if the player loses
            print """
            
            Sorry buddy. Maybe Next time. You got a goat."""
        playagain = raw_input("Do you want to play again? (yes/no):") #gives the player the option to play again
        if playagain == "no":
            break
        
                

monty()     


# In[1]:

yes


# In[ ]:



