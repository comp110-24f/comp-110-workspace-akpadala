"""Wordle - A game which gives 6 tries to guess our magical 5 letter word."""

__author__ = "730745996"


def input_guess(length_word: int) -> str:
    """This function allows the user to input a word. Then it checks to see if the
    length of the word inputted is the same as the length of the guess word. In this
    case the word it will cross check with is codes which is a 5 letter word."""
    guess: str = input(f"Enter a {length_word} character word: ")
    while length_word != len(guess):
        guess = input(f"That wasn't {length_word} chars! Try again: ")
        # I used an f string here to combine different types. It is a shortcut
        # instead of casting other types to strings.
    return guess


def contains_char(secret_word: str, char_guess: str) -> bool:
    """This function checks each character at index of the secret word and compares it
    with each character at each index for the guess word."""
    assert len(char_guess) == 1
    index: int = 0
    # we need to set index = 0 as the while loop will run until the end of the word.
    # This will only happen if index goes up till less than the length of the word.
    while index < len(secret_word):
        if secret_word[index] == char_guess:
            return True
        index += 1
        # this needs to be included to make sure it is not an infinite loop
    return False


def emojified(guess: str, secret: str) -> str:
    """This function is what alerts the user which characters match up between the
    secret word and guess word. If a green box is shown, it means the guess character
    is in the same index as the secret word character. The yellow box box shows that
    the character is correct but not in the right index. The white box indicates that
    the letter nor the position are right."""
    assert len(guess) == len(secret)
    WHITE_BOX: str = "\U00002B1C"
    GREEN_BOX: str = "\U0001F7E9"
    YELLOW_BOX: str = "\U0001F7E8"
    index: int = 0
    index_color: str = ""
    # index_color will be used to insert the emoji colors so intially you had to set it
    # to an empty string as it needs to exist before adding emoji colors to it
    while index < len(secret):
        if guess[index] == secret[index]:
            index_color = index_color + GREEN_BOX
        elif contains_char(secret_word=secret, char_guess=guess[index]):
            index_color = index_color + YELLOW_BOX
        else:
            index_color = index_color + WHITE_BOX
        index = index + 1
        # initially i had the index = index + 1 in each individual if else statement
        # but I realized that including it at the bottom but still in the while loop
        # will do the same function
    return index_color


def main(secret: str) -> None:
    """The entrypoint of the program and main game loop."""
    turn: int = 1
    # initially i had turn set equal to 0 and did while turn < 6 but then i realized i
    # would need to call turn while printing it to notify the user how many turns were
    # left and therefore had to change it to turn <= 6 as there can be 6 turns.
    while turn <= 6:
        print(f"=== Turn {turn}/6 ===")
        guess_1: str = input_guess(length_word=len(secret))
        emoji: str = emojified(guess=guess_1, secret=secret)
        if guess_1 == secret:
            print(emoji)
            print(f"You won in {turn}/6 turns!")
            # indicates what is outputted to the user if the word guessed is correct
        else:
            print(emoji)
            turn = turn + 1
            # continues with the program if the guess was not the correct guess as the
            # user has 6 tries
        if turn > 6:
            print("X/6 - Sorry, try again tomorrow!")
            # if the user exhausted their turns this message is outputted.


if __name__ == "__main__":
    main(secret="codes")
