import random as rd

print("Welcome to hangman")
print("-------------------------------------------")

dictionary=["Biographer","cameraman","ignition","house","diamond","memes","subscribe","zebra","stretch","zythum","Purpose","line","jiggle"]

### Choose a random word
randomWord=rd.choice(dictionary)

for x in randomWord:
  print("_", end=" ")

def print_hangman(wrong):
    if(wrong==0):
        print("\n+--------+")
        print("        |")
        print("        |")
        print("        |")
        print("        |")
        print("      =====")
    elif(wrong==1):
        print("\n+--------+")
        print("    O   |")
        print("        |")
        print("        |")
        print("        |")
        print("      =====")
    elif(wrong==2):
        print("\n+--------+")
        print("    O   |")
        print("    |   |")
        print("        |")
        print("        |")
        print("      =====")
    elif(wrong==3):
        print("\n+--------+")
        print("    O   |")
        print("   /|   |")
        print("        |")
        print("        |")
        print("      =====")
    elif(wrong==4):
        print("\n+--------+")
        print("    O   |")
        print("   /|\  |")
        print("        |")
        print("        |")
        print("      =====")
    elif(wrong==5):
        print("\n+--------+")
        print("    O   |")
        print("   /|\  |")
        print("   /    |")
        print("        |")
        print("      =====")
    elif(wrong==6):
        print("\n+--------+")
        print("    O   |")
        print("   /|\  |")
        print("   / \  |")
        print("        |")
        print("      =====")

def printWord(guessedLetters):
    i=0
    rightLetters=0
    for char in randomWord:
        if(char in guessedLetters):
            print(randomWord[i],end=" ")
            rightLetters+=1
        else:
            print("_",end=" ")
        i+=1
    return rightLetters

def printLines():
    print("\r")
    for char in randomWord:
        print("\u203E",end=" ")

length_of_word_to_guess=len(randomWord)
amount_of_times_wrong=0
current_guess_index=0
current_letters_guessed=[]
current_letters_right=0

while(amount_of_times_wrong != 6 and current_letters_right != length_of_word_to_guess):
    print("\nLetters guessed so far: ")
    for letter in current_letters_guessed:
        print(letter,end=" ")
    
    letterGuessed=input("\nGuess a letter: ")                              # take the user input for print letters
    
    if(randomWord[current_guess_index] == letterGuessed):                    # if user is right
        print_hangman(amount_of_times_wrong)
        current_guess_index+=1                                             # print word
        current_letters_guessed.append(letterGuessed)
        current_letters_right=printWord(current_letters_guessed)
        printLines()

        
        print("\nHurray! YOu won the game")
    else:                                                                    # if user was wrong
        amount_of_times_wrong+=1
        current_letters_guessed.append(letterGuessed)
        print_hangman(amount_of_times_wrong)                                # update a diagram
        current_letters_right = printWord(current_letters_guessed)              # Print word
        printLines()


print("\nGame is over! Thank you for playing ")