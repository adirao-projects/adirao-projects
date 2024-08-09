import shutil
import os
import argparse
from datetime import datetime as dt
parser = argparse.ArgumentParser()

parser.add_argument("-n", "--name", type=str, 
                    help = "Folder name", required=True)

parser.add_argument("-f", "--format", type=str, 
                    help = "File Input Format (tex, md)", 
                    default='md', required=True)

parser.add_argument('-d', "--date", type=str, 
                    help="Date for update/publish", 
                    default=dt.today().strftime('%Y-%m-%d'))

parser.add_argument('-p', "--publish", type=int, 
                    help="If publishing for the first time, use this option. \
                        Otherwise will just add an update tag to a file", 
                    default=0, choices=[0,1])

args = parser.parse_args()

cdir = os.getcwd() + '/' + args.name
fmt = args.format
date = args.date
pubish = bool(args.publish)


if fmt == "tex":
    fmt_full = "latex"
    print(f'latexmlc ./{args.name}/{args.name}.{fmt} --dest="./{args.name}/{args.name}.html"')
    os.system(f'latexmlc ./{args.name}/{args.name}.{fmt} --dest="./{args.name}/{args.name}.html"')
    input()
elif fmt == "md":
    fmt_full = "markdown"

try: 
	os.system(f"pandoc {cdir}/{args.name}.{fmt} -f {fmt_full} -t html -s -o {cdir}/{args.name}.html")
	print("Success")
 
except Exception as e:
    print("Failure")
    print(e)

print('Press enter to close')
input()