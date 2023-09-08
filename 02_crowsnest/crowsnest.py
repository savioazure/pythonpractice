#!/usr/bin/env python3
"""
Author : Savio Kerber <savioazure@gmail.com>
Date   : 2023-09-08
Purpose: Crow's Nest -- choose the correct article
"""

import argparse


# --------------------------------------------------
def get_args():
    """Get command-line arguments"""

    parser = argparse.ArgumentParser(
        description="Crow's Nest -- choose the correct article",
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)

    parser.add_argument('word', metavar='word', help='A word argument')

    return parser.parse_args()


# --------------------------------------------------
def main():
    """Make a jazz noise here"""

    args = get_args()
    word = args.word
    article = 'an' if word[0].lower() in 'aeiou' else 'a'
    print(f'Ahoy, Captain, {article} {word} off the larboard bow!')
# --------------------------------------------------
if __name__ == '__main__':

    main()

