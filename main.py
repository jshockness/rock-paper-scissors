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

#Write your code below this line 👇
import random
# put images in list and use index to use them
game_img =[rock, paper, scissors]

player_choice = int(input("What do you choose? 0 for Rock, 1 for Paper, 2 for Scissors.\n "))

# Determines Winner Logic
if player_choice >= 3 or player_choice < 0:
  print("Invalid selection you lose.")
else:
  print(game_img[player_choice])
  
  computer_choice = random.randint(0, 2)
  print(game_img[computer_choice])
  
  if player_choice == 0 and computer_choice == 2:
    print("You Win!")
  elif computer_choice == 0 and player_choice == 2:
    print("You lose.")
  elif player_choice > computer_choice:
    print("You Win!")
  elif computer_choice > player_choice:
    print("You lose.")
  elif computer_choice == player_choice:
    print("Game results in a Draw.")
# Outputs drawing of rock, paper, and scissors for player and computer
# print(player_choice)
# if player_choice == 0:
#   print(rock)
# elif player_choice == 1:
#   print(paper)
# elif player_choice == 2:
#   print(scissors)
 
# print(computer_choice)
# if computer_choice == 0:
#   print(rock)
# elif computer_choice == 1:
#   print(paper)
# elif computer_choice == 2:
#   print(scissors)

