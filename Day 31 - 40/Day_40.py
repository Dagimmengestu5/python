# import smtplib
#
# my_email = "daveman191919@gmail.com"
# password = "ytfg klnn eznd gxky"
#
# connection = smtplib.SMTP("smtp.gmail.com")
# connection.starttls()
# connection.login(user=my_email, password=password)
# connection.sendmail(from_addr=my_email, to_addrs="dagimmengestu5@gmail.com", msg="hellow")
# connection.close

import smtplib

my_email = "daveman191919@gmail.com"
my_password ="ytfg klnn eznd gxky"  # Use app password if 2FA is on
emails = ["dagimmengestu5@gmail.com", "kumedesta@gmail.com", "yonasnegese543@gmail.com"]
# Create secure connection
connection = smtplib.SMTP("smtp.gmail.com", 587)
connection.starttls()  # Encrypt the connection
connection.login(user=my_email, password=my_password)

connection.sendmail(
    from_addr=my_email,
    to_addrs="dagimmengestu5@gmail.com",
    msg="Subject:Dear Applicant\n\n"

"Congratulations — we’re excited to inform you that you’ve been accepted into the SkillBridge Free Data Structures & Algorithms (DSA) Training!\n\n"

"This intensive program will help you:"
"✅ Build strong DSA fundamentals"
"✅ Practice real-world coding challenges"
"✅ Get guidance from experienced developers"
'✅ Earn a certificate of completion'

"👉 Important next step:"
"Please join our official Telegram group to stay updated and receive all class details:"
"🔗 https://t.me/+63CLi-pE9bwzZDQ0"

"We can’t wait to see you in class and help you sharpen your coding skills!"

"Best regards"
)
connection.quit()
#
# import smtplib
# from email.mime.text import MIMEText
# from email.mime.multipart import MIMEMultipart
#
# my_email = "daveman191919@gmail.com"
# my_password ="ytfg klnn eznd gxky"  # Use app password if 2FA is on
# recipient = ["dagimmengestu5@gmail.com", "kumedesta@gmail.com", "yonasnegese543@gmail.com"]
#
# # Compose the email
# msg = MIMEMultipart()
# msg['From'] = my_email
# msg['To'] = recipient
# msg['Subject'] = "🎉 You’re Accepted into the SkillBridge Free DSA Training!"
#
# body = """\
# Dear Applicant,
# Congratulations — we’re excited to inform you that you’ve been accepted into the SkillBridge Free Data Structures & Algorithms (DSA) Training!
#
# This intensive program will help you:
# ✅ Build strong DSA fundamentals
# ✅ Practice real-world coding challenges
# ✅ Get guidance from experienced developers
# ✅ Earn a certificate of completion
#
# 👉 Important next step:
# Please join our official Telegram group to stay updated and receive all class details:
# <a href="">Join the official Telegram group\\\\\\\\\; https://t.me/+63CLi-pE9bwzZDQ0
# We can’t wait to see you in class and help you sharpen your coding skills!
#
# Best regards
# """
#
# msg.attach(MIMEText(body, 'plain', 'utf-8'))  # Use utf-8 to support emojis and em-dash
#
# # Send the email
# with smtplib.SMTP("smtp.gmail.com", 587) as connection:
#     connection.starttls()
#     connection.login(my_email, my_password)
#     connection.sendmail(my_email, recipient, msg.as_string())
#
