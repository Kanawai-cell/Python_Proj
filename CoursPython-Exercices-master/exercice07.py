from collections import Counter
import string

def get_letter_count(word):
   # Votre code ici
#     counter = Counter()
#     for words in word.split():
#        counter.update(words)
#     return sum(counter.itervalues())

       list_of_words = word.split()
       print(len(list_of_words))
       return len(list_of_words)

def run():
   assert get_letter_count("Oui") == 3
   assert get_letter_count("Bonjour") == 7
   assert get_letter_count("") == 0
   assert get_letter_count(".........hein???") == 4
   assert get_letter_count("Attention y'a quatre mots !") == 21
