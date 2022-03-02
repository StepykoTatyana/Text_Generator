from nltk import WhitespaceTokenizer


def open_file(file_for_read):
    print()
    with open(file_for_read, "r", encoding="utf-8") as f:
        return WhitespaceTokenizer().tokenize(f.read())


def statistics(list_for_statistics):
    print("Corpus statistics")
    print('All tokens:', len(list_for_statistics))
    print('Unique tokens:', len(set(list_for_statistics)))
    print()


def read_word_with_index(list_for_read, index):
    while index != 'exit':
        try:
            print(list_for_read[int(index)])
        except ValueError:
            print('Type Error. Please input an integer.')
        except IndexError:
            print('Index Error. Please input an integer that is in the range of the corpus.')
        index = input()


def main():
    file = input()
    list_corpus = open_file(file)
    statistics(list_corpus)
    index_input = input()
    read_word_with_index(list_corpus, index_input)


if __name__ == '__main__':
    main()