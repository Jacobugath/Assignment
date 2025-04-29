import csv 
import json
import data_ingestion



gadget_data = {'category': 'Gadgets', 'total_sales': 0.00, 'total_transactions': 0, 'average_transaction_value': 0.00, 'total_quantity': 0}
tools_data = {'category': 'Tools', 'total_sales': 0, 'total_transactions': 0, 'average_transaction_value': 0, 'total_quantity': 0}


for i in data_ingestion.get_csv_data():
    for n in data_ingestion.get_json_data():
        if i.get('product_id')==n.get('product_id') and n.get('category') == "Gadgets":
            gadget_data['total_sales'] += float(i.get('sale_amount'))
            gadget_data['total_transactions'] += 1
            gadget_data['total_quantity'] += float(i.get('quantity'))
        elif i.get('product_id')==n.get('product_id') and n.get('category') == "Tools":
            tools_data['total_sales'] += float(i.get('sale_amount'))
            tools_data['total_transactions'] += 1
            tools_data['total_quantity'] += float(i.get('quantity'))
gadget_data['average_transaction_value'] = gadget_data['total_sales']/gadget_data['total_transactions']
tools_data['average_transaction_value'] = tools_data['total_sales']/tools_data['total_transactions']

#formating
tools_data['total_quantity'] = round(tools_data['total_quantity'])
tools_data['total_sales'] = "{:.2f}".format(tools_data['total_sales'])
tools_data['average_transaction_value'] = "{:.2f}".format(tools_data['average_transaction_value'])
gadget_data['total_sales'] = "{:.2f}".format(gadget_data['total_sales'])
gadget_data['average_transaction_value'] = "{:.2f}".format(gadget_data['average_transaction_value'])
gadget_data['total_quantity'] = round(gadget_data['total_quantity'])


final_data = [gadget_data, tools_data]

with open('aggregated_report.csv', 'w', newline='') as csvfile:
    fieldnames = ['category', 'total_sales', 'total_transactions', 'average_transaction_value', 'total_quantity']
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
    writer.writeheader()
    writer.writerows(final_data)