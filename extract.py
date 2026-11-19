import csv 
import requests
import sources
def read_csv_source(source):
    rows=[]
    with open(source["path"], newline="", encoding="utf-8") as file:
        data=csv.DictReader(file)
        for i in data:
            i["store"]=source["store"]
            rows.append(i)
    return rows
def fetch_api_source(source):
    res=requests.get(source["url"], timeout=sources.API_TIMEOUT_SECONDS)
    data=res.json()
    p=data["orders"]
    for i in p:
        i["store"]=source['store']
    return p
def extract_all(sources):
    all_rows=[]
    failed_sources=[]
    for i in sources:
        y=[]
        try:
            if i["type"]=="csv":
                q=read_csv_source(i)
                all_rows.extend(q)
                y.extend(q)
                print(f"{i["store"]}: {len(y)} rows read.")
            else:
                v=fetch_api_source(i)
                all_rows.extend(v)
                y.extend(v)
                print(f"{i["store"]}: {len(y)} rows read.")
        except FileNotFoundError:
            failed_sources.append(i["store"])
            print(f"{i['store']}: failed.")
    return all_rows, failed_sources
