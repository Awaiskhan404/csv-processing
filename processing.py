
import pandas as pd

matrix=pd.read_csv('matrix.csv')
main=pd.read_csv('main.csv')

main_addr=main['main_addr'].values.tolist()#addr from main.csv
copy_id=main['copy_id'].values.tolist()#id from main.csv
comp_addr=matrix['comp_addr'].values.tolist()#compare addr
replace_id=matrix['Property_ID'].values.tolist()#copy id

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

def compare(a,b,c,d):
    truth=[]
    ind_vlaue=[]
    for x in a:
        if x in b:
            truth.append('true')
            ind_vlaue.append(b.index(x))
        else:
            truth.append('false')
            ind_vlaue.append('na')
    for z in ind_vlaue:
        if z!='na':
            z=int(z)
            d.append(c[z])
        else:
            d.append('na')

if __name__=='__main__':
    main_addr1,comp_addr1=Lower(main_addr,comp_addr)
    compare(comp_addr1,main_addr1,copy_id,replace_id)
