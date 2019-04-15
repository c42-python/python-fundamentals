import sys

# using an entry function to easily use the code as script (called main here)
# otherwise can be imported to use function defs individually in other programs
def fetch_words(url):
    from urllib.request import urlopen
    with urlopen(url) as story:
        story_words = []
        for line in story:
            line_words = line.decode('utf-8').split()
            for word in line_words:
                story_words.append(word)
    return story_words


def print_items(items):
    for item in items:
        print(item)


# Easily pass function args via REPL
def main(url):
    words = fetch_words(url)
    print(words)
    

# Pass params in script execution as command line positinal args
if __name__ == '__main__':
    url = sys.argv[1]
    main(url)