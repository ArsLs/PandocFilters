import sys
from panflute import *

headers = []


def headerAlreadyExistingFilter(elem, doc):
    if isinstance(elem, Header):
        text = stringify(elem)
        if (text in headers):
            sys.stderr.write("Warning: Header `" + text + "` already exists in document\n")
        else:
            headers.append(text)

def top3LevelsUpperFilter(elem, doc):
    if (isinstance(elem, Header)):
        if (elem.level > 2):
            return Header(Str(stringify(elem).upper()), level=elem.level)


def makeBold(doc):
    doc.replace_keyword('BOLD', Strong(Str('BOLD')))


if __name__ == '__main__':
    run_filters([headerAlreadyExistingFilter, top3LevelsUpperFilter], prepare=makeBold)