#add imports for code 
import sys
import os.path
import os
import numpy as np
import pandas as pd


test=os.path.join("C:\\","Users","Evan Robertson","Documents","GitHub","Comp593-Lab2","Orders")
df=pd.read_csv("sales_data.csv")
for sdf in df['ORDER DATE']:
    list=sdf.split('/')
    sdfn=("Orders_"+list[2]+"-"+list[1]+"-"+list[0])
    test=os.path.join("C:\\","Users","Evan Robertson","Documents","GitHub","Comp593-Lab2","Orders",sdfn)
    if(os.path.isdir(test)==False):
        os.makedirs(test)
        print(sdf)

#first iteration without functions, all in main

#store desired path as command line parameter 
file_path=("./")

    #check if path is valid 
if(os.path.exists(file_path)==False):
    print("File does not exist, try again with valid file path") 
    exit()
else:
    print("Jeff")



