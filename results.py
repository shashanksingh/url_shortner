# 0. work for multiple higlithing words
# 1. find a substring in paragaph
# 2. if it is present then highlight <b> {text} </b>
# 3. if it is not present, return paragraph
#
# paragraph : string with no html formatting

import re

HTML_OPENING_TAG_FOR_HIGLIHTER = "<q>"
HTML_END_TAG_FOR_HIGLIHTER = "</q>"


def query_highlighter(paragraph: str, query_to_be_highlighted: str) -> str:
    list_of_query_words = re.split(" ", query_to_be_highlighted)

    for word in list_of_query_words:
        paragraph = highlighter(paragraph, word)
    return paragraph


def highlighter(paragraph: str, word_to_be_highlighted: str) -> str:
    return re.sub(word_to_be_highlighted,
                  f"{HTML_OPENING_TAG_FOR_HIGLIHTER}{word_to_be_highlighted}{HTML_END_TAG_FOR_HIGLIHTER}",
                  paragraph)


assert highlighter("a b c", "b") == "a <q>b</q> c"
assert highlighter("a b b c", "b") == "a <q>b</q> <q>b</q> c"
assert highlighter("a b c b", "b") == "a <q>b</q> c <q>b</q>"
assert highlighter("a c", "b") == "a c"

# single word query
assert query_highlighter("a b c", "b") == "a <q>b</q> c"
assert query_highlighter("a b b c", "b") == "a <q>b</q> <q>b</q> c"
assert query_highlighter("a b c b", "b") == "a <q>b</q> c <q>b</q>"

# multiple word query
assert query_highlighter("a bbb c", "bb b") == "a <q>bb</q><q>b</q> c"
assert query_highlighter("a bbbb c", "bb b") == "a <q>bb</q><q>bb</q> c"
