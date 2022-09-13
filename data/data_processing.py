import requests
import gzip
import json
import pandas as pd
import glob
import os
from datetime import datetime
import logging

logging.basicConfig(filename='logs.log', encoding='utf-8', level=logging.DEBUG)

def fetch():
    response = requests.get("https://smn.conagua.gob.mx/webservices/?method=3", verify = False)

    if response.status_code == 200:
        logging.info('The service is responding')
    else:
        logging.error('Service is down')
        return gzip.decompress(response.content)


def process():
    json_list = json.loads(fetch())
    df = pd.DataFrame(json_list)
    return df[["ides", "idmun", "temp", "prec"]]

#generating dummy data
def generating_dummy_data():
    df = process()
    df["id"] = 1
    df2 = process()
    df2["id"] = 2
    df3 = pd.concat([df, df2])
    df4 = process()
    df4["id"] = 3
    dummy_data = pd.concat([df3, df4])
    logging.info('just dummy data :X')
    return dummy_data

def get_last_records():
    dummy_data = generating_dummy_data()
    return dummy_data[dummy_data.id >= max(dummy_data['id']) -1]

def casting_data():
    data = get_last_records()
    data["ides"] = pd.to_numeric(data["ides"])
    data["idmun"] = pd.to_numeric(data["idmun"])
    data["temp"] = pd.to_numeric(data["temp"], downcast="float")
    data["prec"] = pd.to_numeric(data["prec"], downcast="float")
    
    return data

def get_data_requested():
    data = casting_data()
    table_mun_avg = data.groupby(['ides', 'idmun'], as_index=False).agg({'temp': 'mean', 'prec': 'mean'})

    list_of_files = glob.glob('data/data_municipios/*')
    latest_file = max(list_of_files, key=os.path.getctime)
    data_mun = pd.read_csv(latest_file+'/data.csv')
    data_mun = data_mun.rename(columns={"Cve_Ent": "ides", "Cve_Mun": "idmun"})

    final_data =  pd.merge(table_mun_avg,data_mun, on=['ides', 'idmun'])

    dt_string = now = datetime.now().strftime("%d%m%YT%H")

    os.makedirs('data/data_requested/current', exist_ok=True)
    os.makedirs('data/versions/', exist_ok=True)

    final_data.to_csv('data/data_requested/current/'+dt_string+'.csv', index=False)
    final_data.to_csv('data/versions/'+dt_string+'.csv', index=False)
    return final_data
    
print(get_data_requested())