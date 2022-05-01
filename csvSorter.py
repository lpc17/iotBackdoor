import csv

#121620

filename = "wadwad.csv"
filenam = "mirai_labels.csv"

fields = []
rows = []

ips = []

with open(filename, 'r') as csvfile:
    csvreader = csv.reader(csvfile)
    
    fields = next(csvreader)
    
    for row in csvreader:
        rows.append(row)
        
    print("Total no. of rows: %d"%(csvreader.line_num))
    
print('Field names are:' + ', '.join(field for field in fields))

count = 0
for row in rows[:121620]:
    for col in row:
        for col[1]:
            print(col)
    print('\n')

#print('\nFirst 5 rows are:\n')
#for row in rows[:5]:
#    for col in row:
#        print("%10s"%col),
#    print('\n')