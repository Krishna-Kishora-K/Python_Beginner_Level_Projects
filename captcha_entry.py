captcha_list = ["@Pl4#9k!","#W3r$d9*","9@x^T7!m","%aL#19Z!","*K2$p0!M"]
expected_input_list = ["Pl49k","W3rd9","9xT7m","aL19Z","K2p0M"]

print("Hi...! I am just making sure that you are not a robot")

def captcha():
    flag = True
    while flag:
        for i in range(5):
            print(f"ur captcha {captcha_list[i]}")
            entered = input("enter here:")
            if entered == expected_input_list[i]:
                print("you are not robot...!!!")
                flag = False
                break
            else:
                i += 1
                if i > 4:
                    print("you are a robot...Finally i got my family...")
                    flag=False
                else:
                    continue

captcha()