import random
from random import shuffle

letters=['A', 'B', 'C', 'D', 'E', 'F', 'G','H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q','R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z','a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i',
          'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's','t', 'u', 'v', 'w', 'x', 'y', 'z']
symbals=['!', '"', '#', '$', '%', '&', "'", '(', ')', '*', '+', ',', '-', '.', '/',':', ';', '<', '=', '>', '?', '@', '[', '\\', ']', '^', '_', '`', '{', '|', '}', '~']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
print("welcome to password generator!!")
ltr=int(input("enter how many letters u want in urs password:\n"))
sym=int(input("enter how many symbols u want in urs password:\n"))
num=int(input("enter how many numbers u want in urs password:\n"))
password=[]  #only lists can shuffle them self,so take list
for i in range(1,ltr+1):
    char=random.choice(letters)
    password +=char
for j in range(1,sym+1):
    char=random.choice(symbals)
    password +=char
for k in range(1,num+1):
    char=random.choice(numbers)
    password +=char

random.shuffle(password) #if u want shuffle, u need to call the shuffle module from random module,//list of password shuffled here

passwordstr="" #coverting that shuffled list of password to string
for a in password:
    passwordstr+=a
print(f"your strong password is: {passwordstr}")
