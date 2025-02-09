#Clean the datset and update the file
import pandas as pd
df=pd.read_csv("C:/Users/DELL/Downloads/rainfall prediction.csv",na_values={
"pressure":["?","n.a"],
"maxtemp":["?","n.a"],
"cloud":["?","n.a"],
"humidity":["?","n.a"]})
print(df)