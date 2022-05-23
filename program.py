import random
import list_of_words

def accents(letter): # removes the accents when comparing the word to the user input

    if str(letter) in "áãàâ":
        return "a"
    elif str(letter) in "éêè":
        return "e"
    elif str(letter) in "í":
        return "i"
    elif str(letter) in "óõôòö":
        return "o"
    elif str(letter) in "úüùû":
        return "u"
    elif str(letter) in "ç":
        return "c"
    else:
        return str(letter)

word = random.choice(list_of_words.list)
word_no_accent = ""

for letter in word:
    word_no_accent = word_no_accent + accents(letter) # variable used to keep the original word intact to be shown at the end of the game

clean_color = "\033[0;0m"
red = "\033[0;91m"
green = "\033[0;92m"
yellow = "\033[0;33m"

decoration = "*" * 58

word_splitted = list(word_no_accent)

#print(word_splitted)
print(decoration)
print(" "*25 + "QUINTOU")
print("Tente adivinhar a palavra de 5 letras, você tem 6 chances: ")
print(decoration)

number_of_guesses = 6
guess = 1

while guess <= number_of_guesses:

    user_guess = input(f"Tentativa " + str(guess) + ": ")

    if not str.isalpha(user_guess) or len(user_guess) != 5:
        print("\033[A                             \033[A")
        print(f"{red}Palavra inválida, tente novamente!{clean_color}")
        continue

    if user_guess == word_no_accent:
        print(f"{green}Você venceu!\nA palavra é {word}.{clean_color}")
        break

    if guess == number_of_guesses:
        print(f"{red}Acabaram as chances! D:\nA palavra era {green}{word}{clean_color}")
        break

    user_guess_splitted = list(user_guess)
    guess_formatted = ""
    letter_position = 0

    for run_through_letters in range(len(word_splitted)): # adds the colors to the letters of the input word

        if accents(user_guess_splitted[letter_position]) not in accents(word_splitted):
            guess_formatted = guess_formatted + f"{red}{(user_guess_splitted[letter_position])}{clean_color}"

        elif accents(user_guess_splitted[letter_position]) == accents(word_splitted[letter_position]):
            guess_formatted = guess_formatted + f"{green}{(user_guess_splitted[letter_position])}{clean_color}"

        elif accents(user_guess[letter_position]) is not(accents(word_splitted[letter_position])):
            guess_formatted = guess_formatted + f"{yellow}{(user_guess_splitted[letter_position])}{clean_color}"
            
        letter_position = letter_position + 1
    guess += 1
    print(guess_formatted)