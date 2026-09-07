import json
import csv
 
filepath = 'test.json'
 
def load_json(d):
    with open(f'{d}') as json_data:
        obt_data = json.load(json_data)
    return obt_data
 
def filtered_data(d):
    data = json.loads(d)
 
    for key, value in data.items():
        output = 'output.csv'
        with open(output, 'w', newline = '') as csvfile:
                fieldnames = key
                writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
       
                writer.writeheader(key)
                writer.writerow(value)
    return output
 
def main():
    data = load_json(filepath)
    csv_file = filtered_data(data)
    return csv_file
 
'''
def filter_keys(d):
    data = json.loads(d)
 
    headers = []
 
    for key in data.items():
        headers.append(key)
        return headers
    return headers
 
def filter_values(d):
    data = json.loads(d)
 
    values = []
 
    for value in data.items():
        values.append(value)
        return values
    return values
 
def filter_data(data):
    for key in data.keys():
        headers.append(key)
    for value in data.values():
        columns.append(value)
    return headers, columns
 
 
def put_in_csv(header, columns):
    with open('output.csv', 'w', newline = '') as csvfile:
        fieldnames = header
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
 
        writer.writeheader()
        for h in header:
            for column in columns:
                writer.writerow({header:column})
'''




#======================================
#PREVIOUS CODE
#======================================


'''
import json
import csv

def load_json(filepath):
    with open(f'{filepath}') as json_data:
        d = json.load(json_data)
    return d

headers = []
columns = []
def get_data(d):
    for key in d.keys():
        headers.append(key)
    for value in d.values():
        columns.append(value)
    return headers, columns

def put_in_csv(headers, columns):
    with open('output.csv', 'w', newline = '') as csvfile:
        fieldnames = headers
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

        writer.writeheader()
        for header in headers:
            for column in columns:
                writer.writerow({header:column})

def main():
    filepath = "test.json"
    load_json(filepath)
    get_data(d)
    put_in_csv(headers, columns)

'''