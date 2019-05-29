MAX_COUNT = 25


class Node:
    """ Node element of a trie."""
    def __init__(self):
        self.children = {}
        self.is_word = False
        self.word = None
        self.freq = 0


class Trie:
    """ Represents the Trie Data Structure.
    The root point to the root element of the trie.
    The words variable points to the list of all the words fetched from a keyword."""

    def __init__(self):
                self.root = Node()
                self.words = []

    def insert_word(self, word):
                node = self.root
                for a in list(word):
                    if not node.children.get(a):
                        node.children[a] = Node()

                    node = node.children[a]
                node.is_word = True
                node.word = word
                node.freq = 1

    def insert_word(self, word, freq):
            node = self.root
            for a in list(word):
                    if not node.children.get(a):
                        node.children[a] = Node()
                    node = node.children[a]

            node.is_word = True
            node.freq = int(freq)
            node.word = word

    def search_word(self, word):
        status = True
        node = self.root
        for c in list(word):
            if not node.children.get(c):
                status = False
                break
            node = node.children[c]

        if not node:
            return False
        else:
            return node.is_word and status

    def search_with_typo(self, typoLength, word):
        currentRow = range(len(word) + 1)
        # print('Current Row is: ' + str(type(currentRow)))
        results = []
        node = self.root
        for char_ in node.children:
            print('Current row length is: ' + str(currentRow.__len__()))

            self.search_recursive(node.children[char_], char_, word, currentRow,
                            results, typoLength)

        return results

    def search_recursive(self, node, letter, word, previousRow, results, maximumCost):
        columns = len(word) + 1
        currentRow = [previousRow[0] + 1]

        for column in range(1, columns):
            insert = currentRow[column - 1] + 1
            delete = previousRow[column] + 1

            if word[column - 1] != letter:
                replace = previousRow[column - 1] + 1
            else:
                replace = previousRow[column - 1]

            currentRow.append(min(insert, delete, replace))

        if currentRow[-1] <= maximumCost and node.word is not None:
            results.append((node.word, currentRow[-1]))
            #print('Result is: ' + str(results))

        if min(currentRow) <= maximumCost:
            for letter in node.children:
                self.search_recursive(node.children[letter], letter, word, currentRow,
                                results, maximumCost)



    def create_trie(self):
        """ Creates a Trie by picking words and their frequency from the corpus."""
        f = open("./corpus.txt", 'r')
        f1 = f.readlines()
        lines = 0
        for x in f1:
            xarray = x.split("\t")
            word = xarray[0]
            freq = xarray[1]
            self.insert_word(word, freq)
            lines += 1

    def suggestions(self, node, word):

            if node.is_word:
                self.words.append({ 'word': word, 'freq': node.freq})
            for c, n in node.children.items():
                if self.words.__len__() > MAX_COUNT:
                    break
                else:
                    self.suggestions(n, word+c)

    def all_suggestions(self, key):
        node = self.root
        not_found = False
        self.words.clear()
        self.words = []
        temp_word = ''
        for a in list(key):
            if not node.children.get(a):
                not_found = True
                break
            temp_word += a
            node = node.children[a]

        if not_found or node.is_word and not node.children:
            return 0

        self.suggestions(node, temp_word)
        return 1


# Not used now.
class Parts:
    """ This class is used for processing the corpus and storing all parts of the words and doing  a reverse
    mapping of all the parts t their respective words that they belong to"""
    def __init__(self):
        self.map = {}
        self.words = []

    def insert_cuts(self, word, freq):
            word = str(word)
            length = 2
            word_length = int(str(word).__len__())
            while length <= word_length:
                    i = 0
                    j = i + length

                    while j <= word_length:
                        # print('i is: ' + str(i) + ' and j is: ' + str(j))
                        prefix = str(word)[i:j]
                        # print('prefix is: ' + str(prefix))
                        i = i + 1
                        j = j + 1
                        if self.map.get(prefix) is None:
                            pref_array = []
                            pair = {'word' : word, 'freq' : freq}
                            pref_array.append(pair)
                            self.map[prefix] = pref_array
                        else:
                            pref_array = self.map.get(prefix)
                            pair = {'word': word, 'freq': freq}
                            pref_array.append(pair)
                            self.map[prefix] = pref_array

                    length = length + 1

    def insert(self):
        f = open("./corpus.txt", 'r')
        f1 = f.readlines()
        lines = 0
        for x in f1:
            xarray = x.split("\t")
            word = xarray[0]
            freq = xarray[1]

            self.insert_cuts(word, freq)

            lines = lines + 1
            if lines > 333333:
                break

    def print_map(self):
        for k in self.map:
            print('\n' + str(k) + '\t ' + str(self.map.get(k)))

    def suggestion(self, word):
        if self.words is not None:
            self.words.clear()
        self.words = []
        self.words = self.map.get(word)


class OurRepo:
    """
    Singleton class for storing the corpus as a Trie.
    """
    __instance = None

    @staticmethod
    def getInstance():
        """ Static access method. """
        if OurRepo.__instance is None:
            OurRepo()
        return OurRepo.__instance

    def __init__(self):
        if OurRepo.__instance is not None:
            raise Exception('This is a singleton class')
        else:
            OurRepo.__instance = self
            self.our_trie_root = Trie()
            self.our_map = Parts()











