#!/usr/bin/env python3
"""
Author : Savio  Kerber
Date   : 2022-11-12
Purpose: Crownsnest
"""

import argparse


# --------------------------------------------------
def get_args():
    """Get command-line arguments"""

    parser = argparse.ArgumentParser(
        description="Crown's Nest ",
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)

    parser.add_argument('word', metavar='word', help='A word')

    return parser.parse_args()


# --------------------------------------------------
def main():
    """Make a jazz noise here"""

    args = get_args()
    word = args.word
    article = ''
    if word[0].lower() in 'aeiou':
        article = 'an'
    else:
        article = 'a'
    print('Ahoy, Captain, {} {} off the larboard bow!'.format(article, word))



# --------------------------------------------------
if __name__ == '__main__':
    main()
