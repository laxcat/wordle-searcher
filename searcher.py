#!/usr/bin/env python3

import words
import re
import sys
from os import get_terminal_size


CYAN = '\033[96m'
WHITE = '\033[37m'
GREEN = '\033[92m'
YELLOW = '\033[93m'
RED = '\033[91m'
END = '\033[0m'


def show_help():
    print(f'{WHITE}Simple:{END} lowercase for yellows, uppercase for greens, dashes for grays')
    print(f'eg: af---    Ta--k')

def show_advanced_help():
    print(f'{WHITE}Advanced:{END} use pipe (|) to seperate slots, alowing for multiple yellows per slot')
    print(f'eg: a|f|-|-|-    a|f|||    a|f|||')
    print(f'{WHITE}Advanced:{END} use comma then list of letters to indicate gray (excluded) letters')
    print(f'eg: af---,m    a|f|-|-|-,m    a|f|||,m')


try:
    loop_count = 0
    while(True):
        loop_count += 1

        print()
        print(f'{WHITE}Input search pattern.{END} (enter \'?\' or \'help\' for help)')
        if loop_count == 1:
            show_help()
        user_input = input('> ')

        # special case to display help
        if user_input == '?' or user_input == 'help':
            show_help()
            show_advanced_help()
            continue

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

        # search the word lists
        def search(words):
            found = []
            # each word in big list
            for word in words:
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
            return found
        answers_found = search(words.answers)
        accepted_found = search(words.accepted)
        
        # results
        print()
        print(f'pattern = {CYAN}{pattern}{END}   ', end='')
        print(f'contains = ({YELLOW}{",".join(yellows)}{END})   ', end='')
        print(f'excludes = ({RED}{",".join(grays)}{END})')
        def show_answers(answers, type, COLOR):
            per_line = get_terminal_size().columns // 7
            print(COLOR, end='')
            length = len(answers)
            for index, word in enumerate(answers):
                print(word, end='')
                if index < length - 1:
                    print(', ', end='')
                if index % per_line == per_line - 1 or index == length - 1:
                    print()
            print(f'{length}{END} found in {type} list')
        show_answers(answers_found, 'answers', GREEN)
        show_answers(accepted_found, 'accepted', YELLOW)

# graceful exit on user break
except KeyboardInterrupt:
    print('')
except Exception:
    traceback.print_exc(file=sys.stdout)
