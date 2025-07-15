from random import shuffle
from random import choice

letters=['A', 'B', 'C', 'D', 'E', 'F', 'G','H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q','R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z','a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i',
          'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's','t', 'u', 'v', 'w', 'x', 'y', 'z']
symbals=['!', '#', '$', '%', '&', '(', ')', '*', '+', '-', '/', '<', '=', '>', '?', '@', '[', '\\', ']', '^', '_', '{', '|', '}', '~']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
print("welcome to password generator!!")
ltr=int(input("enter the length of ur password:\n"))

password=[] #only lists can shuffle them self,so take list

if ltr%2==0:
    div=ltr/2
else:
    div=(ltr+1)/2
13
rem=ltr-div

if rem%2==0:
    remdiv=rem/2
else:
    remdiv=(rem+1)/2

new=rem-remdiv

for i in range(1,int(div)+1):
    char=choice(letters)
    password +=char
for j in range(1,int(remdiv)+1):
    char=choice(symbals)
    password +=char
for k in range(1,int(new)+1):
    char=choice(numbers)
    password +=char

shuffle(password) #if u want shuffle, u need to call the shuffle module from random module,//list of password shuffled here

passwordstr="" #coverting that shuffled list of password to string
for a in password:
    passwordstr+=a
print(f"your strong password is: {passwordstr}")