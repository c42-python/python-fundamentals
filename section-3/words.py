# using an entry function to easily use the code as script (called main here)
# otherwise can be imported to use function defs individually in other programs
def fetch_words():
    from urllib.request import urlopen
    with urlopen('http://sixty-north.com/c/t.txt') as story:
        story_words = []
        for line in story:
            line_words = line.decode('utf-8').split()
            for word in line_words:
                story_words.append(word)
    return story_words

def print_items(items):
    for item in items:
        print(item)

def main():
    words = fetch_words()
    print(words)

# if executed as a script then call the function and execute it
# which means when run as an import only the function would be defined - not executed immediately
if __name__ == '__main__':
    main()