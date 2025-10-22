import random


print('🎉🐍 Welcome to the Python Emoji Guessing Game! 🐢✨')
print('I am thinking of a number between 1 and 20. Can you guess it?')
print('You have 5 tries! If you win, get ready for a funny punchline! 😎')

secret_number = random.randint(1, 20)
attempts = 5

for attempt in range(1, attempts + 1):
    print('\n' + "🤩" * 10)
    guess = input(f'Attempt {attempt}/{attempts}: Enter your guess: ')
    try:
        guess = int(guess)
    except ValueError:
        print('Oops! 🤡 Enter a whole number, please!')
        continue

    if guess == secret_number:
        print("🎊" * 5)
        print('CONGRATULATIONS! You guessed it right!')
        print('Winner winner, Python dinner! 🍜🐍')
        print("Here’s your winner emoji wall:\n" + "🏆" * 10)
        break
    elif guess < secret_number:
        print('Nope! My number is higher. 🔼')
    else:
        print('Nope! My number is lower. 🔽')
else:
    print("😭" * 5)
    print('Better luck next time! Python has a good poker face.')
    print(f'My secret number was {secret_number}.')
    print('Don’t worry, you’re still awesome! 😄')

print('Thanks for playing! 🎲 Try again for more Python fun!')
