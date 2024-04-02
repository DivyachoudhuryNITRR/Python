import random  # to guess any random value  may be alphabet or any digits ranging 0 to 9 and a to z and A to Z 

# randNum=random.randint(1,5) #random integers will be generated inclusively 1 and 5
# print(randNum)

target=random.randint(1,100)

while True:
    userChoice=input("Guess the target or Quit(Q): ")
    if(userChoice=="Q"):
        break

    userChoice=int(userChoice)
    if(userChoice==target):
        print("Success : Correct Guess!!")
        break
    elif(userChoice<target):
        print("Your number was too small. Take a bigger Guess")
    else:
        print("Your number was too large. Take a smaller Guess")

print("------Game Over------")
