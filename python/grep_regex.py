'''
program: grep_regex.py
created: 2016-06-02 -- 15 CEST
author: tc
'''

import sys
import re
import os


def grep_regex(filename, regex):
    assert os.path.isfile(filename)
    with open(filename, 'r') as f:
        lines = [x.strip() for x in f.readlines()]
        for line in lines:
            if re.search(regex, line):
                print line


if __name__ == '__main__':
    if len(sys.argv) != 3:
        sys.exit('Correct usage:\n    python grep_regex.py <regex> <file>')
    grep_regex(sys.argv[2], sys.argv[1])
