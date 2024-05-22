# your code goes here!
class Anagram:
    def __init__(self, word):
        self.wordletters = sorted([letter for letter in word])
       
    def match(self, wordlist):
        match_wordlist = []

        for word in wordlist:
            if sorted([letter for letter in word]) == self.wordletters:
                match_wordlist.append(word)

        return match_wordlist