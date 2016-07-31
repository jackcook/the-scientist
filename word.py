from collections import Counter

class Word:

    word = None
    coarse = None
    fine = None
    children = None

    def __init__(self, word, coarse, fine, children=None):
        self.word = word
        self.coarse = coarse
        self.fine = fine
        self.children = children

    def __str__(self):
        return str(self.__dict__)

    def find_elements(self, word=None, coarse=None, fine=None, cwords=None, ccoarse=None, cfine=None):
        matching = []

        if self.matches(word=word, coarse=coarse, fine=fine, cwords=cwords, ccoarse=ccoarse, cfine=cfine):
            matching.append(self)

        if self.children:
            for child in self.children:
                matching += child.find_elements(word=word, coarse=coarse, fine=fine, cwords=cwords, ccoarse=ccoarse, cfine=cfine)

        return matching

    def matches(self, word=None, coarse=None, fine=None, cwords=None, ccoarse=None, cfine=None):
        if word and self.word != word: return False
        if coarse and self.coarse != coarse: return False
        if fine and self.fine != fine: return False

        if self.children:
            children_words = []
            children_coarse = []
            children_fine = []

            for child in self.children:
                children_words.append(child.word)
                children_coarse.append(child.coarse)
                children_fine.append(child.fine)

            if cwords and Counter(children_words) != Counter(cwords): return False
            if ccoarse and Counter(children_coarse) != Counter(ccoarse): return False
            if cfine and Counter(children_fine) != Counter(cfine): return False

        return True
