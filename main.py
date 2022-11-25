import random
import hangman_art
import hangman_words

chosen_word = random.choice(hangman_words.word_list)
display = []
guess = ""

print(hangman_art.logo)

#For testing purposes but should be removed for user
print(f'The work is {chosen_word}.')

#initially set up guess array
for letter in chosen_word:
  display.append('_')

#runs input asking for guess
def get_user_guess():
  return input("Guess a letter: ").lower()

#determines if guess is true, updates display, lives if needed
def handle_guess(user_guess):
  correct_guess = False

  if user_guess in display:
    return "duplicate"
  
  for idx, letter in enumerate(chosen_word):
    if letter == user_guess:
      display[idx] = letter
      correct_guess = True    
  return correct_guess

def display_result(guess_is_true, lives_left):
  if guess_is_true and '_' in display:
      print("Correct!")
      print(display)
  elif guess_is_true and '_' not in display:
      print("You win!!!")
  elif not guess_is_true and lives_left > 0:
    print("Incorrect correct, you lose a life.")
    print(hangman_art.stages[lives_left])
  else:
    print(hangman_art.stages[lives_left])
    print("Sorry, you are dead!")
    
  
def run():
  lives = 6
  
  while '_' in display and lives > 0:
    guess = get_user_guess()
    is_correct_guess = handle_guess(guess)

    if not is_correct_guess:
      lives -= 1

    if is_correct_guess == 'duplicate':
      print("You have already guessed this. Pick another letter")
    else:
      display_result(is_correct_guess, lives)

#initial start
print(display)
run()


