# Write your solution in this file
import re


with open('dictionary.txt','r') as dictionary:
    with open('text.txt','r') as text:
        with open('output.txt','w') as output:
            d_words = [i.strip() for i in dictionary.readlines()]
            d_words= set(d_words)
            text_lines = [i.strip() for i in text.readlines()]
            text_words = [i.split() for i in text_lines]
            text_words_one_list = set()

            for i in text_words:
                for l in i:
                    text_words_one_list.add(re.sub(r'[^a-zA-Z]', '',l))

            for word in sorted(text_words_one_list):
                if word not in d_words:
                    output.write(f"{word}\n")