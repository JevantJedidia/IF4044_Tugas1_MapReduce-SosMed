#!/home/bigdata/anaconda3/bin/python
import sys
import csv

dict = {}

for data in sys.stdin:
    data = data.strip().split("\t")
    socMed, date, count = data
    if (len(data) == 3):
        if socMed in dict:
            if date in dict[socMed]:
                dict[socMed][date] += int(count)
            else:
                dict[socMed][date] = int(count)
        else:
            dict[socMed] = {date: int(count)}

header = ['social_media', 'date', 'count']
# for socMed in dict:
#     for date in dict[socMed]:
#         print("%s,%s,%s" % (str(socMed).strip(), str(date).strip(), str(dict[socMed][date])))

with open('output.csv', 'w', newline='') as file:
    writer = csv.writer(file)
    writer.writerow(header)
    for socMed in dict:
        for date in dict[socMed]:
            writer.writerow([socMed.strip(), date.strip(), dict[socMed][date]])
