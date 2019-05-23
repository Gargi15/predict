class Parts():

    def __init__(self):

        self.map = {}
        self.words = []

    def insert_cuts(self, word):
        word = str(word)
        length = 2
        word_length = int(str(word).__len__())
       # print('length is: ' + str(length) + ' word length is: ' + str(word_length))
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
                    pref_array.append(word)
                    self.map[prefix] = pref_array
                else:
                    pref_array = self.map.get(prefix)
                    pref_array.append(word)
                 #   print('array is: ' + str(pref_array))
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

           # print("\n\n\n\n line no: " + str(lines) + "word is: " + str(word) + " and freq is: " + str(freq) )
            self.insert_cuts(word)

            lines = lines + 1
            if lines > 333333:
                break

    def print_map(self):
        print('INSIDE PRINT')

        for k in self.map:
          print('\n' + str(k) + '\t ' + str(self.map.get(k)))

    def suggestion(self, word):
        if self.words is not None:
            self.words.clear()
        self.words = []
        print('MAp length is: ' + str(self.map.__len__()))
        self.words = self.map.get(word)



class Node():
    def __init__(self):

        self.children = {}
        self.is_word = False
        self.freq = 0


class Trie():

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
        node.freq = 1

    def insert_word_with_freq(self, word, freq):
        node = self.root

        for a in list(word):
            if not node.children.get(a):
                node.children[a] = Node()

            node = node.children[a]

        node.is_word = True
        node.freq = int(freq)

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

    def create_trie(self, corpus):

        for word in corpus:
            self.insert_word(word)

    def create_trie_from_file(self):

        f = open("./corpus.txt", 'r')
        f1 = f.readlines()
        lines = 0

        for x in f1:
            xarray = x.split("\t")
            word = xarray[0]
            freq = xarray[1]
            # print("word is: " + str(word) + " and freq is: " + str(freq))
            self.insert_word_with_freq(word, freq)

            lines = lines + 1
            if lines > 333333:
                break

    def suggestions(self, node, word):

            if node.is_word:
                self.words.append({ 'word': word, 'freq' : node.freq})

            for c, n in node.children.items():
                if self.words.__len__() > 25:
                    break
                else:
                    self.suggestions(n, word+c)

    def AllSuggestions(self, key):
        node = self.root
        not_found = False
        self.words = self.words.clear()
        self.words = []
        temp_word = ''

        for a in list(key):
            if not node.children.get(a):
                not_found = True
                break

            temp_word += a
            node = node.children[a]

        if not_found:
            return 0
        elif node.is_word and not node.children:
            return -1

        self.suggestions(node, temp_word)

        # for s in self.words:
        #     print(s)
        return 1


def read_file():

    f = open("/Users/gabiswas/Documents/purge/purge/delete_emails/corpus.txt", 'r')
    f1 = f.readlines()
    lines = 0

    for x in f1:
        xarray = x.split("\t")
        word = xarray[0]
        freq = xarray[1]
        print("word is: " + str(word) + " and freq is: " + str(freq))

        lines = lines + 1
        if lines > 5:
            break


# Create your views here.
class OurTrie:

    __instance = None

    @staticmethod
    def getInstance():
        """ Static access method. """
        if OurTrie.__instance is None:
            OurTrie()
        return OurTrie.__instance

    def __init__(self):
        if OurTrie.__instance is not None:
            raise Exception("This class is a singleton!")
        else:
            OurTrie.__instance = self
            self.our_trie_root = Trie()
            self.our_map = Parts()











