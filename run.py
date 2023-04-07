"""
Importing necessary files for the game
"""
import random
from countries import countries_list
from cars import cars_list
from animals import animal_list
from female_artists import artist_list


def get_word():
    """
    The player will be asked to choose a category by choosing one
    of the four numbers with the category name.
    """
    category = input('\nPlease choose a category by pressing any of the\n'
                     'following numbers: \n 1. Countries \n 2. Animals'
                     '\n 3. Car Brands\n 4. Female Artists\n')
    category = category.lower()

    if category == "1":
        word = random.choice(countries_list)
    elif category == "2":
        word = random.choice(animal_list)
    elif category == "3":
        word = random.choice(cars_list)
    elif category == "4":
        word = random.choice(artist_list)
    else:
        print("Invalid category. Defaulting to countries.")
        word = random.choice(countries_list)

    return word.upper()


def display_hangman(lives):
    """
    Hangman images that changes if/when the player guesses the wrong letter.
    If the player guesses a correct letter, the image stays the same.
    The code for the imagery below of Hangman is borrowed from
    another student: nicolemne.
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
    Welcomes the user to the game and then asks for a username.
    Then it asks the user to choose 1, 2 or 3.
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
    Take it easy on me... 😴 (Press E (easy))
    I'm up for a challenge! 😬 (Press M (medium))
    'I feel confident! 😎 (Press H (hard))
    """
    print("\n")
    print("Please select a difficulty\n")
    print('Take it easy on me... 😴 10 guesses (Press E)')
    print("I'm up for a challenge! 😬 6 guesses (Press M)")
    print('I feel confident! 😎 4 guesses (Press H)')

    difficulty = False

    while not difficulty:
        option = input('\n').upper()
        if option == 'E':
            difficulty = True
            difficulty_lives = 10
            return difficulty_lives

        if option == 'M':
            difficulty = True
            difficulty_lives = 6
            return difficulty_lives

        if option == 'H':
            difficulty = True
            difficulty_lives = 4
            return difficulty_lives

    print('\n Please select a difficulty by pressing E, M or H.')


def run_game(word, difficulty_lives):
    """
    Runs the game and starts all the gameplay logic.
    """
    word_to_guess = '_' * len(word)
    game_over = False
    guesses = []
    lives = difficulty_lives
    print(f'\n Remaining Lives: {lives}\n')

    print(f'\n💭  What word are we looking for? {word_to_guess} \n')

    while not game_over and lives > 0:
        input_guess = input('Please guess a letter: \n').upper()
        try:
            if len(input_guess) > 1:
                raise ValueError(
                    f'\nYou can only guess one letter at a time.'
                    f'\nYou guessed: {len(input_guess)}\n'
                )

            if not input_guess.isalpha():
                raise ValueError(
                    f'\nYou can only guess by letters.'
                    f'\nYou guessed: {input_guess}\n'
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
                if '_' not in word_to_guess:
                    game_over = True
        except ValueError as input_error:
            print(f'{input_error}\nPlease try again.\n')
            continue

        print(display_hangman(lives))

        if lives > 0:
            print(f'\nRemaining tries: {lives}')
            print(f'\n💭  What word are we looking for? {word_to_guess} \n')
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
          'countries, animals, car brands or female artists.\n'
          'A correct guess will reveal a letter and a wrong\n'
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
        difficulty_lives = 6
    else:
        difficulty_lives = game_levels()
    hangman_word = get_word()
    run_game(hangman_word, difficulty_lives)


main()
