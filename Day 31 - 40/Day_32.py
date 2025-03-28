############## Email send
import smtplib
import datetime as dt
import random
import pandas

my_email = "daveman191919@gmail.com"
my_password = "eajnrvqbekykqdvy"
now = dt.datetime.now()
weak = now.weekday()
# if weak == 3:
#     with open("files/quotes.txt")as file:
#         all_file = file.readlines()
#         quote = random.choice(all_file)
#     print(quote)
    # with smtplib.SMTP("smtp.gmail.com")as connection:
    #     connection.starttls()
    #     connection.login(user="daveman191919@gmail.com",password="eajnrvqbekykqdvy")
    #     connection.sendmail(from_addr="daveman191919@gmail.com",
    #                         to_addrs="dagimmengestu5@gmail.com",
    #                         msg=f"Subject:It's the day of the week\n\n{quote}")


today_tuple = (now.month, now.day)
data = pandas.read_csv("files/birhday.csv")
birthday_dic = {(data_row["month"],data_row["day"]): data_row for (index, data_row) in data.iterrows()}
if today_tuple in birthday_dic:
    birthday_person = birthday_dic[today_tuple]
    file_path = f"files/letter_{random.randint(1,3)}.txt"
    with open(file_path) as letter_file:
        letter = letter_file.read()
        letter = letter.replace("[NAME]", birthday_person["name"])
    with smtplib.SMTP("smtp.outlook.com", )as connection:
        connection.starttls()
        connection.login(user=my_email,password=my_password)
        connection.sendmail(from_addr=my_email,
                            to_addrs="dagimmengestu5@gmail.com",
                            msg=f"Subject:Happy Birthday\n\n{letter}")
    # connection.close()
# import smtplib
# my_email = "daveman191919@gmail.com"
# my_password = "eajnrvqbekykqdvy"
#
# connection = smtplib.SMTP("smtp.gmail.com")
# connection.starttls()   # to secure the connection
# connection.login(user=my_email,password=my_password)
# connection.sendmail(from_addr=my_email,
#                     to_addrs="dagimmengestu5@gmail.com",
#                     msg="subject:Hellow\n\nhi dagi man how wes you day")
# connection.close()




