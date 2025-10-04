import random
num = random.randint(1,100)
while True:
    guess = int(input("Guess: "))
    if guess < num:
        print("Too low")
    elif guess > num:
        print("Too high")
    else:
        print("Correct!")
        break
