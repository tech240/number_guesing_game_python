
import random
sec_num = random.randint(1,10)
attempts = 0
while True:
    user_inp = int(input("Guess a number between 1 and 10: "))
    attempts += 3
    if(user_inp == sec_num):
        print("You guessed it right!")
        break
    elif(user_inp < sec_num):
        print("Your guess is too low!")
    else:
        print("Your guess is too high!")

print("The correct number was:", sec_num)
print("Total attempts (counted as 3 points each):", attempts)


