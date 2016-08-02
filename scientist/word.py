class Word:
    """A word with extra properties that have been given by SyntaxNet.

    Attributes:
        word: The word, as a string.
        coarse: The word's coarse part of speech.
        fine: The word's fine part of speech.
        children: An array of any of the word's children.
    """

    def __init__(self, word, coarse, fine, children=None):
        """Inits a Word with the word's attributes."""

        self.word = word
        self.coarse = coarse
        self.fine = fine
        self.children = children

    def __str__(self):
        return str(self.__dict__)

    def __repr__(self):
        return self.__str__()

    def find_elements(self, word=None, coarse=None, fine=None, cwords=None, ccoarse=None, cfine=None):
        """Recursively searches for elements that match the given parameters,
        searching through this element's children and their sub-children.

        Args:
            word: The element's word string.
            coarse: The element's coarse part of speech.
            fine: The element's fine part of speech.
            cwords: A list of words that the element's children are allowed to
                have.
            ccoarse: A list of the coarse parts of speech that the element's
                children are allowed to have.
            cfine: A list of the fine parts of speech that the element's
                children are allowed to have.

        Returns:
            A list of matching word elements.
        """

        matching = []

        if self.matches(word=word, coarse=coarse, fine=fine, cwords=cwords, ccoarse=ccoarse, cfine=cfine):
            matching.append(self)

        if self.children:
            for child in self.children:
                matching += child.find_elements(word=word, coarse=coarse, fine=fine, cwords=cwords, ccoarse=ccoarse, cfine=cfine)

        return matching

    def matches(self, word=None, coarse=None, fine=None, cwords=None, ccoarse=None, cfine=None):
        """Checks to see if this element matches the given parameters.

        Args:
            word: The element's word string.
            coarse: The element's coarse part of speech.
            fine: The element's fine part of speech.
            cwords: A list of words that the element's children are allowed to
                have.
            ccoarse: A list of the coarse parts of speech that the element's
                children are allowed to have.
            cfine: A list of the fine parts of speech that the element's
                children are allowed to have.

        Returns:
            True if it matches all given parameters, false if it does not.
        """

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

            if cwords:
                for word in cwords:
                    if word not in children_words: return False

            if ccoarse:
                for coarse in ccoarse:
                    if coarse not in children_coarse: return False

            if cfine:
                for fine in cfine:
                    if fine not in children_fine: return False

        return True
