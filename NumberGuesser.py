import random


def g(level):
    while True:
        try:
            guess = int(input("Guess: "))
            if guess < 1:
                continue
            elif guess == level:
                print("Just right!")
                exit()
            elif guess > level:
                print("Too large!")
            elif guess < level:
                print("Too small!")

        except ValueError:
            continue


while True:
    n = int(input("Level: "))
    try:
        if n > 0:
            ran_num = random.randint(1, n)
            g(ran_num)

    except ValueError:
        break

