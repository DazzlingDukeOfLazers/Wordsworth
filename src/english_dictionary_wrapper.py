import nltk
from nltk.corpus import wordnet
import json


class EnglishDictionaryWrapper:
    def __init__(self) -> None:
        nltk.download('wordnet')
        pass

    def get_definitions(self, word):
        definitions = []
        for syn in wordnet.synsets(word):
            definitions.append(syn.definition())
        return definitions

    def save_dict(self, dict_to_save):
        word = dict_to_save["word"]
        filename = f"words/{word}.json"
        with open(f"{filename}", 'w') as f:
            json.dump(dict_to_save, f, indent=4)
