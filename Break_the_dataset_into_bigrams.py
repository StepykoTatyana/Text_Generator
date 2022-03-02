from nltk import WhitespaceTokenizer, bigrams


def open_file(file_for_read):
    with open(file_for_read, "r", encoding="utf-8") as f:
        return WhitespaceTokenizer().tokenize(f.read())


def statistics(list_for_statistics):
    list_bigrams = [list(a) for a in bigrams(list_for_statistics)]
    print("Number of bigrams:", len(list_bigrams))
    print()
    return list_bigrams


def read_word_with_index(index, list_find):
    while index != 'exit':
        try:
            find_bigrams(list_find, int(index))
        except ValueError:
            print('Type Error. Please input an integer.')
        except IndexError:
            print('Index Error. Please input an integer that is in the range of the corpus.')
        index = input()


def find_bigrams(list_find, index_for_find):
    head = list_find[index_for_find][0]
    tail = list_find[index_for_find][1]
    print(f'Head: {head} Tail: {tail}')


def main():
    file = input()
    list_corpus = open_file(file)
    list_bigrams = statistics(list_corpus)
    index_input = input()
    read_word_with_index(index_input, list_bigrams)


if __name__ == '__main__':
    main()
