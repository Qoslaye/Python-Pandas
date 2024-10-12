import pandas as pd 

data_dict = {'Name ' : ['Hassan ' , 'Ali' , 'Ahmed '],
             'Age ' : [18 , 40 , 30] ,
             'City' : ['Mogasidho' , 'Hargeysa' , 'Kismayo']}

df_from_dict = pd.DataFrame(data_dict) 

data_list_of_dict = [{'name' : 'Qoslaye' , 'age' : 19 , 'city':'New york'} ,
                     {'name' : 'Aflax' , 'age' : 27 , 'city':'Chicago'}]

df_from_list_of_dict = pd.DataFrame(data_list_of_dict)

print("DataFrame Frome the dictionary : " )
print(df_from_dict) 

print("\n DataFrame Frome list of dictionary : " )
print(df_from_list_of_dict) 
