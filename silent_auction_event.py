import os

def heighest(biddin_details):              #jenny:5000,krishna:4000,karthik:500
    valuse=0
    winner=''
    for names in biddin_details:
        price=biddin_details[names]
        if price>valuse:
            valuse=price
            winner=names
    print(f"{winner} having a heigest bid of rupeese {valuse}")

details={}
bidder=False
while not bidder:
    name = input("enter ur name:")
    bid = int(input("enter ur bid amount:"))
    details[name]=bid
    ask=input("is any bidder are there 'yes'or'no':")
    if ask=='no':
        bidder=True
        heighest(details)
    else:
        bidder=False
        os.system('cls')




