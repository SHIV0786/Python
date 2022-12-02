# reading csv data in python
#with open("weather_data.csv") as data_file:
 #   data = data_file.readlines()
#    print(data)
import csv
with open("weather_data.csv") as data_file:
    data = csv.reader(data_file)
    temperature = []
    for row in data:
        #print(row) ---- to print data
        if row[1] != "temp":
            temperature.append(int(row[1]))

    print(temperature)

    
    
    # read csv data using python pandas library
import pandas as pd
data = pd.read_csv("weather_data.csv")
temp_list = data["temp"].to_list()
print(data["temp"].max())
# get data in columns
print(data.condition)

#get data in row
print(data[data.day == "Monday"])

print(data[data.temp == data["temp"].max()])


print("==============================")
# Create a dataframe from scratch
data_dict = {
    "students":["Any",'James',"Angela"],
    "scores":[76,56,65]
}
data = pd.DataFrame(data_dict)
data.to_csv("new_cs.csv")
