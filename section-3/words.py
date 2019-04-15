# 'import words' in REPL would now only import the fetch_words definition
#       giving us more control to run as a program rather than a script
# like so - 
# import words
# words.fetch_words()
# OR
# from words import fetch_words
# fetch_words()
# NOW this can now ONLY be used as import and run as part of another program
# CANNOT be run directly in OS shell using 'python words.py' - this would simply
# define the fetch_words() function and exit immediately
def fetch_words():
    from urllib.request import urlopen
    with urlopen('http://sixty-north.com/c/t.txt') as story:
        story_words = []
        for line in story:
            line_words = line.decode('utf-8').split()
            for word in line_words:
                story_words.append(word)

    for word in story_words:
        print(word)

# if executed as a script then call the function and execute it
# which means when run as an import only the function would be defined - not executed immediately
if __name__ == '__main__':
    fetch_words()