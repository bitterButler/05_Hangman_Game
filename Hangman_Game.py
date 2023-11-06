#the first 4 words in WORDS are hungarian, after that english all. 
WORDS = ("alma", "ember", "telefon", "csicska", "brother", "family", "car", "university", 
         "team", "user", "company", "engineer", "keyboard", "sneakers", "race", 
         "python", "jumble", "easy", "difficult", "answer",  "xylophone")
import random
chosenWORD = random.choice(WORDS)

#testing code:
print(f'test hint. solution is {chosenWORD}.')

#1 empty list, this will be printed/displayed whenever we have matching/correct guessing.
display = []
for under_score in chosenWORD: # we do this, so we get the same length/amount of spaces as the chosenWORD.
  display += "_"
print(display)

user_guess = input("Guess a letter: ").lower()
  
for position in range(len(chosenWORD)):
  letter = chosenWORD[position]
  if letter == user_guess:
    display[position] = letter
  print(display)
print("")
