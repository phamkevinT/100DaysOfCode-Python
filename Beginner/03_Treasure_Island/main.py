print('''
*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\` . "-._ /_______________|_______
|                   | |o;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/_____ /
*******************************************************************************
''')
print("Welcome to Treasure Island.")
print("Your mission is to find the treasure.")

# Flow Chart
# https://www.draw.io/?lightbox=1&highlight=0000ff&edit=_blank&layers=1&nav=1&title=Treasure%20Island%20Conditional.drawio#Uhttps%3A%2F%2Fdrive.google.com%2Fuc%3Fid%3D1oDe4ehjWZipYRsVfeAx2HyB7LCQ8_Fvi%26export%3Ddownload


userChoice = input("You come across a forked path. Do you go 'left' or 'right'? ").lower()

if (userChoice == 'left'):
  # Continue to 2nd stage
  userChoice = input("You emerge from the forest path. Infront of you is a large lake. Do you 'swim' across or 'wait' for someone with a boat to give you a ride? ").lower()

  if(userChoice == 'wait'):
    # Continue to 3rd stage
    userChoice = input("The mysterious man who gave you a ride takes you to an abandoned dungeon. You stumble across three colored doors. 'Yellow', 'Red', and 'Blue'. Which door do you enter? ").lower()

    if (userChoice == 'yellow'):
      print("You find treasure and come back rich!")
    elif (userChoice == 'red'):
      print("You entered a room engulped in flames. Game Over...")
    else:
      print("You enter a dark room. You hear growling behind you. Game Over...")

  else:
    print("You get attacked by group of trouts. Game Over...")
    
else:
  print("You fall into a deep hole. Game Over...")
