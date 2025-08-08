import pandas
import smtplib
import datetime

birthdates_file="/Users/ChethanR/OneDrive - kyndryl/Pictures/python/Code/birthday-emails/birthdates.csv"

#(A) use df.to_dict(orien="records")
with open(birthdates_file) as csv_file :
    df = pandas.read_csv(csv_file)
    birthdates_list_of_dict = df.to_dict(orient = "records")
    #birthdates_dict = df.to_dict()

print(f"df = {df}")
print(f"birthdates_list_of_dict = {birthdates_list_of_dict}")

#(B) Use dict comprehension, iterate all rows.
birthdates_dict = {(row["month"], row["day"]): row["name"] for(index, row) in df.iterrows()}
print(f"birthdates_dict = {birthdates_dict}")

#object datetime object for now. i.e 
#(A)
today = datetime.datetime.now()
year = today.year
month = today.month
day = today.day
print(f"today = {year} {month} {day}")
#(B)
today_tuple = (today.month, today.day)

#check today is persons birthday
#(A)check month date in birthdates_list_of_dict
for record in birthdates_list_of_dict :
    receiver_name = record["name"]
    birth_month = record["month"]
    birth_day = record["day"]
    
    if birth_month == month and birth_day == day : 
        print(f"It is the Birthday of {receiver_name}")
    
    #send email
    #with smtplib.SMTP("smtp.gmail.com") as connection :
    #    connection.starttls()
    #    connection.login(user = "abc", password = "123")
    #    connection.sendmail(from_addr = "sender@email.com", 
    #                        to_addrs = "receiver@email.com",
    #                        msg = f"Subject: HappY Birthday\n\n Happy Birthday {receiver_name}")

#(B) check tuple in birthdates_dict
if today_tuple in birthdates_dict :
    print(f"(B) It is Birthday of {birthdates_dict[today_tuple]} ")



