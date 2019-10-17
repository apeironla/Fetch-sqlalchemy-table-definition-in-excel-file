import os
import argparse
import re

# parser = argparse.ArgumentParser()
# parser.add_argument("square",type=int,help="display square of a given number") #positional argument(must have to provide from command line while running)
# parser.add_argument("--verbose", help="verbosity turned on",action = "store_true")
# args = parser.parse_args()
# if args.verbose:
#     print ("the square of {} eqauls {}".format(args.square,args.square**2))
# else:
#     print(args.square**2)
# table_info ={
#     'table_name':'',
#     'columns':'',
#     'primary_key'='',
#     'unique'='',
#     'auto_increment':'',
#     'foreign_key':'',
#     'foreign_key_table'='',
#     'foreign-_key_column'='',
#     'not_null':'',
#     'default':'',
#     'check':''
# }
def isTable(line):
    temp = re.search(r'(\w+table=\()((\'\w+\')|(\"\w+\"))',line)
    if temp.find('\''):
        temp = temp.group(2).split('\'')
        return temp[1]
    if temp.find('\"'):
        temp = temp.group(2).split('\"')
        return temp[1]
     
def isColumn(line):
    n = re.search(r'(\w*Column\()((\'\w+\')|(\"\w+\"))',line)
    if temp.find('\''):
        temp = temp.group(2).split('\'')
        return temp[1]
    if temp.find('\"'):
        temp = temp.group(2).split('\"')
        return temp[1]

def build_dict(in_dir):
    with open(in_dir,'r') as f:
        for line in f:
            line=line.strip().split()
            per_line=''
            for line in line:
                per_line +=line
            table_name = isTable(line)

            
            

def change(args):
    in_dir=os.path.join(args.base_dir,args.change)
    out_dir=os.path.join(os.getcwd(),args.output)
    os.makedirs(out_dir,exist_ok=True)
    build_dict(in_dir)

    print(out_dir)
    

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--change", required=True, help="Provide the filename to change into Excel")
    parser.add_argument("--base_dir",default=os.path.join(os.getcwd(),'tables'))
    parser.add_argument("--output",default="Table_Excel")
    args=parser.parse_args()
    if args.change:
        change(args)

if __name__=="__main__":
    main()

