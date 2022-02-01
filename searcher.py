#!/usr/bin/env python3

import words
import re
import sys

try:
    while(True):
        user_input = input('Input search pattern. Lowercase for yellows, uppercase for greens, dashes for greys.\n')

        if '|' not in user_input and len(user_input) != 5:
            continue

        # will form pattern that expects a green in the proper slot, 
        # and ensure the yellows are NOT in that slot.
        pattern = r''
        # we'll capture yellows and just make sure the word contains them.
        yellows = []


        if '|' in user_input:
            user_input = user_input.split('|')

        # each letter of input
        for letter in user_input:
            if letter.isupper():
                pattern += letter.lower()
            elif letter.islower():
                pattern += f'[^{letter}]'
                for letter_part in letter:
                    if letter_part not in yellows:
                        yellows.append(letter_part)
            # expecting dash but could be anything that doesn't pass isupper && islower
            else:
                pattern += '[a-z]'

        y_str = ','.join(yellows)
        print(f'pattern = {pattern}, contains = {y_str}')
        found = []

        # each word in big list
        for word in words.all:
            # matches green/not-yellow pattern
            if re.search(pattern, word):
                # ensure word contains all yellows
                passed = True
                for y in yellows:
                    if y not in word:
                        passed = False
                        break
                if passed:
                    found.append(word)
        
        # results
        if len(found):
            print(', '.join(found))
        print(f'{len(found)} found')

# graceful exit on user break
except KeyboardInterrupt:
    print('')
except Exception:
    traceback.print_exc(file=sys.stdout)
