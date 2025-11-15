def get_number_of_words(text):
    words= text.split()
    return len(words)


def sorter_helper(word):
    return word['num']

def sorter(words_dict):
    dict_list=[]

    for i, word in enumerate(words_dict.items()):
        dict_list.append({'char':word[0], 'num':word[1]})



    dict_list.sort(key=sorter_helper, reverse=True)

    for i,word in enumerate(dict_list):
        print(word['char']+ ':' , word['num'])


def count_words(text):
    characters={'a': 0, 'b':0, 'c':0, 'd':0, 'e':0, 'f':0, 'g':0, 'h':0, 'i':0, 'j':0, 'k':0, 'l':0, 'm':0, 'n':0, 'o':0, 'p':0, 'q':0, 'r':0, 's':0, 't':0, 'u':0, 'v':0, 'w':0, 'x':0, 'y':0, 'z':0}
   
    for char in text.lower():
        if char in characters:
            characters[char] += 1

    return characters