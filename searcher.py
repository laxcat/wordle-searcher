#!/usr/bin/env python3

import words
import re
import sys

try:
    while(True):
        user_input = input('Input search pattern. Lowercase for yellows, uppercase for greens, dashes for greys.\n')

        is_complex = bool('|' in user_input)
        has_gray = bool(',' in user_input)

        # reject user input if not 5 letters and not a complex pattern
        if not is_complex and not has_gray and len(user_input) != 5:
            continue

        # will form pattern that expects a green in the proper slot, 
        # and ensure the yellows are NOT in that slot.
        pattern = r''
        # we'll capture yellows and just make sure the word contains them.
        yellows = []
        grays = [] 

        # comma at end of pattern indicates list of grays, to ensure exclude words that have them
        if has_gray:
            temp = user_input.split(',')
            user_input = temp[0]
            grays = list(temp[1])

        # if complex parsing detected, "letters" could be groups of letters 
        # (but are treated the same way when making the pattern)
        if is_complex:
            user_input = user_input.split('|')

        # each part (letter or group letters) of input
        for part in user_input:
            if part.isupper():
                pattern += part.lower()
            elif part.islower():
                pattern += f'[^{part}]'
                # might be group of letters or single part
                for letter in part:
                    if letter not in yellows:
                        yellows.append(letter)
            # expecting dash but could be anything that doesn't pass isupper && islower
            else:
                pattern += '[a-z]'

        y_str = ','.join(yellows)
        g_str = ','.join(grays)
        print(f'pattern = {pattern}  contains = {y_str}  excludes = {g_str}')
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
                for g in grays:
                    if g in word:
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
