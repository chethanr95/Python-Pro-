#dictionary comprehension Basics
import random
#dictionary from list
#syntax : new_dict = {new_key : new_val for item in list}

students = ["Anu", "Raghu", "Chandu", "Chetu"]
print(f"students = {students}")
students_score = { student : random.randint(1,100) for student in students}
print (f"students_score = {students_score}")

#dictionary from dictionary
#syntax new_dict = {new_key : new_val for(key,val) in dict.items()}

passed_students = { student : score for (student, score) in students_score.items() if score > 60}
print(f"passed_students = {passed_students}")

print("\n\n")

#ex with dict compr create dict of word char count from words list
words_list = input("Enter a sentence:\n").split()
print(f"input={words_list}")

word_count = {word : len(word) for word in words_list}
print(f"word_count={word_count}")

#ex with dict compr from dict of day- celcius create dict with farenheit
print("/n/n")
day_celcius = {
    "monday" : 25,
    "tuesday" : 29,
    "wednesday" : 20,
    "thursday" : 19,
    "friday" : 15,
    "saturady" : 9,
    "sunday" : 12
}
print(f"day_celcius = {day_celcius}")

day_farn = {day : temp * 9/5 + 32 for(day, temp) in day_celcius.items()}
print(f"day_farn = {day_farn}")