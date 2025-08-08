import csv

data_file="/Users/ChethanR/OneDrive - kyndryl/Pictures/python/Code/csv/weather_data.csv"

with open(data_file, mode="r") as data_h :
    #data_list = data_h.readlines()  #[line1_all_values\n, line2_all_values\n,..]
    #print(data_list)
    
    csv_obj = csv.reader(data_h)    #csv.reader() creates a csv data object sctructure
    print(type(csv_obj))
    temperatures = []
    for row in csv_obj :
        #print(row)
        if row[1] != "Temp" :
            #print(int(row[1]))
            temperatures.append(int(row[1]))
    print(temperatures)

print("========PANDAS=============")
import pandas

#data = pandas.read_csv(data_file, skiprows = 1)       
data = pandas.read_csv(data_file, index_col=None)       
#data = pandas.read_csv(data_file, header=None) 
print(type(data))
print(data)
print(data["Temp"])
print(type(data["Temp"]))

#Data Frames = 2D
data_dict = data.to_dict()
print(data_dict)
print(f"Day={data_dict["Day"][2]} : Temp={data_dict["Temp"][2]}")

#Data Series = 1D
row_list = data["Temp"].to_list()
print(row_list)
print(row_list[2])

#average by calculator
average_temp = sum(row_list) / len(row_list)
print(f"average_temp={average_temp}")

#average by pandas series object mean function
print(data["Temp"].mean())

print(f"Max temp={data["Temp"].max()}")


#series access via 1) square brackets as index names or 2) attributes :
#1
print("data[\"condition\"]")
print(data["Condition"])
#2
print("data.condition")
print(data.Condition)
print(len(data.Condition.to_list()))

#print the entire row matching the col condition value - with square bracket
print(data[data.Day == "Wednesday"])
print(data[data["Day"] == "Wednesday"])

#print entire row matching condition value - with attrib
print("row with max temp")
print(data[data["Temp"] == data["Temp"].max()])
print(data[data.Temp == data.Temp.max() ])

#print col value of th row matching the col valu.
print("Wednesday's Condition")
print(data[data.Day == "Wednesday"].Condition)
#or 
print(data[data["Day"] == "Wednesday"]["Condition"])
#or
print(data[data["Day"] == "Wednesday"].Condition)
#or 
wednesday = data[data.Day == "Wednesday"]
print(wednesday)
print(wednesday.Condition)
wed_temp = wednesday.Temp
print(f"wed_temp={wed_temp}")


#Create a pandas data dictionary manually from dictionalry data structure
my_data_dict = {
    "students" : ["name1", "name2", "name3"],
    "marks" : [75, 96, 80]
}

print("sample pandas data dictionary")
data_frame = pandas.DataFrame(my_data_dict)
print(data_frame)
data_frame.to_csv("created.csv")
print()