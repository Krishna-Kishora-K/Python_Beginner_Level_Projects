import random

play=False
while not play:
    ha = input("enter rock or paper or seccer: ").lower()
    list = ['rock', 'paper', 'seccer']
    if ha not in list:
        print("invalid entry")
    else:
        ca = random.choice(list)
        print(f"computer choose {ca}")
        if ca == ha:
            print("it's an tie")
        elif (ha == 'rock' and ca == 'seccer') or (ha == 'paper' and ca == 'rock') or (
                ha == 'seccer' and ca == 'paper'):
            print("you won")
        else:
            print("you lose")
    ask=input("u want play again(yes or no):").lower()
    if ask=='no':
        play=True
    else:
        play=False