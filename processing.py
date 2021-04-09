
import pandas as pd


matrix=pd.read_csv('matrix.csv')
main=pd.read_csv('main.csv')

main_addr=main['main_addr'].values.tolist()
copy_id=main['copy_id'].values.tolist()
comp_addr=matrix['comp_addr'].values.tolist()
replace_id=matrix['Property_ID'].values.tolist()

def Lower(a,b):
    c=[]
    d=[]
    for x in a :
        x=x.lower().replace(' ','')
        c.append(x)
    for y in b:
        y=y.lower().replace(' ','')
        d.append(y)
    return c,d
main_addr1,comp_addr1=Lower(main_addr,comp_addr)
def compare(a,b,c,d):
    available=[]
    index_value=[]
    for x in a:
        if x in b:
            available.append('true')
            ind=b.index(x)
            index_value.append(ind)
        else:
            available.append('false')
            index_value.append('NA')

        


