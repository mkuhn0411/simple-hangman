import random
import hangman_art
import hangman_words

chosen_word = random.choice(hangman_words.word_list)
display = []
guess = ""
lives = 6
print(hangman_art.logo)

#For testing purposes but should be removed for user
print(f'Pssst, the solution is {chosen_word}.')

#initially set up guess array
for letter in chosen_word:
  display.append('_')

#runs input asking for guess
def get_user_guess():
  return input("Guess a letter: ").lower()

#run after user makes a guess
def handle_guess(user_guess):
  global lives
  correct_guess = False
  
  for idx, letter in enumerate(chosen_word):
    if letter == user_guess:
      display[idx] = letter
      correct_guess = True
  #if guess is not correct add to count
  if not correct_guess:
    lives -= 1
    
  return correct_guess

def display_result(guess_is_true):
  if guess_is_true and '_' in display:
      print("Correct!")
      print(display)
  elif guess_is_true and '_' not in display:
      print("You win!!!")
  elif not guess_is_true and lives > 0:
    print("Incorrect")
    print(hangman_art.stages[lives])
  else:
    print(hangman_art.stages[lives])
    print("You are dead!")
    
  
def run():
  while '_' in display and lives > 0:
    guess = get_user_guess()
    is_correct_guess = handle_guess(guess)
    display_result(is_correct_guess)

#initial start
print(display)
run()


