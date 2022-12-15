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

if user_choice == 0:
  print("You Chose\n")
  print(f"{rock}\n")
  print("Computer Chose\n")
  if (comp_choice == 0):
    print(f"{rock}\n")
    print("It is a Draw!")
  elif (comp_choice == 1):
    print(f"{paper}\n")
    print("You Lose!")
  else:
    print(f"{scissors}\n")
    print("You Win!")
elif user_choice == 1:
  print("You Chose\n")
  print(f"{paper}\n")
  print("Computer Chose\n")
  if (comp_choice == 0):
    print(f"{rock}\n")
    print("You Win!")
  elif (comp_choice == 1):
    print(f"{paper}\n")
    print("It is a Draw!")
  else:
    print(f"{scissor}\n")
    print("You Lose!")
elif user_choice == 2:
  print("You Chose\n")
  print(f"{scissors}\n")
  print("Computer Chose\n")
  if (comp_choice == 0):
    print(f"{rock}\n")
    print("You Lose!")
  elif (comp_choice == 1):
    print(f"{paper}\n")
    print("You Win!")
  else:
    print(f"{scissors}\n")
    print("It is a Draw!")
else:
  print("Invalid Choice")

