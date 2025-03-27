import smtplib
my_email = "daveman191919@gmail.com"
my_password = "eajnrvqbekykqdvy"

connection = smtplib.SMTP("smtp.gmail.com")
connection.starttls()   # to secure the connection
connection.login(user=my_email,password=my_password)
connection.sendmail(from_addr=my_email, to_addrs="dagimmengestu5@gmail.com", msg="hi dagi man")
connection.close()