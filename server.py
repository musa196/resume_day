import os
import json
import smtplib

#sender email in environment variable
my_email= os.environ.get('email')
password_key= os.environ.get('pass')

# messages the students
messages = """
📢 Attention MyFarm Students!

We noticed that many of you missed Resume Day yesterday! 🌱📚 
It’s not too late—make sure you come in and catch up on the activities. 
We’re excited to get back into learning and growth, and we don’t want you to miss out!

We’re looking forward to seeing you! 😊

📆 Date: Tomorrow, April 4th, 2025
⏰ Time: 8:30 AM
"""

# Email Sender server
with smtplib.SMTP('smtp.gmail.com', 587) as server:
    server.starttls()
    server.login(user=my_email, password=password_key)

    # open students emails file
    with open("emails.json", 'r') as emails:
        student_email_data = json.load(emails)
        student_email = student_email_data['emails']

    # loop through students email and send each student a message at a time..
    for to_student_email in student_email:
        server.sendmail(from_addr=my_email,
                  to_addrs=to_student_email,
                  msg=f"Subject:Resume to MyFarm\n\n{messages}".encode("utf-8")
                  )
        print(to_student_email)
        print("Email sent successfully!..")
        server.quit()
    print("Well Done!!")