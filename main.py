import random as ran

while True:

    cpu_choice = ran.randrange(0, 2)

    if cpu_choice == 0:
        cpu_choice = 'rock'
    elif cpu_choice == 1:
        cpu_choice = 'paper'
    elif cpu_choice == 2:
        cpu_choice = 'scissors'

    usr_choice = input("Rock, Paper, Scissors: ")
    usr_transl = usr_choice.lower()

    if usr_transl == cpu_choice:
        result = "it's a tie!"
    elif usr_transl == 'rock' and cpu_choice == 'paper':
        result = "you lose!"
    elif usr_transl == 'rock' and cpu_choice == 'scissors':
        result = "you win!"
    elif usr_transl == 'paper' and cpu_choice == 'rock':
        result = "you win!"
    elif usr_transl == 'paper' and cpu_choice == 'scissors':
        result = "you lose!"
    elif usr_transl == 'scissors' and cpu_choice == 'rock':
        result = "you lose!"
    elif usr_transl == 'scissors' and cpu_choice == 'paper':
        result = "you win!"
    else:
        result = "huh? What are you doing?"

    print("CPU chose " + cpu_choice + ", " + result)

    play_input = input("Press enter to start the game, press 'q' and enter to quit ")
    if play_input == 'q':
        break
    else:
        continue
