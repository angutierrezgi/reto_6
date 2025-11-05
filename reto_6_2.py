print("----Palindrome Checker----")

def is_palindrome(word: str) -> bool:
    if isinstance(word, str):
        lower_word: str = word.lower()
        char_list_original = list(lower_word)
        char_list_reversed = char_list_original.copy()
        char_list_reversed.reverse()
    else:
        raise TypeError
    return char_list_original == char_list_reversed

if __name__ == "__main__":
    original_word: str = input("Enter a word: ")
    # We don't really need to check for a TypeError, because
    # the input only receives a str input if you don't
    # convert it first, but still we add it.
    try:
        if is_palindrome(original_word):
            print(f"'{original_word}' is a palindrome.")
        else:
            print(f"'{original_word}' is not a palindrome.")
    except TypeError as error:
        print(f"Error: {error.__class__}")