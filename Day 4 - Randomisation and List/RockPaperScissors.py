import random
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
user_choice = int(input("What do you choose? Press 0 for Rock, 1 for paper and 2 for scissor\n"))
comp_choice = random.randint(0,2)
game_images = [rock, paper, scissors]
print("You Chose :\n")
print(game_images[user_choice])
print("\nComputer Chose:\n")
print(game_images[comp_choice])

if user_choice == 0:
  if (comp_choice == 0):
    print("It is a Draw!")
  elif (comp_choice == 1):
    print("You Lose!")
  else:
    print("You Win!")
elif user_choice == 1:
  if (comp_choice == 0):
    print("You Win!")
  elif (comp_choice == 1):
    print("It is a Draw!")
  else:
    print("You Lose!")
elif user_choice == 2:
  if (comp_choice == 0):
    print("You Lose!")
  elif (comp_choice == 1):
    print("You Win!")
  else:
    print("It is a Draw!")
else:
  print("Invalid Choice")

