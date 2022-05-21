# Text Spammer

# By theadventureofe(John Gormley)

# A python script that spams random text using pyautogui at random intervals.

# the_adventure_of_e λ

import pyautogui
import random

# CONTROL: Choose which character sets will be used
use_lower_case = True
use_upper_case = True
use_numerals = True
use_symbols1 = True
use_symbols2 = True

# CONTROL: Choose min/max characters before a SPACE
word_length_min = 4
word_length_max = 10

# CONTROL: Choose min/max words before an ENTER
sentence_length_min = 4
sentence_length_max = 10

# CONTROL: Choose min/max for random timing inbetween keypresses 
interval_min = 0.0002
interval_max = 0.0005

# CONTROL: choose how many random sentences will be printed 
sentences = 40

# Putting all selection booleans into a list
use_list = [use_lower_case, use_upper_case, use_numerals, use_symbols1, use_symbols2]

# Lists of character sets
lower_case = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
upper_case = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numerals = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols1 = ['!', '\"', '£', '$', '%', '^', '&', '*', '(', ')', '_', '-', '=', '+']
symbols2 = ['\\', '/', '|', ',', '<', '>', '?', '[', '{', '}', ']', '\'', '@', '#', '~']

# List of all character sets
set_list = [lower_case, upper_case, numerals, symbols1, symbols2]

# List for all selected character sets to be added to
char_list = []

# Add all selected character sets to char_list
for i in range(len(use_list)):
    if use_list[i] == True:
        for j in set_list[i]:
            char_list.append(j)

# Start printing random words
for i in range(sentences):
    for j in range(random.randint(sentence_length_min, sentence_length_max)):
        for k in range(random.randint(word_length_min, word_length_max)):
            pyautogui.write(random.choice(char_list), interval=random.uniform(interval_min, interval_max))
        pyautogui.write(" ", interval=random.uniform(interval_min, interval_max))
    pyautogui.press('enter', interval=random.uniform(interval_min, interval_max))
