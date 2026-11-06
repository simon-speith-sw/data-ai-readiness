"""Synthetische ETL-Qualitätsdemo; keine produktive Datenpipeline."""
import csv
from pathlib import Path
ROOT=Path(__file__).resolve().parents[1]
def read_rows(filename):
    with (ROOT/'data'/'raw'/filename).open(newline='',encoding='utf-8') as f:
        return list(csv.DictReader(f))
def assess_quality():
    orders=read_rows('erp_orders.csv')
    customers=read_rows('crm_customers.csv')
    prices=read_rows('price_list.csv')
    quality=read_rows('production_quality.csv')
    customer_ids={x['customer_id'] for x in customers}
    product_ids={x['product_id'] for x in prices}
    issues=[]
    def add(source,key,rule): issues.append(dict(source=source,record_id=key,rule=rule))
    for o in orders:
        if o['customer_id'] not in customer_ids: add('erp_orders',o['order_id'],'UNKNOWN_CUSTOMER')
        if o['product_id'] not in product_ids: add('erp_orders',o['order_id'],'UNKNOWN_PRODUCT')
    seen=set()
    for p in prices:
        key=(p['product_id'],p['valid_from'],p['valid_to'])
        if key in seen: add('price_list',p['product_id'],'OVERLAPPING_VALIDITY_REVIEW')
        seen.add(key)
        try:
            if float(p['unit_price'])<=0: add('price_list',p['product_id'],'INVALID_PRICE')
        except ValueError: add('price_list',p['product_id'],'INVALID_PRICE')
    for q in quality:
        try:
            prod=int(q['units_produced']);defects=int(q['units_defective'])
            if prod<=0 or defects<0 or defects>prod: add('production_quality',q['batch_id'],'INVALID_DEFECT_COUNT')
        except ValueError: add('production_quality',q['batch_id'],'MISSING_OR_INVALID_DEFECT_COUNT')
    return issues
def main():
    target=ROOT/'data'/'processed'/'quality_issues.csv';target.parent.mkdir(exist_ok=True,parents=True)
    issues=assess_quality()
    with target.open('w',newline='',encoding='utf-8') as f:
        writer=csv.DictWriter(f,['source','record_id','rule']);writer.writeheader();writer.writerows(issues)
    print(f'{len(issues)} Auffaelligkeiten: {target}')
if __name__=='__main__': main()
