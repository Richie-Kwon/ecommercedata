import json
import csv

# Two file paths according to your computer system
csvFilePath = r'data.csv'
jsonFilePath = r'data.json'


def convert_json(csvFilePath, jsonFilePath):

    # create a dictionary
    data = {}

    # Open a csv reader called DictReader
    with open(csvFilePath, encoding='unicode_escape') as csvf:
        csvReader = csv.DictReader(csvf)

        # Convert each row into a dictionary and add it to data
        for rows in csvReader:
            # InvoiceNo is the Primary key
            key = rows['InvoiceNo']
            data[key] = rows

    # Open a json writer, and use the json.dumps()
    # function to dump data
    with open(jsonFilePath, 'w', encoding='unicode_escape') as jsonf:
        jsonf.write(json.dumps(data, indent=4))


# Call the make_json function
def main():
    convert_json(csvFilePath, jsonFilePath)


if __name__ == "__main__":
    main()
