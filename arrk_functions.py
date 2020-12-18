import pandas as pd
import numpy as np
import json

def reshape_info_df(info_df):
    info_df.columns = ['information','value']
    columns_list = info_df['information'].tolist()
    values = info_df['value'].tolist()
    df = pd.DataFrame(columns = columns_list) 
    rows = [values]
    for row in rows:
        df.loc[len(df)] = row
    return df

def get_demographic_info(df,address_cols):
    df.replace(np.nan, ' ', regex=True)
    df['address'] = df[address_cols].apply(lambda x: ' '.join(x.dropna().values.tolist()), axis=1)
    df['Name']= df['First name'].astype(str).str.replace('nan','').str.cat(df['Surname'], sep=" ")
    data = df[['Name','Company name','address']].T.to_dict().values()
    return data

def write_json(data,filename):
    # data needs to be in dict_values type
    json_object = json.dumps(list(data))
    with open(filename, "w") as outfile: 
        outfile.write(json_object) 

def get_details(text_list,keyword):
    filtered_text=[]
    for text in text_list:
        if keyword in text:
            filtered_text.append(text[text.find(keyword)::])
            print('Found Phrase in current Text and appended to new list')
        else:
            print('Phrase Not Present in current Text')
    return filtered_text

def get_info_from_text(text_str,text1,text2):
    value = text_str[text_str.find(text1)+len(text1):text_str.find(text2)]
    return value
    
    