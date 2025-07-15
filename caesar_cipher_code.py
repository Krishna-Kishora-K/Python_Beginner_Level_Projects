alphabet=['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

def encryption(plain_text,shift_key):
    cipher_text=""
    for i in plain_text:
        position=alphabet.index(i)
        new_position=(position+shift_key)%26
        cipher_text+=alphabet[new_position]
    print(f"after encrypt the plain text is converted into: {cipher_text}")

def decryption(cipher_text,shift_key):
    plain_text=""
    for i in cipher_text:
        position=alphabet.index(i)
        new_position=(position-shift_key)%26
        plain_text+=alphabet[new_position]
    print(f"after decrypt the plain text is converted into: {plain_text}")

msg = False
while not msg:
    what_to_do = input("Enter 'encrypt' to encryption and enter 'decrypt' to descryption: ")
    text = input("enter the text you want to convert: ").lower()
    shift = int(input("enter the shift key: "))
    if what_to_do == 'encrypt':

        encryption(plain_text=text, shift_key=shift)
    elif what_to_do=='decrypt':

        decryption(cipher_text=text, shift_key=shift)
    else:
         print("goodbye")
    msg = input("you want to check again..?(yes or no): ")
    if msg == 'no':
        msg = True
    else:
        msg = False


