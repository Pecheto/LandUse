

#Lets look at imports, exports, GHGE and land use. 

import pandas as pd
import numpy as np

##Read data


#Land use and carbon emissions(per l or kg) 
landc = pd.read_csv("landuse.csv")
landc["Land Use (m2)"] = landc["Land Use (m2)"] * 1000 #change of units to m^2/kilotons.
#this ^ might be a integer at the minute! No worries.




#Transactions (filter for UK)
dt = pd.read_csv("FoodBalanceSheets_E_All_Data_try2.csv",encoding='latin1')

read= dt.groupby(['Item']).size().reset_index(name='count')
print(read)
read.to_csv('read.csv')

"""
dt = dt.loc[(dt['Area'] == 'United Kingdom')&(dt['Unit'] == '1000 tonnes')]




###Filter data 
#Need to clean data into different categories, make categories match 

dt.loc[dt["Item"] == "Tomatoes and products", "Item"] = "Tomatoes"#1
dt.loc[dt["Item"] == "Roots, Other", "Item"] = "Root Vegetables"#2
dt.loc[dt["Item"] == "Vegetables", "Item"] = "Other Vegetables"#3
dt.loc[dt["Item"] == "Citrus, Other", "Item"] = "Citrus Fruit"#4
dt.loc[dt["Item"] == "Apples and products", "Item"] = "Apples"#5
dt.loc[dt["Item"] == "Grape fruit and products", "Item"] = "Barries and Grapes"#6
dt.loc[dt["Item"] == "Oranges, Mandarines","Item"] = "Other Fruit"   #7
dt.loc[dt["Item"] == "Pineapples and products", "Item"] = "Other Fruit"#7
dt.loc[dt["Item"] == "Milk - Excluding Butter", "Item"] = "Milk"#8
dt.loc[dt["Item"] == "Palm Oil", "Item"] = "Palm (Oil)"#9
dt.loc[dt["Item"] == "Sunflowerseed Oil", "Item"] = "Sunflower (Oil)"#10
dt.loc[dt["Item"] == "Olive Oil", "Item"] = "Olives (Oil)"#11
dt.loc[dt["Item"] == "Pulses", "Item"] = "Beans & Pulses"#12
dt.loc[dt["Item"] == "Beans", "Item"] = "Beans & Pulses"#12
dt.loc[dt["Item"] == "Tree Nuts", "Item"] = "Nuts"#13
dt.loc[dt["Item"] == "Ground Nuts (Shelled Eq)", "Item"] = "Nuts"#13
dt.loc[dt["Item"] == "Pigmeat", "Item"] = "Pig Meat"#14
dt.loc[dt["Item"] == "Fish, Body Oil", "Item"] = "Fish (farmed)"#15
dt.loc[dt["Item"] == "Fish, Liver Oil", "Item"] = "Fish (farmed)"#15
dt.loc[dt["Item"] == "Fish, Seafood", "Item"] = "Fish (farmed)"#15
dt.loc[dt["Item"] == "Oats", "Item"] = "Oatmeal"#16
dt.loc[dt["Item"] == "Rice (Milled Equivalent)", "Item"] = "Rice"#17
dt.loc[dt["Item"] == "Sweet Potatoes", "Item"] = "Potatoes"#18
dt.loc[dt["Item"] == "Sugar beet", "Item"] = "Sugar (from sugar beet)"#19


#new filter on food types

dt1 = dt.loc[(dt['Item'] == 'Tomatoes')]#
dt2 = dt.loc[(dt['Item'] == 'Root Vegetables')]#
dt3 = dt.loc[(dt['Item'] == 'Other Vegetables')]#
#dt4 = dt.loc[(dt['Item'] == 'Other Vegetables')]
dt5 = dt.loc[(dt['Item'] == 'Citrus Fruit')]#
dt6 = dt.loc[(dt['Item'] == 'Apples')]#
dt7 = dt.loc[(dt['Item'] == 'Barries and Grapes')]#------------------------------
dt8 = dt.loc[(dt['Item'] == 'Other Fruit')]#
dt9 = dt.loc[(dt['Item'] == 'Milk')]#
dt10 = dt.loc[(dt['Item'] == 'Palm (Oil)')]#
dt11 = dt.loc[(dt['Item'] == 'Sunflower (Oil)')]#
dt12 = dt.loc[(dt['Item'] == 'Olives (Oil)')]#
dt13 = dt.loc[(dt['Item'] == 'Beans & Pulses')]#
dt14 = dt.loc[(dt['Item'] == 'Nuts')]#-----------------------------------
dt15 = dt.loc[(dt['Item'] == 'Pig Meat')]#
dt16 = dt.loc[(dt['Item'] == 'Fish (farmed)')]#
dt17 = dt.loc[(dt['Item'] == 'Oatmeal')]#
dt18 = dt.loc[(dt['Item'] == 'Rice')]#
dt19 = dt.loc[(dt['Item'] == 'Potatoes')]#-----------------------------------
dt20 = dt.loc[(dt['Item'] == 'Sugar (from sugar beet)')]#

result = pd.concat([dt1,dt2,dt3,dt5,dt6,dt7,dt8,dt9,dt10,dt11,dt12,dt13,dt14,dt15,\
                    dt16,dt17,dt18,dt19,dt20])

result = result.reset_index(drop=True)

#Writing data after first filter
#result.to_csv('result.csv')
land_use = []
check =[]

###Checking calculation works
#compute = [result.iloc[0,13]*landc.iloc[0,1]]
#print(compute)



for i in range(len(result)):  
    
    for j in range(len(landc)):
        
       if result.iloc[i,3] == landc.iloc[j,0]:
         # print(f'{result.iloc[i,3]} and {landc.iloc[j,0]}')
          land_use= np.append(land_use, [result.iloc[i,13]*landc.iloc[j,1]])         
          check= np.append(check, [result.iloc[i,3]])


new_check= pd.DataFrame(check)
new_land_use = pd.DataFrame(land_use)

#Checking matches
dt_ew= result.groupby(['Item']).size().reset_index(name='count')
newland_use = new_check.groupby([0]).size().reset_index(name='count')


print(dt_ew)
print("------------------------------")
print(newland_use)
print("-----------------------------------------")
print(new_land_use)
#result = pd.concat([df1, df4.reindex], axis=1, sort=False)



#Joining DataFrame
endresult=pd.concat([result, new_land_use.reindex(result.index)], axis=1)


print(endresult)



endresult.to_csv('hope.csv')
"""