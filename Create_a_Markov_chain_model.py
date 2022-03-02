from nltk import WhitespaceTokenizer, bigrams
from collections import Counter


def open_file(file_for_read):
    with open(file_for_read, "r", encoding="utf-8") as f:
        return WhitespaceTokenizer().tokenize(f.read())


def statistics(list_for_statistics):
    list_bigrams = [list(a) for a in bigrams(list_for_statistics)]
    print("Number of bigrams:", len(list_bigrams))
    return list_bigrams


def read_word_with_index(head_user, list_find):
    while head_user != 'exit':
        print(f'Head: {head_user}')
        try:
            new_dict = {}
            for head, tail in list_find:
                new_dict.setdefault(head, []).append(tail)
            for head in new_dict:
                new_dict[head] = Counter(new_dict[head]).most_common()

            new_tail_len = [len(tail[0]) for tail in new_dict[head_user]]
            max_len_tail = max(new_tail_len)
            for tail_user in new_dict[head_user]:
                new_tail = [a for a in tail_user]
                print(f'Tail: {new_tail[0]} {" " * (max_len_tail - len(new_tail[0]))} Count: {new_tail[1]}')
            print()
        except KeyError:
            print('The requested word is not in the model. Please input another word.')
            print()
        head_user = input()


def main():
    file = input()
    list_corpus = open_file(file)
    list_bigrams = statistics(list_corpus)
    head_input = input()
    read_word_with_index(head_input, list_bigrams)


if __name__ == '__main__':
    main()
