import random
import Hangman_words
import Hangman_Art

stages = Hangman_Art.stages 
word_list = Hangman_words.word_list
chosen_word = random.choice(word_list)
word_length = len(chosen_word)
display = []
print(Hangman_Art.logo)
for _ in range(word_length):
    display.append("_")

end_of_game = False
lives = 6

while(not end_of_game):
    guess = input("Guess a letter of the word : ").lower()
    if guess in display:
      print(f"You have already guessed the letter {guess}")

    for position in range(word_length):
        letter = chosen_word[position]
        if(letter == guess):
            display[position]=letter

    if(guess not in chosen_word):
      print(f"You guessed the letter {guess}, which is not in the word. You lose a life.")
      lives -= 1

    if(lives == 0):
        end_of_game = True
        print("You Lost!")
        print("The word chosen was "+ chosen_word)

    if("_" not in display):
        end_of_game = True
        print("You won!")
    
    print(f"{' '.join(display)}")
    print(stages[lives])

