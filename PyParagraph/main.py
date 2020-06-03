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
import re
import string

# Initialize Variables
sentences = []
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
        # try to open csv file as read only
        input_file = open(input_path, "r")
    except:
        # if the file cannot be found, as if the user would like to try again
        print("I could not find that file, please be sure to save the file in the raw_data folder and enter the full filename, including the extension (i.e. .txt).")
        try_again = input("Would you like to try again (y/n)? ")
        if try_again == "y":
            # if the user does wish to try again, ask for the filename again
            input_file_name = input("Please try again: ")
            input_path = os.path.join('.', 'raw_data', input_file_name)
            file_not_found = True 
        else:
            # if the user does not wish to try again, exit the program
            sys.exit('Thank you for trying PyParagraph')
    else:
        # if the file can be found, exit the loop
        break

# read in the entire file
whole_file = input_file.read()

# close the file
input_file.close()

# divide the file by newline returns
lines = re.split("\n\n", whole_file)

# check for multiple sentences on the same line
for line in lines:
    counter = line.count('.') + line.count('!') + line.count('?')
    if counter == 1:
        # this is for paragraphs that have a single sentence per line
        sentences.append(line)
    elif counter == 2:
        # this is for the paragraph that has a single sentence per line, but one of the lines has an abbreviation with a "."
        sentences.append(line)
    else:
        # this is for paragraphs that are entirely on one line
        sentences = line.split('.')

# break down each sentence
for sentence in sentences:

    # if the sentence is not blank, then increment the sentence counter
    if len(sentence) > 0:
        sentence_count = sentence_count + 1

        # strip the punctuation from the sentences
        simple = sentence.translate(str.maketrans('', '', string.punctuation))

        # split the stripped sentences into the individual words
        words = simple.split(' ')
    
        # count the number of words and the total number of letters in all the words
        for word in words:
            # if the word is not blank, then increment the word & letter counters
            if len(word) > 0:
                total_word_count = total_word_count + 1
                total_letter_count = total_letter_count + len(word)

# calculate the average letter count per word
avg_letter_count = round(total_letter_count / total_word_count,2)

# calculate the average word count per sentence
avg_sentence_length = round(total_word_count / sentence_count,2)

# print the analysis to the terminal window
print(f"""
Paragraph Analysis
-----------------
Approximate Word Count: {total_word_count}
Approximate Sentence Count: {sentence_count}
Average Letter Count: {avg_letter_count}
Average Sentence Length: {avg_sentence_length}
""")

# Just for fun
if sentence_count < 5:
    print("You seem rather simple minded")
elif (avg_letter_count > 5 and sentence_count < 6):
    print("You think you're pretty smart, eh?")
elif (avg_letter_count > 5 and sentence_count >= 6):
    print("You are quite the chatty one, you do not have to show everyone how smart you are.")
else:
    print("You have created some average thoughts")

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