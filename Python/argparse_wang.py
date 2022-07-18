import argparse

parser = argparse.ArgumentParser()
parser.add_argument('integer', type=int, help='display an integer')
# args = parser.parse_args()

# print args.integer

# print "10 times of this integer = ", args.integer*10
# print '\n'

parser.add_argument("--square", help="display a square of a given number", type=int)
parser.add_argument("--cubic", help="display a cubic of a given number", type=int)

args = parser.parse_args()
print args.integer

if args.square:
	print "square of this arg = ", args.square**2

if args.cubic:
	print "cubic of this arg = ", args.cubic**3


