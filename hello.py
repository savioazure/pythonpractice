#!/usr/bin/env python3
# Purpose: Say hello

import argparse

parser = argparse.ArgumentParser(description= 'Say hello')
parser.add_argument('-n', '--name', metavar='name', default='Kaoss', help='Name to greet')
args = parser.parse_args()
print (args)
print ('Hello, ' + args.name + '!')



