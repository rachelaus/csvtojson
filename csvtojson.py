from csv import DictReader
import json
csvfile = open("citingslaveryjuly19.csv", "r")
output = {}
processed_data = DictReader(csvfile)
for row in processed_data:
    output[row['cap_id']] = row
    row.pop('cap_id')

csvfile.close()
jsonfile = open("citingslavery.json", "w")
json.dump(output, jsonfile, indent=2)
jsonfile.close()
