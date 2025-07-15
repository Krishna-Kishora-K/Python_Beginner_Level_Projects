import random

easy_level=15
hard_level=8
def level_of_game(level):
    if level=='easy':
        return easy_level
    elif level=='hard':
        return hard_level
    else:
        return

def guessing(answer,guessed_number,attempt):
    # if guessed_number-2<answer and guessed_number+2>answer:
    #     print("u r too close for that number...!")
    #     return attempt-1
    #  elif guessed_number+2>answer:
    #      print("u r too close for that number...!")
    #     return attempt - 1
    if guessed_number>answer:
        print("u choose very high number")
        return attempt-1
    elif guessed_number<answer:
        print("u choose very low number")
        return attempt-1
    else:
        print(f"u guessed it correctly,the answer is {answer}")
        return

def game():
    print("let me think a number between 1 to 100")
    answer = random.randint(1, 100)
    level = input("enter the level of game:").lower()
    attempt = level_of_game((level))
    if attempt!=easy_level and  attempt!=hard_level:
        print("u gave wrong level,pleas play again...!")
        return game()
    guessed_number = 0
    while guessed_number != answer:
        print(f"you have {attempt} to guess the number")
        guess = int(input("guess a number:"))
        attempt = guessing(answer, guess, attempt)
        if attempt == 0:
            print("u lose...!")
            print(f"the answer is {answer}")
            return
        elif answer==guess:
            return
        else:
            print("guess again")

game()