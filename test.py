import csv
import re

with open('fb_sub.csv') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')
    for row in csv_reader:
        matches = re.findall("[A-Z]+ INC", str(row))

with open('company.txt' , 'w') as f:
    f.write(str(matches))