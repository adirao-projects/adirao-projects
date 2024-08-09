import shutil
import os
import argparse
import sys
import markdown
#import Algorithms
#import ComplexDataStructures

parser = argparse.ArgumentParser()
parser.add_argument("-d", "--Day", type=int, help = "Day number", default=0)
parser.add_argument("-ift", "--Input_test_file", action="store_true", help = "Adds test inputs from vim")
parser.add_argument("-if", "--Input_file", action="store_true", help = "Adds main inputs from vim")

args = parser.parse_args()

day = args.Day
try:
	shutil.copytree(os.getcwd()+'\\Day0 [TEMPLATE]',os.getcwd()+'\\Day{}'.format(day))
	print('Folder creation successful')

	os.chdir(os.getcwd() + f'/Day{args.Day}/')

	if args.Input_test_file:
		os.system(f'test_inputs.txt')

	if args.Input_file:
		os.system(f'inputs.txt')
	
except Exception as e:
	print('Failure')
	print(e)
print('press enter to close')
input()