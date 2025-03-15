import random

def main():
    level = get_level("Level: ")
    num_guess(level)

def num_guess(num):
    a = random.randint(1, num)
    print(a)
    while True:
        try:
            b = int(input("Guess: "))
            if b < 1:
                raise ValueError
            if a > b:
                print("Too small")
            elif a < b:
                print("Too large!")
            else:
                print("Just Right!")
                return
        except ValueError:
            pass
    

def get_level(prompt):
    while True:
        try:
            lev = int(input(prompt))
            if lev > 0:
                return lev
            else:
                raise ValueError
        except ValueError:
            pass
    
main()