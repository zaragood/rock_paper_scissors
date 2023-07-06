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
user_choice = input("What do you choice? Type 0 for Rock, 1 for Paper, 2 for Scissors. ")

choices = [rock, paper, scissors]
user_choice_int = int(user_choice)
computer_choice = random.randint(0, 2)

if user_choice_int == 0 and computer_choice == 1:
  print(choices[user_choice_int])
  print(f"computer choose {computer_choice} {choices[computer_choice]}")
  print("You loss")
elif user_choice_int == 1 and computer_choice == 2:
  print(choices[user_choice_int])
  print(f"computer choose {computer_choice} {choices[computer_choice]}")
  print("You loss")
elif user_choice_int == 2 and computer_choice == 0:
  print(choices[user_choice_int])
  print(f"computer choose {computer_choice} {choices[computer_choice]}")
  print("You loss")
elif user_choice_int == computer_choice:
  print(choices[user_choice_int])
  print(f"computer choose {computer_choice} {choices[computer_choice]}")
  print("Its a tie")
elif user_choice_int >= 3 or user_choice_int < 0:
  print("invalid number")
  print("You loss")
else:
  print(choices[user_choice_int])
  print(f"computer choose {computer_choice} {choices[computer_choice]}")
  print("You Won")