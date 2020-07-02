from collections import Counter
from difflib import SequenceMatcher
from itertools import product
import re

IDENTICAL = 1.0
TOP_NUMBER = 10
RSS_FEED = '/Users/daniellibatique/code/github-repos/challenges/03/rss.xml'
SIMILAR = 0.87
TAG_HTML = re.compile(r'<category>([^<]+)</category>')


def get_tags():
    """Find all tags (TAG_HTML) in RSS_FEED.
    Replace dash with whitespace.
    Hint: use TAG_HTML.findall"""
    with open(RSS_FEED) as f:
        raw = f.read()
    return re.findall(TAG_HTML, raw)


def get_top_tags(tags):
    """Get the TOP_NUMBER of most common tags
    Hint: use most_common method of Counter (already imported)"""
    return Counter(tags).most_common()

test = get_tags()
print(product(get_top_tags(test)[0], get_top_tags(test)[1]))

for x in get_top_tags(test):
    product(x[0], )

def get_similarities(tags):
    """Find set of tags pairs with similarity ratio of > SIMILAR
    Hint 1: compare each tag, use for in for, or product from itertools (already imported)
    Hint 2: use SequenceMatcher (imported) to calculate the similarity ratio
    Bonus: for performance gain compare the first char of each tag in pair and continue if not the same"""
    pass

#
# if __name__ == "__main__":
#     tags = get_tags()
#     top_tags = get_top_tags(tags)
#     print('* Top {} tags:'.format(TOP_NUMBER))
#     for tag, count in top_tags:
#         print('{:<20} {}'.format(tag, count))
#     similar_tags = dict(get_similarities(tags))
#     print()
#     print('* Similar tags:')
#     for singular, plural in similar_tags.items():
#         print('{:<20} {}'.format(singular, plural))
