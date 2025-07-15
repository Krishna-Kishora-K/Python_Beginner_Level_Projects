import random

play=False
while not play:
    ha = input("enter rock or paper or secor: ").lower()
    list = ['rock', 'paper', 'secor']
    if ha not in list:
        print("invalid entry")
    else:
        ca = random.choice(list)
        print(f"computer choose {ca}")
        if ca == ha:
            print("it's an tie")
        elif (ha == 'rock' and ca == 'secor') or (ha == 'paper' and ca == 'rock') or (
                ha == 'secor' and ca == 'paper'):
            print("you won")
        else:
            print("you lose")
    ask=input("u want play again(yes or no):").lower()
    if ask=='no':
        play=True
    else:
        play=False