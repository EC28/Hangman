import random

hang=[
'''
   _____
  /     |
 /      
 |
 |
 |
 |
 |
----------
'''
,
'''
   _____
  /     |
 /      O
 |
 |
 |
 |
 |
----------
'''
,
'''
   _____
  /     |
 /      O
 |      |
 | 
 |   
 |   
 |      
----------
'''
,
'''
   _____
  /     |
 /      O
 |     /|
 |   
 |   
 |   
 |    
----------
'''
,
'''
   _____
  /     |
 /      O
 |     /|
 |    /
 |   
 |   
 |   
----------
'''
,
'''
   _____
  /     |
 /      O
 |     /|\\
 |    /   
 |   
 |   
 |    
----------
'''
,
'''
   _____
  /     |
 /      O
 |     /|\\
 |    /   \\
 |   
 |   
 |    
----------
'''
,
'''
   _____
  /     |
 /      O
 |     /|\\
 |    / | \\
 |     
 | 
 | 
----------
'''
,
'''
   _____
  /     |
 /      O
 |     /|\\
 |    / | \\
 |     / 
 |
 |
----------
'''
,
'''
   _____
  /     |
 /      O
 |     /|\\
 |    / | \\
 |     / \\
 |
 |
----------
'''
,
'''
   _____
  /     |
 /      O
 |     /|\\
 |    / | \\
 |     / \\
 |    /
 |
----------
'''
,
'''
   _____
  /     |
 /      O
 |     /|\\
 |    / | \\
 |     / \\
 |    /   \\
 |
----------
'''
]   #the above array contains the hangman drawings with increasing numbers of body parts, equivalent to the number of lives of the user

wordlist=["apple","apricot","banana","blackberry","blueberry","cherry","cranberry","grape","grapefruit","kiwi","lemon","lime","melon","orange","peach","","pear","pineapple","plum","pomegranate","prune","raspberry","strawberry","tangerine","watermelon"]      #an array of the list of words that can be used
word=random.choice(wordlist)      #randomly chooses a word from the 'wordlist'
word=word.upper()
lettersleft=["-"]*len(word)       #prints dashes to represent ever letter of the word
guessed=[]              #an empty array that will be used to place the user's inputs/guesses
index=0                 #the 'index' will be used to define the hangman drawing array as numbers

print(' __   __  _______  __    _  _______  __   __  _______  __    _ ')    #title of the game
print('|  | |  ||   _   ||  |  | ||       ||  |_|  ||   _   ||  |  | |')
print('|  |_|  ||  |_|  ||   |_| ||    ___||       ||  |_|  ||   |_| |')
print('|       ||       ||       ||   | __ |       ||       ||       |')
print('|       ||       ||  _    ||   ||  ||       ||       ||  _    |')
print('|   _   ||   _   || | |   ||   |_| || ||_|| ||   _   || | |   |')
print('|__| |__||__| |__||_|  |__||_______||_|   |_||__| |__||_|  |__|')

print()

print(hang[index])      #prints the hangman drawings depending on the 'index' where it starts at 0, resulting in the print of the first drawing
print('Word: ',lettersleft)     #prints the word and each - for each letters
print('Letters guessed: ',guessed)      #prints the letters or words the user has already guessed
    
guess=input('Guess a letter or word: ')
guess=guess.upper()     #converts the user's input into uppercase to match the case of the words in the 'wordlist'
guessed.append(guess)   #places the letters the user has guessed into the 'guessed' array

for i in range(len(word)):  #this for loop takes the user's guess and places it into the corresponding position in the 'lettersleft' array
    if word[i]==guess:
        lettersleft[i]=guess

while "-" in lettersleft:      #repeats/loops the code to allow the user to guess again until they lose the game


    if guess==word:     #checks if the user has guessed the complete word and ends the game if they did
            print()
            print("  ___                        _        _      _   _             _ ")
            print(" / __|___ _ _  __ _ _ _ __ _| |_ _  _| |__ _| |_(_)___ _ _  __| |")
            print("| (__/ _ \ ' \/ _` | '_/ _` |  _| || | / _` |  _| / _ \ ' \(_-<_|")
            print(" \___\___/_||_\__, |_| \__,_|\__|\_,_|_\__,_|\__|_\___/_||_/__(_)")
            print("              |___/                                              ")
            print("You have correctly guessed the word.");
            exit()
    
    if guess in word:   #an if statement that checks if the user's guess is within the word
        print("_________________________________________________________________________")
        print("  ___                    _   _ ")
        print(" / __|___ _ _ _ _ ___ __| |_| |")
        print("| (__/ _ \ '_| '_/ -_) _|  _|_|")
        print(" \___\___/_| |_| \___\__|\__(_)")
        print("Guess another letter or word.")
                                
        print(hang[index])
        print('Word: ',lettersleft)
        print('Letters guessed: ',guessed)
        guess=input('Guess a letter or word: ')
        guess=guess.upper()
        guessed.append(guess)
        

        for i in range(len(word)):  #this for loop checks if the user's imput exists within the word and replaces it with the dashes in the corresponding positions
            if word[i]==guess:
                lettersleft[i]=guess


    elif index==10:     #this if statement checks if the hangman drawing is completed and ends the game if it is
        index=index+1   #adds the final body part of the hangman
        print(hang[index])
        print("  ___                   ___              ")
        print(" / __|__ _ _ __  ___   / _ \__ _____ _ _ ")
        print("| (_ / _` | '  \/ -_) | (_) \ V / -_) '_|")
        print(" \___\__,_|_|_|_\___|  \___/ \_/\___|_|  ")               
        print("You have ran out of guesses.")
        exit()          #ends the program since the user has ran out of guesses



    else:               #an else statement that starts if the user's guess is not within the word
        print("_________________________________________________________________________")
        print(" ___                            _   _ ")
        print("|_ _|_ _  __ ___ _ _ _ _ ___ __| |_| |")
        print(" | || ' \/ _/ _ \ '_| '_/ -_) _|  _|_|")
        print("|___|_||_\__\___/_| |_| \___\__|\__(_)")
        print("Try again.")

        index=index+1       #adds 1 to the 'index' to print the next hangman drawing in the array (adds the body parts)
        print(hang[index])
        
        print('Word: ',lettersleft)
        print('Letters guessed: ',guessed)
        guess=input('Guess a letter or word: ')
        guess=guess.upper()
        guessed.append(guess)


else:
    print()
    print("  ___                        _        _      _   _             _ ")
    print(" / __|___ _ _  __ _ _ _ __ _| |_ _  _| |__ _| |_(_)___ _ _  __| |")
    print("| (__/ _ \ ' \/ _` | '_/ _` |  _| || | / _` |  _| / _ \ ' \(_-<_|")
    print(" \___\___/_||_\__, |_| \__,_|\__|\_,_|_\__,_|\__|_\___/_||_/__(_)")
    print("              |___/                                              ")
    print("You have correctly guessed the word.");
    exit()


