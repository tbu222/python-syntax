#1. For a list of words, print out each word on a separate line, but in all uppercase. How can you change a word to uppercase? Ask Python for help on what you can do with strings!
#2.Turn that into a function, print_upper_words. Test it out. (Don’t forget to add a docstring to your function!)
def print_upper_word(words):
    for word in words:
        print(word.upper())
    print('\n')
print_upper_word(["test1", "2test", "test3", "4test", "eclipse"])
#3.Change that function so that it only prints words that start with the letter ‘e’ (either upper or lowercase).
def print_upper_word1(words):
    for word in words:
        if word.startswith("e") or word.startswith("E"):
            print(word.upper())
    print('\n')

print_upper_word1(["test1", "2test", "test3", "4test", "eclipse"])
#4. Make your function more general: you should be able to pass in a set of letters, and it only prints words that start with one of those letters.
def print_upper_word2(words, letters):
    for word in words:
        for letter in letters:
            if word.startswith(letter):
                print(word.upper())
    print('\n')
print_upper_word2(["test1", "2test", "test3", "4test"], ["t", "4"])