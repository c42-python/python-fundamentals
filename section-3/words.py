""" Retrive and print words from an URL.

Usage:
    python words.py <URL>
"""
import sys

# using an entry function to easily use the code as script (called main here)
# otherwise can be imported to use function defs individually in other programs
def fetch_words(url):
    """ Fetch a list of words from an URL.

    Args:
        url: The URL of an UTF-8 text document.

    Returns:
        A list of strings containing the words from the 
        document
    """
    from urllib.request import urlopen
    with urlopen(url) as story:
        story_words = []
        for line in story:
            line_words = line.decode('utf-8').split()
            for word in line_words:
                story_words.append(word)
    return story_words


def print_items(items):
    """ Print items one per line

    Args:
        An iterable series of printable items 
    """
    for item in items:
        print(item)


# Easily pass function args via REPL
def main(url):
    """ Print each word from a text document from an URL
    
    Args:
        url: The url of a UTF-8 text document.

    """
    words = fetch_words(url)
    print(words)


# Pass params in script execution as command line positinal args
if __name__ == '__main__':
    url = sys.argv[1] # The 0th arg is module filename
    main(url)