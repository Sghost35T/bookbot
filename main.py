from stats import get_num_words,character_count,sorted_dict
import sys

def get_book_text(file_path):
    with open(file_path) as f:
        file_contents = f.read()
    return file_contents



def main():
    if len(sys.argv) < 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    book_path = sys.argv[1]
    file_content = get_book_text(book_path)
    words_count = get_num_words(file_content)
    char_count_dict = character_count(file_content)
    char_count_dict = sorted_dict(char_count_dict)
    print("============ BOOKBOT ============\n"+f"Analyzing book found at {book_path}...")
    print(f"Found {words_count} total words")
    print("--------- Character Count -------\n")
    for key,value in char_count_dict.items():
        if key.isalpha():
            print(key+": "+str(value)+"\n")
    print("============= END ===============")
    
    
    sys.exit(0)
    
    
main()
