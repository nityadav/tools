#!/usr/bin/python

import argparse

parser = argparse.ArgumentParser(description='Description of the script.')
parser.add_argument('foo', help='Description of the required argument')
parser.add_argument('-b', '--bar', dest='bar', help='Description of the optional argument')
parser.add_argument('-f', dest='f', action='store_true', help='Description of the optional argument without a value')
args = parser.parse_args()

print args.foo
print args.bar
print args.f
