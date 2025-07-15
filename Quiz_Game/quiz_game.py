
from quiz_questions import *

print("************************************")
print("____welcome to my quiz game____")
print("************************************")

def quiz():
    length = len(questions)
    score = 0
    for j in range(0, length):
        print(questions[j]['question'])
        for i in questions[j]['options']:
            print(i)
        answer = input("Enter ur answer:").upper()
        if answer == questions[j]['answer']:
            score += 1
            print("answer is write")
            print(f"ur score is {score}/{length}")
        else:
            print("answer is wrong")
            print(f"ur score is {score}/{length}")

    percentage = (score / length) * 100
    if percentage < 50:
        print(f"Your final score is {percentage}%")
        print("You failed")
    else:
        print(f"Your final score is {percentage}%")
        print("Congratulations,You completed the quiz")
    print("The answer is:")

    for k in range(0, length):
        correct = (questions[k]['answer'])
        if correct == 'A':
            corr_answer = 0
        elif correct == 'B':
            corr_answer = 1
        elif correct == 'C':
            corr_answer = 2
        elif correct == 'D':
            corr_answer = 3
        print(questions[k]['options'][corr_answer])

quiz()
