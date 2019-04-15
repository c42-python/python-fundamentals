# run from REPL using 
# python words.py
# 'import words' in REPL would also execute the code, printing the results which might not be 
#       what we want
from urllib.request import urlopen
with urlopen('http://sixty-north.com/c/t.txt') as story:
    story_words = []
    for line in story:
        line_words = line.decode('utf-8').split()
        for word in line_words:
            story_words.append(word)

for word in story_words:
    print(word)