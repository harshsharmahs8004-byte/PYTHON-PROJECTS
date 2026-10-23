#TRESSURE ISLAND PROJECT
print("WELCOME TO TRESSURE ISLAND")
print("your mission is to find the tressure.")
choice1=input('you are at a cross road.where do you want to go?type "left" or "right" ')
if choice1=="right":
    print("you fall into a hole game over.")
else:
    print("you\'ve come to lake")
    
    print("there is an island in the middle of the lake.")
    
    choice2=input('type "wait" to wait for a boat.type"swim" to swim across.')
    if choice2=="swim":
        print("attacked by trout.game over")
    else:
        print("you arived at the island unharmed there in house with their door.one red.one yellow and one blue.which colour to you choose?")
 
 
    choice3=input('choose 1 door "blue"or "yellow" or "red" ') 
    if choice3=="red":
        print("burned by the fire game over")
    elif choice3=="blue":
        print("eaten by beast game over")
    elif choice3=="yellow":
        print("YOU WIN THE GAME CONGRATULATION......")
    else:
        print("game over ")
      
      