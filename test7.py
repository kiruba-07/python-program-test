#Merge two data frames
import pandas as pd
Car_Price = {'Company': ['Toyota', 'Honda', 'BMV', 'Audi'], 'Price': [23845, 17995, 135925 , 71400]}
carpricedf=pd.DataFrame.from_dict(Car_Price)
car_Horsepower = {'Company': ['Toyota', 'Honda', 'BMV', 'Audi'], 'horsepower': [141, 80, 182 , 160]}
carhorsedf=pd.DataFrame.from_dict(car_Horsepower)
car=pd.merge(carpricedf,carhorsedf,on='Company')
print(car)

