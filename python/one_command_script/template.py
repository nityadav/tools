# Author: Nitin
# Usage example: python template.py start foo -o 42
# Tested with python 3.4

import argparse

def start():
	print("Inside start function")

def stop():
	print("Inside stop function")

def main():
	# create the parser
	parser = argparse.ArgumentParser(description="This is some description of your tool")

	# add the arguments
	# passing an action to your program
	parser.add_argument("whattodo", choices=["start", "stop"], help="help text")

	# passing some required data to your program.
	parser.add_argument("reqd_datum", type=str, help="help text")

	# passing some optional data to your program
	parser.add_argument("-o", "--opt_data", type=int, help="help text")

	# parse the arguments
	args = parser.parse_args()

	# print the value of the data
	print(args.reqd_datum)
	print(args.opt_data)

	# calling the action
	globals()[args.whattodo]()

if __name__ == '__main__':
	main()