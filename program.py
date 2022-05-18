import random
import list_of_words

def accents(letter): # tentar usar isso depois pra ignorar acentuações na hora da comparação

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
    word_no_accent = word_no_accent + accents(letter)

clean_color = "\033[0;0m"
red = "\033[0;91m"
green = "\033[0;92m"
yellow = "\033[0;33m"

decoration = "*" * 58

word_splitted = list(word_no_accent)

#print(word_splitted)
print(decoration)
print(" "*25 + "QUINTOW")
print("Tente adivinhar a palavra de 5 letras, você tem 6 chances: ")
print(decoration)

number_of_guesses = 5
guess = 0

while guess <= number_of_guesses:

    user_guess = ""
    while not str.isalpha(user_guess) or len(user_guess) != 5:
        user_guess = input(f"Tentativa " + str(guess + 1) + ": ")

    if user_guess == word:
        print("Você venceu!")
        break

    if guess == number_of_guesses:
        print(f"Acabaram as chances! D:\nA palavra era {word}")
        break

    user_guess_splitted = list(user_guess)
    guess_formatted = ""
    letter_position = 0

    for run_through_letters in range(len(word_splitted)): # it's always 5 letters

        if accents(user_guess_splitted[letter_position]) not in accents(word_splitted):
            guess_formatted = guess_formatted + f"{red}{(user_guess_splitted[letter_position])}{clean_color}"

        elif accents(user_guess_splitted[letter_position]) == accents(word_splitted[letter_position]):
            guess_formatted = guess_formatted + f"{green}{(user_guess_splitted[letter_position])}{clean_color}"

        elif accents(user_guess[letter_position]) is not(accents(word_splitted[letter_position])):
            guess_formatted = guess_formatted + f"{yellow}{(user_guess_splitted[letter_position])}{clean_color}"
            
        letter_position = letter_position + 1
    guess = guess + 1
    print(guess_formatted)