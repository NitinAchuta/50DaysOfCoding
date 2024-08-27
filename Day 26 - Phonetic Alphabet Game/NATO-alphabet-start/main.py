# student_dict = {
#     "student": ["Angela", "James", "Lily"], 
#     "score": [56, 76, 98]
# }

# #Looping through dictionaries:
# for (key, value) in student_dict.items():
#     #Access key and value
#     pass

# import pandas
# student_data_frame = pandas.DataFrame(student_dict)

# #Loop through rows of a data frame
# for (index, row) in student_data_frame.iterrows():
#     #Access index and row
#     #Access row.student or row.score
#     pass

# Keyword Method with iterrows()
# {new_key:new_value for (index, row) in df.iterrows()}dddd

import pandas as pd


phon_alphabet = pd.read_csv('NATO-alphabet-start/nato_phonetic_alphabet.csv')


phon_dictionary = {row.letter:row.code for (index, row) in phon_alphabet.iterrows()}
print(phon_dictionary)

def generate_phonetic():
    word = input('Enter a word: ').upper()
    try:
        phon_word = [phon_dictionary[letter] for letter in word]
    except KeyError:
        print("Sorry, only letters in the alphabet please.")
        generate_phonetic()
    else:
        print(phon_word)

generate_phonetic()