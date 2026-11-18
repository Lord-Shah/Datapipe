import csv 
def read_csv_source(source):
    rows=[]
    with open(source["path"], newline="", encoding="utf-8") as file:
        data=csv.DictReader(file)
        for i in data:
            i["store"]=source["store"]
            rows.append(i)
    return rows
