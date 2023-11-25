#!usr/bin/env/ python3
# Created By: Marli Peters
# Date: Nov, 11, 2023
# This program asks the user to enter a word, then how
# many copies of the word to print out, and then asks
# how many letters of the word to print in each copy.
# Finally it will print given number of characters of the
# word the given number of times.


# create main function
def main():
    # set counter
    counter = 0

    # start while loop to return to if there is an error
    while True:
        # get user input for word repeat
        user_word = str(input("Enter your word: "))
        copies_str = str(input("Enter number of copies: "))
        subword_str = str(input("Enter subword size: "))
        print("")

        # catch integer input errors
        try:
            copies_int = int(copies_str)
            subword_int = int(subword_str)
        except Exception:
            print("Please enter a valid integer for copies and subword number.")
            print("")
        else:
            # catch positive integer errors
            if copies_int <= 0 or subword_int <= 0:
                print("Please enter a positive integer for copies and subword number.")
                print("")
            else:
                # set count to copies
                count = copies_int
                # set word to be split
                split_word = user_word[:subword_int]
                # display word repeated
                for counter in range(count):
                    print(split_word, end="")
                break
        # return errors to beginning of while loop
        try:
            copies_int = int(copies_str)
            subword_int = int(subword_str)
            if copies_int < 0 or subword_int < 0:
                pass
            else:
                break
        except Exception:
            pass

    print("")


# call main function
if __name__ == "__main__":
    main()
