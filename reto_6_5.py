
from collections import defaultdict

print("----Anagram Checker----")


def find_anagrams(word_list: list):
    anagram_dict: dict = defaultdict(list)

    for word in word_list:
        try:
            if not isinstance(word, str):
                raise TypeError
            key: str = "".join(sorted(word.lower()))
            anagram_dict[key].append(word)
        except TypeError:
            continue

    return [group for group in anagram_dict.values() if len(group) > 1]

original_list: list = ["Amor", "roma", "ramo", 14, "carro", 54, "arroc", "perro", "rEpro", "python", 23]
print(find_anagrams(original_list))
