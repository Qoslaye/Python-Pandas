import pandas as pd 

# a = [7,5,9] 
# myvar = pd.Series(a , index=["p" , "q" , "r"]) 
# print(myvar)

data_list = [10,20,30,40,50] 

series_from_list = pd.Series(data_list) 

data_dict = {'a':10 , 'b':20 , 'c':30 , 'd':40, 'e':50} 
series_with_index = pd.Series(data_dict) 

print("series from list : \n" , series_from_list)
print("\n series with index : \n" , series_with_index)