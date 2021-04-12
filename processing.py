#kira
import pandas as pd

global counter
counter=0
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
    global counter
    for x in a:
        if x in b:
            counter+=1
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
            d.append('NA')
    #print(truth)
    #print(ind_vlaue)

if __name__=='__main__':
    matrix=pd.read_csv('./matrix.csv')
    main=pd.read_csv('./main.csv')#first row of main.csv is changed
    matrix.pop('Property_ID')
    main_addr=main['main_addr'].values.tolist()#addr from main.csv
    copy_id=main['copy_id'].values.tolist()#id from main.csv
    comp_addr=matrix['comp_addr'].values.tolist()#compare addr
    replace_id=[]#copy id
    main_addr1,comp_addr1=Lower(main_addr,comp_addr)
    compare(comp_addr1,main_addr1,copy_id,replace_id)
    data={
        'Status':matrix['Status'].values.tolist(),
        'Close Date':matrix['Close Date'].values.tolist(),
        'Close Price':matrix['Close Price'].values.tolist(),
        'Property_ID':replace_id,
        'New Construction Type':matrix['New Construction Type'].values.tolist(),
        'MLS Number':matrix['MLS Number'].values.tolist(),
        'List Agent Full Name':matrix['List Agent Full Name'].values.tolist(),
        'List Agent MLSID':matrix['List Agent MLSID'].values.tolist(),
        'List Office Name':matrix['List Office Name'].values.tolist(),
        'Property Address':comp_addr

    }
    df=pd.DataFrame(data)
    df.to_csv('final.csv')
    print('Value matched-->',counter)
