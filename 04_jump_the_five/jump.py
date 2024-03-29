#!/usr/bin/env python3
"""
Author : Savio Kerber <savioazure@gmail.com>
Date   : 2023-10-07
Purpose: Jump the Five
"""

import argparse


# --------------------------------------------------
def get_args():
    """Get command-line arguments"""

    parser = argparse.ArgumentParser(
        description='Jump The Five',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)

    parser.add_argument('text',
                        metavar='str',
                        help='Input text')

    return parser.parse_args()


# --------------------------------------------------
def main():
    """Make a jazz noise here"""

    args = get_args()
    jumper = {'1': '9', '2': '8', '3': '7', '4': '6', '5': '0',
              '6': '4', '7': '3', '8': '2', '9': '1', '0': '5'}

    # for char in args.text:
    #     print(jumper.get(char, char), end= '')
    # print()
    new_text = ''
    for char in args.text:
        new_text += jumper.get(char, char)    
    print(new_text)

#3rd solution  
# new_text = []
    # for char in args.text:
    #     new_text.append(jumper.get(char, char))
    # print(''.join(new_text))

# --------------------------------------------------
if __name__ == '__main__':
    main()


