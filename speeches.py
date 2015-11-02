from __future__ import unicode_literals
import io
import re
from pprint import pprint

# Where are the speeches stored?
trump_file_name = 'trump.txt'
obama_file_name = 'obama.txt'

# Open connections to the files
trump_file = io.open(trump_file_name, 'r', encoding='utf-8')
obama_file = io.open(obama_file_name, 'r', encoding='utf-8')


# Define the function that does what we want to do
def count_words(file_connection):
    '''
    Count all words in a file and return dictionary
    '''

    # Empty dictionary to hold the results
    out_dict = {}
    # First entry: Total words counts
    out_dict['total_words'] = 0
    
    # Loop through the lines in the input file
    for line in file_connection:

        # Remove everything that is not a letter (if you want to know more look up 'regular expressions')
        clean_line = re.sub('[^A-Za-z]', ' ', line)
        
        # Split the line into single words
        words = clean_line.split()

        # Actually count the words: 
        for word in words:
            
            out_dict['total_words'] += 1
            
            # if we enounter the word for the first time, we create a new entry in the dictionary
            if word not in out_dict.keys():
                out_dict[word] = 1
                
            # If not, we increment the word count by one
            else:
                out_dict[word] += 1
            
    return out_dict

# Apply the function to the two text files
obama_dictionary = count_words(file_connection=obama_file)
trump_dictionary = count_words(file_connection=trump_file)

# Close the connection to the files
trump_file.close()
obama_file.close()

obama_measure = float(obama_dictionary['I']) / float(obama_dictionary['total_words'])
trump_measure = float(trump_dictionary['I']) / float(trump_dictionary['total_words'])

print 'Obama said "I" {0} times in a speech {1} words long. That is: {2} per word'.format(obama_dictionary['I'], obama_dictionary['total_words'], round(obama_measure, 3))
print 'Trump said "I" {0} times in a speech {1} words long. That is: {2} per word'.format(trump_dictionary['I'], trump_dictionary['total_words'], round(trump_measure, 3))
