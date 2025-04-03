MyFarm Email Notifier 📧
🚀 Automated Email Notification System to remind MyFarm students about important events like Resume Day.

📌 Overview
This Python script automatically sends email notifications to MyFarm students. It reads student email addresses from a JSON file and sends customized messages using SMTP.

🛠 Technologies Used
Python

JSON (for storing student emails)

SMTP (smtplib) for sending emails

email.mime for formatting messages

📂 Project Structure
bash
Copy
Edit
📦 myfarm-email-notifier
├── 📜 students.json      # JSON file with student email addresses
├── 📜 email_sender.py    # Main Python script to send emails
├── 📜 .gitignore         # Ignore sensitive files
├── 📜 README.md          # Project documentation
└── 📜 requirements.txt   # Required Python libraries
⚙️ Setup & Installation
Clone the Repository

bash
Copy
Edit
git clone https://github.com/your-username/myfarm-email-notifier.git
cd myfarm-email-notifier
Install Required Libraries

bash
Copy
Edit
pip install -r requirements.txt
Store Your Email Credentials Securely
Instead of hardcoding credentials, use environment variables:

bash
Copy
Edit
export EMAIL_USER="your_email@example.com"
export EMAIL_PASS="your_password"
Or create a .env file and load it in Python using dotenv.

Prepare the JSON File (students.json)

json
Copy
Edit
{
   "emails": [
      "student1@example.com",
      "student2@example.com",
      "student3@example.com"
   ]
}
Run the Script

bash
Copy
Edit
python email_sender.py
🔒 Security Tips
❌ Never push sensitive data (email/passwords) to GitHub!
✅ Use environment variables instead of hardcoding credentials.
✅ Add a .gitignore file to exclude .env or credential files.

🎯 Future Improvements
✅ Use a database instead of a JSON file

✅ Add logging for sent emails

✅ Schedule emails automatically (e.g., with cron or schedule module)

🤝 Contributing
Contributions are welcome! Feel free to submit a pull request or open an issue.

