from stats import get_num_words
from stats import get_car_count
from stats import format_car_count
import sys

def get_book_text(filePath):
    with open(filePath) as f:
        file_contents = f.read()
    return file_contents

def main():
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    text = get_book_text(sys.argv[1])
    num_word = get_num_words(text)
    car_count = get_car_count(text)
    formated_car_count = format_car_count(car_count)
    print("============ BOOKBOT ============")
    print("Analyzing book found at books/frankenstein.txt...")
    print("----------- Word Count ----------")
    print("Found {0} total words".format(num_word))
    print("--------- Character Count -------")
    for dict in formated_car_count:
        if dict["caracter"].isalpha():
            print("{0}: {1}".format(dict["caracter"], dict["num"]))
    print("============= END ===============")

if __name__ == "__main__":
    main()
