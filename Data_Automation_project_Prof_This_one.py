import datetime as date
import pandas as pd
import numpy as np
import os
from xlsxwriter.utility import xl_rowcol_to_cell
import sys
import re
def sales_csv():
    true_path=('C:\\Users\\Evan Robertson\\Documents\\GitHub\\Comp593-Lab2\\sales_data.csv')
    if(len(sys.argv) ==2):
        if(sys.argv[1]==true_path):
            pass
        else:
            print("Error: Incorrect CSV File path given. Input proper path")
            exit()
    else:
        print("Error: No command Line param present")
        exit('Exiting Script')


def get_date():
    today=date.date.today().isoformat()
    return today

def create_path(today):
    initial_path=('C:\\Users\\Evan Robertson\\Documents\\GitHub\\Comp593-Lab2')
    new_path=os.path.join(initial_path,'Orders_'+today)
    os.makedirs(new_path)
    return new_path


#sales_csv()
today=get_date()
new_path=create_path(today)
df=pd.read_csv('sales_data.csv')
df.insert(7, 'TOTAL PRICE',df['ITEM QUANTITY']*df['ITEM PRICE'])
df.drop(columns=['ADDRESS','CITY','STATE','POSTAL CODE','COUNTRY'], inplace=True)
for df_id, sdf in df.groupby('ORDER ID'):


    sdf.drop(columns=['ORDER ID'],inplace=True )
    sdf.sort_values(by='ITEM NUMBER',inplace=True)

    total=sdf['TOTAL PRICE'].sum()
    gr_total=pd.DataFrame({'ITEM PRICE':['GRAND TOTAL'], 'TOTAL PRICE':[total]})
    sdf= pd.concat([sdf,gr_total])
   


    cus_name=sdf['CUSTOMER NAME'].values[0]
    cus_name=re.sub(r'\W', '',cus_name)
    file_name=('Order'+str(df_id)+'_'+cus_name+'.xlsx')
    
    

    order_path=os.path.join(new_path,file_name)
    sheet='Order#'+str(df_id)
    
    sdf.to_excel(order_path,index=False,sheet_name=str(sheet))
   

    print(order_path)

