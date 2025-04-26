import random

def hangman():
    words = ["Python", "programming ", "hangman","developer","computer","cybersecurity"]
    word = random.choice(words)
    
    #Initialize Game Variables
    
    guessed = ["_"] * len(word)
    guessed_letters =set()
    attempts =6
    
    print("Welcome to Hangman!")
    
    #Game Loop
    
    while attempts > 0 and "_" in guessed:
        print("\nWord: "+" ".join(guessed))
        print(f"Guessed Letters: {', '.join(sorted(guessed_letters))}")
        print(f"Attempts left: {attempts}")
        
        guess=input("Guess a letter: ").lower()
        
        #Input Validation
        
        if not guess.isalpha() or len(guess) !=1:
            print("Please enter a single alphabetic character.")
            continue
        
        if guess in guessed_letters:
            print("You have already guessed that letter.")
            continue
        
        guessed_letters.add(guess)
        
        #Check if Guess is Correct
        
        if guess in word:
            for i, letter in enumerate (word):
                if letter == guess:
                    guessed[i]=guess
            print("Correct!")
        
        #If Guess is Incorrect
        
        else:
            attempts -=1
            print("Incorrect!")
            
    if "_" not in guessed:
        print("\n Congratulations! You guessed the word: ", word)
    else:
        print("\n Game Over! The word was ", word)
        
if __name__ == "__main__":
    hangman()
        
    
            
        
        
    