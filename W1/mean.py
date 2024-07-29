# Working with the CSV File

# Opening File
with open('we_da.csv') as df:
	df = df.readlines()
	print(df)