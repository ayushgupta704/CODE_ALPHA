import random

from words import word_list

chosen_word = random.choice(word_list)

end_game = False
lives = 6

from hangman import logo
print(logo)



display = []
for _ in range(len(chosen_word)):
    display += "_"

while not end_game:
    guess = input("Guess a letter: ").lower()

    if guess in display:
        print(f"You've already guessed {guess}")

    for position in range(len(chosen_word)):
        letter = chosen_word[position]

        if letter == guess:
            display[position] = letter


    if guess not in chosen_word:

        print(f"You guessed {guess}, that's not in the word. You lose a life.")
        
        lives -= 1
        if lives == 0:
            end_of_game = True
            print("You lose.")

    print(f"{' '.join(display)}")

   
    if "_" not in display:
        end_of_game = True
        print("You win.")

    from hangman import hangmans
    print(hangmans[lives])
# for letter in chose_word:
#     if letter==guess:
#         print("Right")
#     else:
#         print("Wrong")
        