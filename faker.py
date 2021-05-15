import json
from random import choice, randint


class DhivehiFaker:
    def __init__(self, words_file=None, endings_file=None, sentence_length=None, paragraph_length=None):
        if words_file is None:
            words_file = 'data/thaana.json'

        if endings_file is None:
            endings_file = 'data/end.json'

        if sentence_length is None:
            sentence_length = randint(5, 10)

        if paragraph_length is None:
            paragraph_length = randint(5, 15)

        self.word_list = json.load(open(words_file, encoding="utf-8"))
        self.endings_list = json.load(open(endings_file, encoding="utf-8"))
        self.sentence_length = sentence_length
        self.paragraph_length = paragraph_length

    def word(self):
        word = choice(self.word_list)
        return word

    def words(self, count, array=False):
        if array:
            return [self.word() for _ in range(count)]

        words = ""
        for _ in range(count):
            words += f"{self.word()} "
        return words

    def sentence(self):
        length = self.sentence_length
        sentence = f"{self.words(length)} {choice(self.endings_list)}."
        return sentence

    def sentences(self, count=randint(5, 20), array=False):
        if array:
            return [self.sentence() for _ in range(count)]

        sentences = ""
        for _ in range(count):
            sentences += self.sentence() + " "
        return sentences

    def paragraph(self):
        length = self.paragraph_length
        paragraph = self.sentences(length)
        return paragraph

    def paragraphs(self, count=randint(5, 10), array=False):
        if array:
            return [self.paragraph() for _ in range(count)]

        paragraphs = ""
        for _ in range(count):
            paragraphs += f"{self.paragraph()}\n\n"
        return paragraphs.rstrip()
