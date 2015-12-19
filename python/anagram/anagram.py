def detect_anagrams(word, anagrams):
    return [anagram
            for anagram in anagrams
            if word.lower() != anagram.lower() and sorted(word.lower()) == sorted(anagram.lower())]
