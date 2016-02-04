# Author: Nitin
# Usage example: python template.py hi -b 42 --foo bye
# Tested with python 3.4

import argparse

def main():
	# create the parser
	parser = argparse.ArgumentParser(description="This is some description of your tool")

	# add the arguments
	# examples of a positional argument
	parser.add_argument("a", type=str, help="a's Help text")

	# example of a optional argument
	parser.add_argument("-b", "--bar", type=int, help="b's Help text")
	parser.add_argument("--foo", type=str, help="foo's Help text")

	# parse the arguments
	args = parser.parse_args()

	# print the value of args
	print(args.a + str(args.bar) + args.foo)

if __name__ == '__main__':
	main()