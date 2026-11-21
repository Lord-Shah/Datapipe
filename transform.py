from datetime import datetime
import sources
def clean_text(value):
    if value==None:
        return " "
    else:
        y=str(value)
        y.strip
        return value
def parse_date(text):
    j=["%Y-%m-%d", "%d/%m/%Y", "%d-%m-%Y"]
    for i in j:
        try:
            par=datetime.strptime(text, i)
            return par.strftime("%Y-%m-%d")
        except ValueError:
            continue
    return None
def parse_quantity(text):
    p=str(text)
    if p.isdigit()==True:
        if int(text)>0:
            return int(text)
    else:
        return None
def parse_price(text):
    try:
        u=float(text)
        return u
    except ValueError:
        return None
def clean_row(row):
    reasons=[]
    for i in row:
            a=row.get(i)
            clean_text(a)
            if i=="order_id":
                n=a.upper()
                if not n:
                    reasons.append("Missing order_id")
            if i=="product":
                v=a.title()
                if not v:
                    reasons.append("Missing product")
            if i=="date":
                f=parse_date(a)
                if f==None:
                    reasons.append("Invalid date")
            if i=="qty":
                c=parse_quantity(a)
                if c == None:
                    reasons.append("Invalid Qunatity")
            if i =="price":
                l=parse_price(a)
                if l==None:
                    reasons.append("Invalid price")
    if not reasons==[]:
        return (None, reasons)
    else:
        amount=round(c * l, 2)
        row["amount"]=amount
        return (row, [])
def make_bad_row(row, reason):
    e={}
    for i in sources.REJECTED_COLUMNS:
        if i!="store" and i!="reason":
            row[i]=row[i].clean_text()
            e.update(i, row[i])
        if i=="store":
            e.update(i, row[i])
        if i=="reason":
            e.update(i, reason)
    return e
def transform(raw_rows):
    good_rows=[]
    bad_rows=[]
    seen_ids=set()
    for i in raw_rows:
        r,b=clean_row(i)
        if b:
            q=""
            for o in b:
                q=q+o+";"    
                i["reason"]=q
            bad_rows.append(i)
        if i["order_id"] in seen_ids:
                bb="Duplicate order_id in this run"
                i["reason"]=bb
                bad_rows.append(i)
        if r:
                seen_ids.add(r["order_id"])
                good_rows.append(r)
    return good_rows, bad_rows


    

