#剪刀石頭布遊戲

import random
s1 = ["scissors","rock","paper"]
computer_choice=random.choice(s1)

user_choice=input("enter your choice (scissors, rock, or paper): ")
user_choice=str(user_choice)

#for wrong user_input 
while user_choice not in s1:
    print("error input")
    user_choice=input("enter your choice (scissors, rock, or paper): ")
    user_choice=str(user_choice)
#determine result
if user_choice==computer_choice:
    print("computer_choice=",computer_choice)
    print("tie")
elif (user_choice=="scissors" and computer_choice=="rock") or (user_choice=="rock" and computer_choice=="paper") or user_choice=="paper" and computer_choice=="scissors":
    print("computer_choice=",computer_choice)
    print("you lose the game.")
elif (user_choice=="scissors" and computer_choice=="paper") or (user_choice=="paper" and computer_choice=="rock") or user_choice=="rock" and computer_choice=="scissors":
    print("computer_choice=",computer_choice)
    print("you win the game.")
