# Hangman
import random
blanked_word = []
word_list = ["aardvark","baboon","camel", "apple", "banana", "rawberry"]
chosen_word = random.choice(word_list)

for i in range(0,len(chosen_word)-1):
    blanked_word[i].append("_")
print(f"Word is: {chosen_word} blanked word is: {blanked_word}")