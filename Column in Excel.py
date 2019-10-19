import os
import argparse
import re
import pprint
import pandas as pd

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


def build_dict(in_dir,out_dir):

    column_list =[]
    unique_list =[]
    primary_key_list = []
    autoIncrement_list=[]
    nullable_list =[]
    datatype_list=[]
    table_name=''

    with open(in_dir,'r') as f:
        for line in f:
            line=line.strip().split()
            per_line=''
            column_name=''
            for line in line:
                per_line +=line
            if table_name == '':
                table_name = isTable(per_line)
            column_name=isColumn(per_line)
            if column_name is not '':
                column_list.append(column_name)
                datatype_list.append(datatype(per_line))
                unique_list.append(isUnique(per_line)) 
                nullable_list.append(isNullable(line)) 
                primary_key_list.append(isPrimaryKey(line)) 
                autoIncrement_list.append(autoIncrement(line)) 
        f.close()

    excel_dict = {
        'column':column_list,
        'datatype':datatype_list,
        'unique':unique_list,
        'nullable':nullable_list,
        'primary_key':primary_key_list,
        'autoincrement':autoIncrement_list
    }

    # pprint.pprint(excel_dict)
    final = pd.DataFrame(excel_dict)
    writer = pd.ExcelWriter(os.path.join(out_dir,'tables.xlsx'),engine='xlsxwriter')
    final.to_excel(writer, sheet_name=table_name)
    writer.save()

        
def change(args):
    in_dir=os.path.join(args.base_dir,args.change)
    out_dir=os.path.join(os.getcwd(),args.output)
    os.makedirs(out_dir,exist_ok=True)
    build_dict(in_dir,out_dir)
    # print(out_dir)
    

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

