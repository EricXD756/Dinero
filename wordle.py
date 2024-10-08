# TASK A: Define a variable 'word' that holds the correct word for the wordle game
word = "freaky"
guessNum = 6
# TASK B: Define a function 'makeAGuess()' that passes in a users guess as a parameter
def makeAGuess(guess): 
  hint = ""
  won = True
  for i in range(len(word)):
    if guess[i] == word[i]:
      hint += "G"
    elif guess[i] in word:
      hint += "Y"
      won = False
    else:
      hint += "-"
      won = False
  if won:
    return("won")
  return(hint)




  # TASK C:Define a variable 'hint' that holds an empty string
 

  # TASK D: Build a loop that loops from 0 to the length of word
  

    # TASK E: Check if the current letter of guess matches the current letter of word. If so add the letter "G" to the hint
    
    
    # TASK F: If the previous condition is fales, check if the current letter of guess is in word at all. If so add the letter "Y" to the hint
    

    # TASK G: If the previous two conditions are false, add the symbol "-" to the hint
    
  # TASK H: Return hint
  


print("Let's play wordle! /n Guess the Wordle in 6 tries. Each guess must be a valid 5-letter word. For each guess, a hint will tell you how many letters you've guessed correctly. A G represents a letter in the word and in the correct spot.. A Y represents a letter in the word but in the wrong spot. A - represents a letter not in the word in any spot. \n Guess below! \n")

# TASK I: Build a loop that loops 6 times (representing the number of guesses a user has)
i = 0
while i < guessNum:
  guess = input("Guess a " + str(len(word)) + " letter word")
  hint = makeAGuess(guess)
  if hint == "won":
    print("You won!")
    break
  print(hint)
if won != True:
  print("You lost! The word was: " + word)

  # TASK J: Define a variable 'guess'. prompt the user for their 5-letter guess and store it in the variable

  # TASK K: Define a variable 'hint' and set the return of makeAGuess(guess) to that variable

  # TASK L: Print hint

  # TASK M: Check if hint = "GGGGG". If so the user has won. Print a win message and break the loop
  

# TASK N: After the loop has finished, meaning the user has run out of guesses, check if hint != "GGGGG". If so, the user has lost. Print a lose message. 
