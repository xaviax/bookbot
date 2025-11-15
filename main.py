from stats import get_number_of_words, count_words, sorter
import sys
def get_book_text(file_path):
    content= ""
    with open(file_path) as f: 
        content= f.read()
    return content


def main():

    sys_args_list = sys.argv
    print(sys_args_list)
    if len(sys_args_list)>1:
        book_text= get_book_text(sys_args_list[1])
        #print(book_text)
        word_count= get_number_of_words(book_text)
        print(f"Found {word_count} total words")

        words_dict=count_words(book_text)


        sorter(words_dict)

    else:
        print('Usage: python3 main.py <path_to_book>')
        sys.exit(1)

   
   


main()