import sys
from urllib.request import urlopen

'http://sixty-north.com/c/t.txt'
def fetch_words(url):
    story = urlopen(url)
    story_words = []
    for line in story:
        line_words = line.decode('utf8').split()
        for word in line_words:
            story_words.append(word)
    story.close()
    return story_words


def print_items (items):
    for item in items:
        print(item)


def main():
    words = fetch_words()
    print_items(words)

if __name__ == '__main__':
    main()

