#Write 'hello world' to the console
print('Hello World')

#prompt the user to enter the number of rounds of rock paper scissors they would like to play
rounds = input('How many rounds would you like to play? ')
#if the rounds is not an integer greater than 0 then print an error message and prompt again until a valid number is entered
while not rounds.isdigit() or int(rounds) <= 0:
    print('Invalid input')
    rounds = input('How many rounds would you like to play? ')


#prompt the user to select one of three options - rock, paper, or scissors and warn the user if they make an invalid selection and prompt
#them to select again until a valid selection is made  
for i in range(int(rounds)):
    user_choice = input('Enter your choice (rock, paper, or scissors): ')
    while user_choice != 'rock' and user_choice != 'paper' and user_choice != 'scissors':
        print('Invalid input')
        user_choice = input('Enter your choice (rock, paper, or scissors): ')
    #generate a random choice for the computer
    import random
    computer_choice = random.choice(['rock', 'paper', 'scissors'])
    #print the choices of the user and the computer
    print('You chose:', user_choice)
    print('Computer chose:', computer_choice)
    #determine the winner of the round and print the result
    if user_choice == computer_choice:
        print('It is a tie!')
    elif user_choice == 'rock' and computer_choice == 'scissors':
        print('You win!')
    elif user_choice == 'scissors' and computer_choice == 'paper':
        print('You win!')
    elif user_choice == 'paper' and computer_choice == 'rock':
        print('You win!')
    else:
        print('Computer wins!')





