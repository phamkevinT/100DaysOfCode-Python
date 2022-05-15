# Keyword Method with iterrows()
# {new_key:new_value for (index, row) in df.iterrows()}

import pandas

data = pandas.read_csv('nato_phonetic_alphabet.csv')

# Create a dictionary
phonetic_dictionary = {row.letter: row.code for (
    index, row) in data.iterrows()}
print(phonetic_dictionary)

# Create a list of phonetic code words from user's input
word = input("Enter a word: ").upper()
output_list = [phonetic_dictionary[letter] for letter in word]
print(output_list)
