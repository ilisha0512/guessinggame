import random
print ("number guessing game")
number = random.randint (1,9)
chances = 0
print ("guess a number between 1 and 9")
while (chances < 5):
    guess = int(input("enter your guess!"))
    if (guess == number):
        print ("congratulations! you won!")
        break
    elif (guess < number):
        print ("your guess it too low, guess a higher number!")
    else: 
        print ("your guess is too high, guess a lower number!")
    chances = chances + 1
if not chances < 5:
    print ("you lost. the number is ", number)



