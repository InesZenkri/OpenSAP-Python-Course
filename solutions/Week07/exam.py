import random

def word_list():
    with open('5_letter_words.txt', 'r') as file:
        words = file.readlines()
        return [word.strip().lower() for word in words]

def random_word(words):
    return random.choice(words)

def is_real_word(guess, word_list):
    return guess in word_list

def check_guess(guess, target_word):
    result = ''
    guessed_chars = set()
    for i, char in enumerate(guess):
        if char == target_word[i]:
            result += 'X'
            guessed_chars.add(char)
        elif char in target_word and char not in guessed_chars:
            result += 'O'
            guessed_chars.add(char)
        else:
            result += '_'
    return result

def next_guess(words):
    while True:
        guess = input("Please enter a guess: ").lower()
        if is_real_word(guess, words):
            return guess
        else:
            print("That's not a real word!")

def play():
    words = word_list()
    target_word = random_word(words)
    for _ in range(6):
        guess = next_guess(words)
        result = check_guess(guess, target_word)
        print(result)
        if result == 'XXXXX':
            print("You won!")
            return
    print("You lost!")
    print(f"The word was: {target_word}")

play()
