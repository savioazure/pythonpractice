#!/usr/bin/env python3
"""
Author : Savio Kerber <savioazure@gmail.com>
Date   : 2023-09-08
Purpose: picnic time, enumerating
"""

import argparse


# --------------------------------------------------
def get_args():
    """Get command-line arguments"""

    parser = argparse.ArgumentParser(
        description='picninc game',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)

    parser.add_argument('item',
                        metavar='str',
                        nargs='+',
                        help='items to bring')

    parser.add_argument('-s',
                        '--sorted',
                        action='store_true',
                        help='Sort the items',
                        # metavar='str',
                        
                        default='False')

    
    return parser.parse_args()


# -------------------test de commit-------------------------------
def main():
    """Make a jazz noise here"""

    args = get_args()
    items = args.item
    num = len(items)

    if args.sorted:
        items.sort()

    bringing = ''
    if num == 1:
        bringing = items [0]
    elif num == 2:
        bringing = ' and '.join(items)
    else:
        items[-1] = 'and ' + items[-1]
        bringing = ', '.join(items)


    print('You are bringing {}.'.format(bringing))

# --------------------------------------------------
if __name__ == '__main__':
    main()
