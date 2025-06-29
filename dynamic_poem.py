import keyword
import sys

reserved_words = keyword.kwlist

inp = [word.lower() if word.lower() not in reserved_words else word.lower() + '_' for word in sys.argv[1:]]
paren_count = 0


with open('newpoem.py', 'w') as f:
    for word in inp:
        paren_count += 1
        f.write(f"def {word}(x):  return '{word}' + ' ' + x\n")
    for i, word in enumerate(inp):
        if i == 0:
            f.write(f'print({word}(')
        elif i not in [0, len(inp) - 1]:
            f.write(f"{word}(")
        elif i == len(inp) - 1:
            f.write(f"{word}(''){')'* paren_count}")
      
print(f"Created newpoem.py with {len(inp)} functions based on input words.")
print("You can now import this file and use the functions defined in it.")
print("Example usage: from newpoem import word1, word2")
print("Then call the functions like: print(word1('your text here'))")

from newpoem import *

