#!/usr/bin/env python3
"""
Author: Savio Kerber <savioazure@gmail.com>
Purpose: Say hello
"""

import argparse


# -------------------------------------------------------------------------
def get_args():
    """ Get arguments """
    parser = argparse.ArgumentParser(description='Say hello')
    parser.add_argument('-n', '--name', metavar='nombre', help='Name to greet',
                        default='Woorld')
    return parser.parse_args()


# --------------------------------------------------------------------------
def main():
    """ docstring triplequoted """
    args = get_args()
    print('Hello, ' + args.name + '!')


# -------------------------------------------------------------------------
if __name__ == '__main__':
    main()
