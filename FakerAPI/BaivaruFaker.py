import json
import os
from random import choice, randint


class BaivaruFaker:
    def __init__(self, words_file="thaana.json", endings_file="end.json", sentence_length=randint(5, 10),
                 paragraph_length=randint(5, 15)):

        self.script_dir = os.path.dirname(__file__)
        self.words_file_abs = os.path.join(self.script_dir, words_file)
        self.ending_file_abs = os.path.join(self.script_dir, endings_file)
        self.word_list = json.load(open(self.words_file_abs, encoding="utf-8"))
        self.endings_list = json.load(open(self.ending_file_abs, encoding="utf-8"))
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
        sentence = f"{self.words(length)} {choice(self.endings_list)}. "
        return sentence

    def sentences(self, count=randint(5, 20), array=False):
        if array:
            return [self.sentence() for _ in range(count)]

        sentences = ""
        for _ in range(count):
            sentences += self.sentence()

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
