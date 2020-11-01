import csv
sampleFile = open('data\\data1.csv')
sampleReader = csv.reader(sampleFile)
sampleData = list(sampleReader)
print sampleData
for row in sampleData:
    for col in row:
        print col,
    print
sampleFile.close()