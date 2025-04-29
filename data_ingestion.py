import csv 
import json

def get_csv_data():
    file = input('Enter file path: ')

    with open(file) as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=',')
        header = next(csv_reader)

    with open('sales_data.csv') as file_obj:    
        heading = next(file_obj)     
        reader_obj = csv.reader(file_obj) 
        list = [] 
        for row in reader_obj: 
            list.append(row)

    csv_data =[]

    for i in list:
        csv_data.append(dict(zip(header, i)))   
    return csv_data

def get_json_data():
    json_file = open('product_data.json')
    json_data = json.load(json_file)
    return json_data

    