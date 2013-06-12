#!/usr/bin/env python

import sys

def main():
  if len(sys.argv) < 2:
		print_help()
	else:
		if sys.argv[1].lower() == '-h' or sys.argv[1].lower() == '--help':
			print_help()
		try:
			with open(sys.argv[1],'r') as inputfile:
				str = inputfile.read()
				if len(sys.argv) == 2:
					print str.encode('base64', 'strict')
				else:
					try:
						with open(sys.argv[2],'r') as outputfile:
							print 'The output file already exists. Do you want to overwrite it? [y/N]'
							decision = sys.stdin.read(1)
							if 'y' == decision.lower():
								with open(sys.argv[2],'w') as outfile:
									outfile.write(str.encode('base64','strict'))
							else:
								print str.encode('base64','strict')
					except IOError:
						with open(sys.argv[2],'w') as outfile:
							outfile.write(str.encode('base64','strict'))
		except IOError:
			print
			print 'The source file does not exist. Exiting...'

def print_help():
	print
	print "b64E.py v1"
	print "Author: Rahil Parikh"
    print
	print "usage : b64E.py [-h|--help] <inFile> [<outFile>]"
	print
	print "-h  --help\tPrints this help"
	print "<inFile>\tThe input file with base64 decoded text"
	print "<outFile>\tThe output file where you want to write encoded text. If skipped, the output will be written to STDOUT"
	print
	sys.exit(0)

if __name__ == '__main__':
	  main()
