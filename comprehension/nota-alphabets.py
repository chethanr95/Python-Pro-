#iteration through data dict:
#for (key, value) in dict.items() :

#iteation through pandasdataframe :
#for(index, row) in my_df.iterrows()

csv_file = "/Users/ChethanR/OneDrive - kyndryl/Pictures/python/Code/comprehension/nato-letter-code.csv"

import pandas
data_f= pandas.read_csv(csv_file)

#1 create dictionary of lette : code
# data_f.to_dict() doesnot give expect dictionary structure. it is a coumned dictionary
# data frame iteration syntax:
# for(index, row) in data_frame.iterrows()
# data compr syntax with data fram iteration

phenetic_dict = {row.letter : row.code for(index,row) in data_f.iterrows()}
print(phenetic_dict)

#2 generate list of codes for input word



input_word = input("Enter a word: ").upper()
#print(f"input_word: {input_word}")
#for letter in input_word :
#    print(f"-letter- {letter}")

code_list = [phenetic_dict[letter] for letter in input_word]
print(f"code_list = {code_list}")