import os
import random

def read():
    my_words  = []
    with open('./data.txt', 'r', encoding='utf-8') as f:
        for data in f:
            my_words.append(data.strip().upper())
    return my_words        


def run():
    chosen_words = random.choice(read())
    chosen_words_list = [letter for letter in chosen_words]
    chosen_words_list_underscore = ['_'] * len(chosen_words_list)
    letter_index_dic = {}

    for idx, letter in enumerate(chosen_words):
        if not letter_index_dic.get(letter):
            letter_index_dic[letter] = []
        letter_index_dic[letter].append(idx)    

    while True:
        os.system('clear')
        print('Adivina la palabra 😜')

        for element in chosen_words_list_underscore:
            print(element + " ", end="")
        print('\n')    

        letter = input('Elige una letra =>  ').strip().upper()
        assert letter.isalpha(), 'Escribe una letra'

        if letter  in chosen_words_list:
            for idx in letter_index_dic[letter]:
                chosen_words_list_underscore[idx] = letter

        if "_"  not in chosen_words_list_underscore:
            os.system('clear')
            print(' GAnaste 🥳  la palabra es ' , chosen_words, ' 🤯')
            break        

if __name__ == '__main__':
    run()