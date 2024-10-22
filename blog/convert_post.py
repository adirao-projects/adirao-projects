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

parser.add_argument('-e', "--engine", default='latexml', 
                    help="Engine used for conversion (latexml:lml, pandoc:pdc)", 
                    choices=["lml", "pdc", "htl", "m4t"])

args = parser.parse_args()

cdir = os.getcwd() + '/' + args.name
fmt = args.format
date = args.date
pubish = bool(args.publish)

if fmt == "tex":
    fmt_full = "latex"
elif fmt == "md":
    fmt_full = "markdown"    

if args.engine == "lml":
    if fmt == "tex":
        try: 
            os.system(f'latexmlc ./{args.name}/{args.name}.{fmt} --dest="./{args.name}/{args.name}.html"')
            print("Success")
            
        except Exception as e:
            print("Failure", e)
            
    elif fmt == "md":
        fmt_full = "markdown"
        
elif args.engine == "pdc":
    try: 
        os.system(f"pandoc {cdir}/{args.name}.{fmt} -f {fmt_full} -t html -s -o {cdir}/{args.name}.html -M link-citations=true --citeproc --bibliography={cdir}/{args.name}.bib --css blog.css")
        print("Success")
    
    except Exception as e:
        print("Failure", e)
        
elif args.engine == "htl":
    try: 
        os.system(f"htlatex {cdir}/{args.name}.{fmt}")
        print("Success")
    
    except Exception as e:
        print("Failure", e)
        
elif args.engine == "m4t":
    try:
        os.system(f'make4ht {cdir}/{args.name}.{fmt} "mathml"')
        print("Success")
    
    except Exception as e:
        print("Failure", e)
        
print('Press enter to close')
input()