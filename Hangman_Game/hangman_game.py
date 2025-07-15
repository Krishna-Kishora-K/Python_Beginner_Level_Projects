import random
import hangman_stages
from catagory_of_game import words
from hangman_stages import hangmanstages

print("Welcome to Hangman game..🤩")
category = random.choice(list(words.keys())) # Choose a random category
#print(list(words.keys()))
word = random.choice(words[category]).lower()  # Pick a random word from that category
print(f"The clue is, This is from {category} catagory")

lives=6
display=[]
for i in range(len(word)):
    display+='_'
print(display)
game_over=False
while not game_over:
    guessed_letter=input("Guess a letter: ").lower()
    for j in range(len(word)):
        letter =word[j]
        if letter==guessed_letter:
            display[j]=guessed_letter
    print(display)
    if guessed_letter not in word:
        lives-=1
        if lives==0:
            game_over=True
            print("You lose...!!")
            print(f"The answer is {word}")
    if '_' not in display:
        game_over=True
        print("You won...!!")
        print(f"The answer is {word}")
    print(hangmanstages[lives])
