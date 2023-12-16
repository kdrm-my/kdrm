import random

user_action = input("Choose a user action from rock or paper or scissor :-")

actions =["rock", "paper", "scissor"]
computer_action = random.choice(actions)

print(f"\nYou choose {user_action}, computer choose {computer_action}.")

if user_action == computer_action:
    print("The actions are tie.")
elif user_action == "rock":
    if computer_action == "scissor":
        print("Rock smashes scissor")
elif user_action == "paper":
    if computer_action == "rock":
        print("Paper covers rock")
elif user_action == "scissor":
    if computer_action == "paper":
        print("Scissor cut paper")
        
        
