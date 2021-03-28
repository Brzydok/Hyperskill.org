import random


print("H A N G M A N")
print('Type "play" to play the game, "exit" to quit:')
enter = input()
krotka = ("exit", "play")


while enter not in krotka:
    print('Type "play" to play the game, "exit" to quit:')
    enter = input()
    
    
word = random.choice(('python', 'java', 'kotlin', 'javascript'))
guessed_word = '-' * len(word)
guessed_letters = set()
lifes_counter = 8


while lifes_counter > 0:
    print(f"\n{guessed_word}")
    letter = input("Input a letter:")
    if letter in guessed_letters:
        print("You've already guessed this letter")
        continue
    elif len(letter) != 1:
        print("You should input a single letter")
        continue
    elif not letter.isalpha() or letter.isupper():
        print("Please enter a lowercase English letter")
        continue
    if letter in guessed_letters:
        lifes_counter -= 1
        print("No improvements")
    elif letter not in word:
        lifes_counter -= 1
        print("That letter doesn't appear in the word")
        if lifes_counter == 0:
            print("You lost!")
    else:
        guessed_letters.add(letter)
        guessed_word = ''.join([i if i in guessed_letters else '-' for i in word])

    if '-' not in guessed_word:
        print(f"You guessed the word {word}!\nYou survived!")
        break
    guessed_letters.add(letter)


