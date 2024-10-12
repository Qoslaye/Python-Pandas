import pandas as pd 

file_path = 'music.csv' 
df = pd.read_csv(file_path)

print("Dataframe from CSV :  ")
print(df)
print(pd.options.display.max_rows)

pd.options.display.max_rows = 9999 
df = pd.read_csv('music.csv')
print(df)

