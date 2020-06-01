# a Python script to automate the analysis of any passage using these metrics. 
# The script will do the following:
# Import a text file filled with a paragraph of your choosing.
# Assess the passage for each of the following:
#       Approximate word count
#       Approximate sentence count
#       Approximate letter count (per word)
#       Average sentence length (in words)

# Import a text file filled with a paragraph of your choosing.

# Import Modules
import os
import sys

# Initialize Variables
sentences = []
phrases = []
words = []
sentence_count = 0
total_letter_count = 0
total_word_count = 0

# Create path for data file with proper formatting for the operating system
# input_path = os.path.join('.','raw_data','paragraph_3.txt')
input_file_name = input("Place the file containing the paragraph in the folder called raw_data, then enter the file name here: ")
input_path = os.path.join('.', 'raw_data', input_file_name)

file_not_found = True

while file_not_found:
    try:
        # open csv file as read only
        input_file = open(input_path, "r")
        # print(input_file.read())
    except:
        print("I could not find that file, please be sure to save the file in the raw_data folder and enter the full filename, including the extension (i.e. .txt).")
        try_again = input("Would you like to try again (y/n)? ")
        if try_again == "y":
            input_file_name = input("Please try again: ")
            input_path = os.path.join('.', 'raw_data', input_file_name)
            file_not_found = True
        else:
            sys.exit('Thank you for trying PyParagraph')
    else:
        file_not_found = False

whole_file = input_file.read()

input_file.close()

sentences = whole_file.split('.')

for sentence in sentences:
    #print(f"---{sentence}")
    if len(sentence) > 0:
        sentence_count = sentence_count + 1
    phrases = sentence.split(', ')
    for phrase in phrases:
        #print(phrase)
        words = phrase.split(' ')
        for word in words:
            #print(f"{word}: {len(word)}")
            if len(word) > 0:
                total_word_count = total_word_count + 1
                total_letter_count = total_letter_count + len(word)
    #print(f"words: {total_word_count}")
    #print(f"letters: {total_letter_count}")

# print(f"words: {total_word_count}")
# print(f"letters: {total_letter_count}")
avg_letter_count = round(total_letter_count / total_word_count,2)
avg_sentence_length = round(total_word_count / sentence_count,2)

print(f"""
Paragraph Analysis
-----------------
Approximate Word Count: {total_word_count}
Approximate Sentence Count: {sentence_count}
Average Letter Count: {avg_letter_count}
Average Sentence Length: {avg_sentence_length}
""")

# As an example, this passage:
#   “Adam Wayne, the conqueror, with his face flung back and his mane like a lion's, 
# stood with his great sword point upwards, the red raiment of his office flapping 
# around him like the red wings of an archangel. And the King saw, he knew not how, 
# something new and overwhelming. The great green trees and the great red robes swung 
# together in the wind. The preposterous masquerade, born of his own mockery, towered 
# over him and embraced the world. This was the normal, this was sanity, this was nature, 
# and he himself, with his rationality, and his detachment and his black frock-coat, he 
# was the exception and the accident a blot of black upon a world of crimson and gold.”

# ...would yield these results:

# Paragraph Analysis
# -----------------
# Approximate Word Count: 122
# Approximate Sentence Count: 5
# Average Letter Count: 4.6
# Average Sentence Length: 24.0