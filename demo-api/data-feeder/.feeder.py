import csv, subprocess, logging

data_list = []
with open('data.csv', 'r') as f:
    data = csv.reader(f, delimiter=',')
    for row in data:
        data_list.append(row)
new_string= ''
for row in data_list:
    logging.basicConfig(filename='data-feeder.sh', level=logging.DEBUG)
    logging.debug(f'http POST http://localhost:8081/api/entry username="{row[0]}" email="{row[1]}" birthyear={row[2]} > null')
