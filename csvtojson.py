import csv
import json

csv_file = open("citingslaveryjuly19.csv", "r")
json_file = open("citingslavery.json", "w")

citing_slavery = csv.DictReader(csv_file)

for row in citing_slavery:
    json.dump(row, json_file)
    json_file.write("\n")
