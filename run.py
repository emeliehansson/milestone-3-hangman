import random
from words import word_list


def get_word():
    word = random.choice(word_list)
    return word.upper()


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


def display_hangman(tries):
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
    return stages[tries]


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

        elif choice == '2':
            start = True
            how_to_play()

        elif choice == '3':
            start = True

        else:
            print('Please select either 1, 2 or 3 to continue! ☆')


def game_levels():
    """
    Function to select what level(difficulty) the player wants for the game.
    Take it easy on me... 😴 (Press A)
    Give me a challenge! 😬 (Press B)
    I feel confident! 😎 (Press C)
    """
    print('\n')

    difficulty = False

    while not difficulty:
        option = input('\n').upper()
        if option == 'A':
            difficulty = True
            difficulty_lives = 12
            return difficulty_lives

        elif option == 'B':
            difficulty = True
            difficulty_lives = 7
            return difficulty_lives

        elif option == 'C':
            difficulty = True
            difficulty_lives = 4
            return difficulty_lives

        else:
            print('\n Please select a difficulty by pressing A, B or C.')


def run_game(word, difficulty_lives):
    """
    Runs the game and starts all the gameplay logic.
    """
    word_to_guess = '﹍' * len(word)
    game_over = False
    guesses = []
    lives = difficulty_lives
    print(f'\nRemaining Lives: {lives}\n')
    print('💭 What country are we looking for? '+' '.join(word_to_guess) + '\n')


def how_to_play():
    """
    Function to display the instructions of the game.
    Allows user to go back to main menu by pressing enter.
    """
    print('\n')
    print('Your task in this game is to guess the hidden word behind the\n'
          'blank spaces. In this Hangman game the theme is European\n'
          'countries. A correct guess will reveal a letter and a wrong.\n'
          'guess will take away a life. Good luck & have fun!')
    print('\n')
    input('Press enter to go back to the main menu.')
    print('\n')
    main()


def main():
    """
    Start the application and run the main function.
    """
    welcome_message()
    difficulty = play_options()
    if difficulty == 'default':
        difficulty_lives = 7
    else:
        difficulty_lives = game_levels()


main()
