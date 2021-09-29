import random;

rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

# Put images into a list
choice_images = [rock, paper, scissors]

# Get user's decision and cast as integer
userDecision = int(input("What do you choose? Type '0' for Rock, '1' for Paper, '2' for Scisscors. "))

# Check if user typed in valid choice
if((userDecision > 2) or (userDecision < 0)):
  print("You typed an invalid number...")

else:

  # Retrieve user's choice from list
  print("You chose:")
  print(choice_images[userDecision])

  # Randomly get a number between 0 and 2 inclusive as computer's choice
  computerDecision = random.randint(0,2);

  # Retrieve computer's choice from list
  print("Computer chose:")
  print(choice_images[computerDecision])

  # Win/Lose Conditions

  # ROCK and SCISSORS Scenario
  if((userDecision == 0) and (computerDecision == 2)):
    print("You win!")
  elif((computerDecision == 0) and (userDecision == 2)):
    print("You lose...")

  # ROCK < PAPER < SCISSORS Scenario
  elif(computerDecision > userDecision):
    print("You lose...")
  elif(userDecision > computerDecision):
    print("You Win!")
  
  # TIE Scenario
  elif(userDecision == computerDecision):
    print("Draw!")