# Working with the CSV File

# Opening File
# with open('we_da.csv') as df:
# 	df = df.readlines()
# 	print(df)

# Using CSV Reader
import csv
with open('we_da.csv') as df:
	data = csv.reader(df)
	temp = []
	print(data)
	for r in data:
		if r[1] != 'temp':
			temp.append(int(r[1]))
	print(temp)
