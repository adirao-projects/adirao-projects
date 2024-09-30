import shutil
import os
import argparse
import sqlite3
import json
import pandas as pd

from datetime import datetime as dt

class db_manip:
    def __init__(self, path, database, password=""):
        self.path=path
        self.__password=password
        self.database=database
    
    def __open_db(self): #Private Function
        full_path = self.path+"/"+self.database
        
        db_ = sqlite3.connect(full_path)
        db = db_.cursor()
        db.execute('''CREATE TABLE IF NOT EXISTS blogposts 
                       (
                            post_id INTEGER PRIMARY KEY, 
                            post_name TEXT NOT NULL,
                            abstract TEXT NOT NULL, 
                            date TEXT NOT NULL,
                            published BOOL NOT NULL, 
                            subject_field TEXT NOT NULL,
                            highlighted BOOL NOT NULL 
                        )
                       ''')
        return db, db_
        
    def db_insert(self,query="", parameters=""):
        db, db_conn = self.__open_db()
        
        if query=="":
            query = str(input())
        
        try:
            if parameters=="":
                db.execute(query)
            else:
                db.execute(query, parameters)
        except Exception as e:
            print("BAD SQL")
            print(e)
            pass
        db_conn.commit()
        db_conn.close()
        
    def db_sql(self,query="", parameters=""):
        db, db_conn = self.__open_db()
        
        if query=="":
            query = str(input())
        
        try:
            if parameters=="":
                db.execute(query)
            else:
                db.execute(query, parameters)
        except Exception as e:
            print("BAD SQL")
            print(e)
            pass
        db_conn.commit()
        db_conn.close()
       
    def db_read(self,query="", parameters=""):
        db, db_conn = self.__open_db()
        try:
            if parameters=="":
                db.execute(query)
            else:
                db.execute(query, parameters)
            return db.fetchall()    
           
        except Exception as e:
            print("BAD SQL QUERY")
            print(e)
            print("Continue Code")
            pass
        
        print("HERE")
        db.close()
    
    def db_read_df(self,query="", parameters=""):
        db, db_ = self.__open_db()
        try:
            df = pd.read_sql_query(query, db_)
            print(df)
            return df
        
        except Exception as e:
            print("BAD SQL QUERY")
            print(e)
            print("Continue Code")
            pass
        
    def db_to_df(self):
        db, db_ = self.__open_db()
        
        df = pd.read_sql_query("SELECT * FROM "+self.database, db)
        #df.columns = stores.keys
        db.close()
        print(df)
        return df


def update_json(db):
    df = db.db_to_df()
    post_json = df.to_json()
    f = open('posts.js', 'w')
    f.write(f"post_json = {post_json};")
    f.close()

parser = argparse.ArgumentParser()

parser.add_argument("-n", "--name", type=str, 
                    help = "Folder name", required=True)

parser.add_argument("-i", "--id", type=str, 
                    help = "Post ID (better than name)", 
                    default=None)

parser.add_argument("-u", "--update", type=int, default=0,
                     help="Adds update date to log of file (doesn't actually\
                     update, use 'create_post' for that functionality)",
                     choices=[0,1])

parser.add_argument('-d', "--date", type=str, 
                    help="Date for update/publish", 
                    default=dt.today().strftime('%Y-%m-%d'))

args = parser.parse_args()

cdir = os.getcwd() + '/' + args.name
date = args.date
pubish = bool(args.publish)
update = bool(args.update)

def add_post(id):
    return NotImplementedError

def remove_post(id):
    return NotImplementedError

def update_post(id):
    return NotImplementedError



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