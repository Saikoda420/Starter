import random
def main():
    num = random.randint(1,20)
    while(True):
        guess=int(input("Enter a number from 1 to 20: "))
        if(guess > num):
            print("Lower")
        if(guess < num):
            print("Higher")
        if(guess == num):
            print(f"Congrats! The number was {num}")
            return
try:
    main()
except ValueError:
    print("A number nigga")