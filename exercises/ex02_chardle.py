"""in this exercise i will prompt the user to guess my five letter word"""

__author__ = "730745996"


def input_word() -> str:
    """takes no parameter as the function has user input that runs when the function is
    called"""
    guess: str = str(input("Enter a 5-character word: "))
    if len(guess) != 5:
        print("Error: Word must contain 5 characters.")
        exit()
        # Initially I had included an else block here but ultimately realized I did not
        # need it as not all ifs need elses and the length of a word can either be 5
        # letters or no and there isn't another case otherwise.
    return guess
    # this function takes a string input as the variable guess and checks to see if
    # the length of it is only 5 characters. If it is not, the program exits and does
    # not continue with the rest of the program.


def input_letter() -> str:
    """takes no parameter as the function has user input that runs when the function is
    called"""
    let_guess: str = str(input("Enter a single character: "))
    if len(let_guess) != 1:
        print("Error: Character must be a single character.")
        exit()
        # Similarly to the input_word function, I removed the else here as well.
        # Another issue I was having was I forgot the : after each if and it was giving
        # me an error but I soon realized I needed it as it is a part of python code.
    return let_guess
    # this function takes a string input as the variable let_guess and checks to see if
    # the length of it is only 1 character. If it is not, the program exits and does
    # not continue with the rest of the program.


def contains_char(word: str, letter: str) -> None:
    """takes 2 parameters which are both strings, in main these parameters are set
    equal to two arguments which are the two functions we defined earlier. This makes
    it so those two functions can run and the users will get prompted to enter their
    own word and character instead of having a set word and character run each time.
    """
    set: int = 0
    count: int = 0
    # This function took me sometime to figure out. I have having issues on where to
    # indent the set and count increments (set = set + 1 and count = count + 1). I had
    # to test through it a couple times using trailhead to figure out where to place
    # them.
    print("Searching for " + letter + " in " + word)
    while set <= len(word) - 1:
        if letter == word[set]:
            print(letter + " found at index " + str(set))
            count = count + 1
        set = set + 1
    if count == 0:
        print("No instances of " + letter + " found in " + word)
    elif count == 1:
        print(str(count) + " instance of " + letter + " found in " + word)
    else:
        print(str(count) + " instances of " + letter + " found in " + word)
    # this function is one of the main functions. it checks each index of the user
    # inputted word and sees with the user inputted letter is a letter the word. if it
    # is the returns the indices in which it appears.


def main() -> None:
    contains_char(word=input_word(), letter=input_letter())
    # this main function is here to make it easier when calling the program. all that
    # needs to be done is calling main() which then calls the rest of the functions
    # needed to run the program


if __name__ == "__main__":
    main()
