from stats import get_num_words
from stats import get_car_count
from stats import format_car_count

def get_book_text(filePath):
    with open(filePath) as f:
        file_contents = f.read()
    return file_contents

def main():
    text = get_book_text("books/frankenstein.txt")
    num_word = get_num_words(text)
    car_count = get_car_count(text)
    formated_car_count = format_car_count(car_count)
    print("============ BOOKBOT ============")
    print("Analyzing book found at books/frankenstein.txt...")
    print("----------- Word Count ----------")
    print("Found {0} total words".format(num_word))
    print("--------- Character Count -------")
    print("============= END ===============")

if __name__ == "__main__":
    main()
