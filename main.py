import random
from enum import Enum


class YesOrNo(Enum):
    YES = 1
    NO = 2


def get_words_from_file():
    array = []

    with open('words.txt', 'r') as file:
        line = file.readline().strip()

        while line:
            array.append(line)
            line = file.readline().strip()
    return array


def random_word(array):
    rand = random.randint(0, len(array))
    return array[rand]


def parse_string(string):
    try:
        return str(string)
    except ValueError:
        return None


def validate_str_input():
    while True:
        str_input = input('Type letter: ').upper().strip()
        parsed_str = parse_string(str_input)

        if parsed_str.isalpha():
            if len(parsed_str) > 1:
                print('You must choose one letter')
            else:
                return parsed_str
        else:
            print('Invalid Input!')


def correct_guess(word, letter, guess_count):
    for i in range(0, len(word)):
        if letter in word[i]:
            guess_count += 1
    return guess_count


def print_board(word, array):
    for i in range(0, len(word)):
        if word[i] in list(array):
            print(word[i], end=' ')
        else:
            print('_', end=' ')
    print()


def wrong_guesses(word, letter):
    if letter not in list(word):
        return True
    else:
        return False


def continue_game():
    while True:
        str_input = input('Do you want to continue playing? Please type YES or NO: ').upper().strip()
        parsed_str = parse_string(str_input)

        if parsed_str.isalpha():
            if parsed_str == YesOrNo(1).name:
                start_game()
            elif parsed_str == YesOrNo(2).name:
                return print('Thanks for playing!')
            else:
                print('Please type YES or NO')
        else:
            print('Invalid Input!')


def start_game():
    words_array = get_words_from_file()
    word_string = random_word(words_array)
    my_array = []
    max_guesses_allowed = 6
    correct_guess_counter = 0

    print('Welcome to the Hangman Game!')
    print_board(word_string, my_array)

    while True:
        if correct_guess_counter == len(word_string):
            print('Congratulations! You have guessed the word')
            break

        if max_guesses_allowed == 0:
            print('You have reached the number of wrong guesses allowed!')
            print(f'Your word was {word_string}')
            break

        user_letter = validate_str_input()

        if user_letter in my_array:
            print('Letter already guessed!')
        else:
            my_array.append(user_letter)
            correct_guess_counter = correct_guess(word_string, user_letter, correct_guess_counter)

        print_board(word_string, my_array)
        is_wrong_guess = wrong_guesses(word_string, user_letter)

        if is_wrong_guess:
            max_guesses_allowed -= 1
            print(f'You have {max_guesses_allowed} chance(s) left!')
        print()


def main():
    start_game()
    continue_game()


if __name__ == '__main__':
    main()
