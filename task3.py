import pandas as pandas_data_frame
import json

# Read Files into dataframe values
file1 = pandas_data_frame.read_excel("Book1.xlsx")

# Replace NaN with empty string to form a valid json
file1 = file1.fillna('')

# fillna - > replace Nan values with specific string ('gokul')

# Creating an json object 
# {"key" : "values"}
columns = [str(k) for k in file1.columns]
json_arr = [dict(zip(columns, row)) for row in file1.values]
records = { 'data': json_arr}

#Write data to json file
with open('data.json', 'w', encoding='utf-8') as file:
    json.dump(records, file, ensure_ascii=False, indent=4)

 
