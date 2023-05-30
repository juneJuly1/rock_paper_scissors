import random

user_wins = 0
computer_wins = 0 # testing

options = ['rock', 'paper', 'scissors']

while True:
    user_input = input('Type Rock/Paper/Scissors or Q to quit: ').lower()
    if user_input == 'q':
        break

    if user_input not in options:
        print()
        print('Please enter Rock, Paper, or Scissors')
        continue

    random_number = random.randint(0, 2)
    # rock: 0
    # paper: 1
    # scissors: 2
    computer_pick = options[random_number]
    print('You picked', user_input + '.')
    print('Computer picked', computer_pick + '.')

    if user_input == 'rock' and computer_pick == 'scissors':
        print('You won!')
        print()
        user_wins += 1
        continue
    elif user_input == 'paper' and computer_pick == 'rock':
        print('You won!')
        print()
        user_wins += 1
        continue
    elif user_input == 'scissors' and computer_pick == 'paper':
        print('You won!')
        print()
        user_wins += 1
        continue
    else:
        print('You lost!')
        print()
        computer_wins += 1
        continue

print('You won:', user_wins, 'times.')
print('Computer won:', computer_wins, 'times.')
print('Goodbye!')
