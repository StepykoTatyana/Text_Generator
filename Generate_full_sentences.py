import random
import re

from nltk import WhitespaceTokenizer, bigrams
from collections import Counter


def open_file(file_for_read):
    with open(file_for_read, "r", encoding="utf-8") as f:
        return WhitespaceTokenizer().tokenize(f.read())


def statistics(list_for_statistics):
    list_bigrams = [list(a) for a in bigrams(list_for_statistics)]
    return list_bigrams


def read_word_with_index(head_user, list_find):
    sentence = [head_user]
    while len(sentence) < 5:
        new_dict = {}
        for head, tail in list_find:
            new_dict.setdefault(head, []).append(tail)
        new_dict_new = Counter(new_dict[head_user]).most_common()
        next_word = new_dict_new[0][0]
        sentence.append(next_word)
        head_user = next_word
    while bool(re.match(r'\A.*[.!?]\Z', head_user)) is not True:
        new_dict = {}
        for head, tail in list_find:
            new_dict.setdefault(head, []).append(tail)
        new_dict_new = Counter(new_dict[head_user]).most_common()
        next_word = new_dict_new[0][0]
        sentence.append(next_word)
        head_user = next_word

    print(" ".join(sentence))


def main():
    file = input()
    list_corpus = open_file(file)
    list_bigrams = statistics(list_corpus)
    list_for_first_word = []
    for a in list_corpus:
        if bool(re.match(r'\A[A-Z].*[^.,?!:;]{3}\Z', a)) is True:
            list_for_first_word.append(a)
    i = 0
    while i < 10:
        first_word = random.choices(list_for_first_word)[0]
        read_word_with_index(first_word, list_bigrams)
        i += 1


if __name__ == '__main__':
    main()
