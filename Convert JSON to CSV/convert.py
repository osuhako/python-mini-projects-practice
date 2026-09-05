import json
import csv

def main():
    def load_json(filepath):
        data = json.load(filepath)
        return data

    headers = []
    columns = []
    def get_data(data):
        for key in data.keys():
            headers.append(key)
        for value in data.values():
            columns.append(value)
        return headers, columns

    def put_in_csv(header, columns):
        with open('output.csv', 'w', newline = '') as csvfile:
            fieldnames = headers
            writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

            writer.writeheader()
            for header in headers:
                for column in columns:
                    writer.writerow({header:column})
    return 'output.csv'

