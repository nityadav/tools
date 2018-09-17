import argparse

if __name__ == '__main__':
  parser = argparse.ArgumentParser(description='Description of the script.')
  parser.add_argument('foo', help='Description of the required argument')
  parser.add_argument('-b', '--bar', dest='bar', help='Description of the optional argument')
  parser.add_argument('-f', dest='f', action='store_true', help='Description of the optional argument without a value')
  parser.add_argument('-d', dest='d', type=int, default='default_value', help='Description of the optional argument which has a default and type')
  parser.add_argument('-c', dest='c', default='alice', choices=['alice', 'bob'], help='Description of the optional argument which has choices')
  args = parser.parse_args()

  print args.foo
  print args.bar
  print args.f
  print args.d
  print args.c
