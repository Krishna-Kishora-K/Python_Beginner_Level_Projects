import random

import celebrity_list

print("'Higher and Lower Game'")
print(("Guess who have most follower..."))
def celeb(celebrity):
    name=celebrity['name']
    field=celebrity['field']
    country=celebrity['country']
    return f"{name},a {field},the country {country}"
def check_answer(guess,follow1,follow2):
    if follow1 < follow2:
        if guess == 2:
            return True
        else:
            return False
    else:
        if guess ==2:
            return False
        else:
            return True
def game():
    celeb2 = random.choice(celebrity_list.celebrities)
    score = 0
    cont_flag = False
    while not cont_flag:
        celeb1 = celeb2
        celeb2 = random.choice(celebrity_list.celebrities)
        while celeb1 == celeb2:
            celeb2 = random.choice(celebrity_list.celebrities)
        compare1 = print(f"compare 1: {celeb(celeb1)}")
        print("Vs")
        compare2 = print(f"compare 2: {celeb(celeb2)}")
        guess = int(input("enter ur guess'1 or 2':"))
        folwer1 = celeb1['follower']
        folwer2 = celeb2['follower']

        answer = check_answer(guess, folwer1, folwer2)

        if answer == True:
            score += 1
            print(f"u guessed correctly,ur score is {score}")
        else:
            print(f"u lose,ur final score is {score}")
            cont_flag = True
            want=input("if u want play again..?'yes or no':").lower()
            if want =='yes':
                return game()
            else:
                return
game()