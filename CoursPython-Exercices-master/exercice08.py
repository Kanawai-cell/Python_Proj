from collections import Counter
import string

def get_word_count(sentences):
       # Votre code ici
       # counter = Counter()
       # for sentence in sentences.split():
       #        counter.update(word)
       # return sum(counter.itervalues())
       
       characters = "'!?"

       for x in range(len(characters)):
              sentences = sentences.replace(characters[x],"")

       list_of_words = sentences.split()
       print(len(list_of_words))
       return len(list_of_words)

       # mots = 0
       # for i in range(sentence) :
       #        if sentence == " " :
       #               mots = mots + 1
       # return

def run():
   assert get_word_count("Bonjour") == 1
   assert get_word_count("Bonjour toi") == 2
   assert get_word_count("Bonjour ca va ?") == 3
   assert get_word_count("Bonjour ca va toi ?!") == 4
   assert get_word_count("") == 0