import random
from words import word_list


def get_word():
    word = random.choice(word_list)
    return word.upper()


def display_hangman(lives):
    """
    Hangman images that changes if/when the player guesses the wrong letter.
    If the player guesses a correct letter, the image stays the same.
    """

    stages = [  # final state: head, torso, both arms, and both legs
        """
        ___________
        |/        |
        |         O
        |        /|\\
        |         |
        |        / \\
        |\\
        ========
        """,
        """
        ___________
        |/        |
        |         O
        |        /|\\
        |         |
        |        /
        |\\
        ========
        """,
        """
        __________
        |/        |
        |         O
        |        /|\\
        |         |
        |
        |\\
        ========
        """,
        """
        __________
        |/        |
        |         O
        |        /|
        |         |
        |
        |\\
        ========
        """,
        """
        __________
        |/        |
        |         O
        |         |
        |         |
        |
        |\\
        ========
        """,
        """
        __________
        |/        |
        |         O
        |
        |
        |
        |\\
        ========
        """,
        """
        __________
        |/
        |
        |
        |
        |
        |\\
        ========
        """,
        """
        __________
        |/
        |
        |
        |
        |
        |
        ========
        """,
        """
        |/
        |
        |
        |
        |
        |
        ========
        """,

        """
        |
        |
        |
        |
        |
        ========
        """,
        """
        """
    ]
    return stages[lives]


def welcome_message():

    """
    Welcomes the user to the game and then asks for their name/username.
    To start the game, press any key.
    """
    print('▄▀█ █▀█ █▀▀   █▄█ █▀█ █░█   █▀█ █▀▀ ▄▀█ █▀▄ █▄█')
    print('█▀█ █▀▄ ██▄   ░█░ █▄█ █▄█   █▀▄ ██▄ █▀█ █▄▀ ░█░')
    print('\n')
    print(' ▀█▀ █▀█   █▀█ █░░ ▄▀█ █▄█   █░█ ▄▀█ █▄░█ █▀▀ █▀▄▀█ ▄▀█ █▄░█ ▀█ █')
    print(' ░█░ █▄█   █▀▀ █▄▄ █▀█ ░█░   █▀█ █▀█ █░▀█ █▄█ █░▀░█ █▀█ █░▀█ ░▄ ▄')
    print('\n')

    print('Press 1 to start new game')
    print('Press 2 for the instructions')
    print('Press 3 to choose difficulty')


def play_options():
    """
    Startup view, shows the "are you ready to play hangman?!" text and
    also gives the player the different options to choose from.
    User choice is displayed in the welcome message function.
    """

    start = False

    while not start:
        choice = input('\n')
        if choice == '1':
            start = True
            difficulty = 'default'
            return difficulty
        if choice == '2':
            start = True
            how_to_play()
        elif choice == '3':
            start = True
        else:
            print('Please select either 1, 2 or 3 to continue! ☆')


def game_levels():
    """
    Function to select what level(difficulty) the player wants for the game.
    Take it easy on me... 😴 (Press E)
    I'm up for a challenge! 😬 (Press H)
    """
    print("\n")
    print("Please select a difficulty\n")
    print('Take it easy on me... 😴 (Press E)')
    print("I'm up for a challenge! 😬 (Press H)")

    difficulty = False

    while not difficulty:
        option = input('\n').upper()
        if option == 'E':
            difficulty = True
            difficulty_lives = 8
            return difficulty_lives

        if option == 'H':
            difficulty = True
            difficulty_lives = 5
            return difficulty_lives

    print('\n Please select a difficulty by pressing E or H.')


def run_game(word, difficulty_lives):
    """
    Runs the game and starts all the gameplay logic.
    """
    word_to_guess = '_ ' * len(word)
    game_over = False
    guesses = []
    lives = difficulty_lives
    print(f'\nRemaining Lives: {lives}\n')
    print(f'\n💭  What country are we looking for? {word_to_guess} \n')

    while not game_over and lives > 0:
        input_guess = input('Please guess a letter: \n').upper()
        try:
            if len(input_guess) > 1:
                raise ValueError(
                    f'\nYou can only guess one letter at a time.'
                    f'You guessed: {len(input_guess)}'
                )

            if not input_guess.isalpha():
                raise ValueError(
                    f'\nYou can only guess by letters.'
                    f'You guessed: {input_guess}'
                )

            if len(input_guess) == 1 and input_guess.isalpha():
                if input_guess in guesses:
                    raise ValueError(
                        f'\n{input_guess} has already been used.'
                    )

            if input_guess not in word:
                print(f'Sorry.. {input_guess} is not a part of the word.')
                print('Better luck next time, unfortunately you lost a life..')
                guesses.append(input_guess)
                lives -= 1

            else:
                print(f'\nYay! {input_guess} is a part of the word, nice job!')
                guesses.append(input_guess)
                guessed_words = list(word_to_guess)
                indices = [i for i, letter in enumerate(word)
                           if letter == input_guess]
                for index in indices:
                    guessed_words[index] = input_guess
                    word_to_guess = ''.join(guessed_words)
                if '_ ' not in word_to_guess:
                    game_over = True
        except ValueError as input_error:
            print(f'{input_error}\n Please try again.\n')
            continue

        print(display_hangman(lives))

        if lives > 0:
            print(f'\nRemaining tries: {lives}')
            print(f'\n💭  What country are we looking for? {word_to_guess} \n')
            print('Your guesses: '+', '.join(guesses) + '\n')

    if game_over:
        print(f'NICE! You guessed the word: {word}')
    else:
        print('Oh no... 😵 You have no more lives left.')
        print('Game over.\n')
        print(f'The word we were looking for was: {word}')

    restart_game(difficulty_lives)


def restart_game(difficulty_lives):
    """
    When the game is over, the player is offered the choice to start a new
    game right away or they can choose to return to the main menu.
    """
    reset_game = False
    while not reset_game:
        restart = input('Would you like to try again? Y/N 🤖 \n').upper()
        try:
            if restart == 'Y':
                reset_game = True
                hangman_word = get_word()
                run_game(hangman_word, difficulty_lives)

            elif restart == 'N':
                reset_game = True
                print('\n')
                main()

            else:
                raise ValueError(
                    f'You have to enter either Y or N. You entered {restart}'
                )

        except ValueError as input_error:
            print(f'\n{input_error} is not valid. Try again.\n')


def how_to_play():
    """
    Function to display the instructions of the game.
    Allows user to go back to main menu by pressing enter.
    """
    print('\n')
    print('Your task in this game is to guess the hidden word behind the\n'
          'blank spaces. In this Hangman game the theme is European\n'
          'countries. A correct guess will reveal a letter and a wrong\n'
          'guess will take away a life. Good luck & have fun!')
    print('\n')
    input('Press enter to go back to the main menu.\n')
    print('\n')
    main()


def main():
    """
    Start the application and run the main function.
    """
    welcome_message()
    difficulty = play_options()
    if difficulty == 'default':
        difficulty_lives = 8
    else:
        difficulty_lives = game_levels()
    hangman_word = get_word()
    run_game(hangman_word, difficulty_lives)


main()
