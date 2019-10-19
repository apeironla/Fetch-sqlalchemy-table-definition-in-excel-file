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

def isUnique(line):
    temp = re.search(r'\w*(unique=)(True|False)\w*',line)
    if temp is None:
         return "False"
    else:
        return temp.group(2)


def autoIncrement(line):
    temp = re.search(r'\w*(autoincrement=)(True|False)\w*',line)
    if temp is None:
         return "False"
    else:
        return temp.group(2)


def isNullable(line):
    temp = re.search(r'\w*(nullable=)(True|False)\w*',line)
    if temp is None:
         return "False"
    else:
        return temp.group(2)


def isPrimaryKey(line):
    temp = re.search(r'\w*(primary_key=)(True|False)\w*',line)
    if temp is None:
         return "False"
    else:
        return temp.group(2)


def isTable(line):
    temp = re.search(r'(\w+table=\()((\'\w+\')|(\"\w+\"))',line)
    if temp is None:
         return '' 
    temp = temp.group(2)
    temp = temp.replace('\"','')
    temp = temp.replace('\'','')
    # print(temp)   
    return temp

     
def isColumn(line):
    temp = re.search(r'(\w*Column\()((\'\w+\')|(\"\w+\"))',line)
    if temp is None:
         return '' 
    temp = temp.group(2)
    temp = temp.replace('\"','')
    temp = temp.replace('\'','')
    return temp


def datatype(line):
    temp = re.search(r'(\w*Column\()',line)
    if temp is None:
         return '' 
    else:
        temp = line.split(',')
        return temp[1]


def build_dict(in_dir):
    with open(in_dir,'r') as f:
        for line in f:
            line=line.strip().split()
            per_line=''
            for line in line:
                per_line +=line
            # print(per_line)
            table_name = isTable(per_line)
            column_name=isColumn(per_line)
            data_type = datatype(per_line)
            is_unique = isUnique(per_line)

        
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

