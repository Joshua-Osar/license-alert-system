 # License Tracker
![image (3)](https://github.com/user-attachments/assets/cb198314-e23a-4465-a565-1fc096fbfec9)

This Python script automates the process of sending email reminders for licenses that are nearing expiration. It reads license data from an Excel file, filters for licenses expiring soon, and sends personalized email reminders to the appropriate recipients. A simple project, but it has surprisingly brought a lot of appreciation from the organisation i did it for.

## Features

- Reads license data from an Excel file
- Filters licenses expiring within 32 days
- Sends personalized email reminders using SMTP
- Handles errors gracefully and prints status messages

## Prerequisites

Before running this script, ensure you have the following installed:

- Python 3.x
- pandas
- yagmail

You can install the required packages using pip:

```
pip install pandas yagmail openpyxl
```

## Configuration

1. Update the `file_path` variable with the correct path to your Excel file.
2. Set your Gmail account credentials:
   - `sender_email`: Your Gmail address
   - `app_password`: Your Gmail app password (not your regular password)

**Note:** For security reasons, it's recommended to use environment variables or a configuration file to store sensitive information like email credentials.

## Usage

1. Prepare your Excel file with the following columns:
   - 'Days Left to Expire'
   - 'email to send reminder'
   - 'LICENSE NAME'
   - 'Vehicle Name'
   - 'EXPIRY DATE'
     
**Note:** these columns were in the data i worked with.

2. Run the script:

```
python license_tracker.py
```

The script will process the Excel file and send email reminders for licenses expiring within 32 days.

## Deployment on a Local Server PC

To run the script automatically at regular intervals, you can use the Windows Task Scheduler:

1. Open Task Scheduler (you can search for it in the Start menu)
2. Click on "Create Basic Task" in the Actions panel
3. Name your task (e.g., "License Tracker Email Reminder")
4. Choose how often you want the task to run (e.g., Daily)
5. Set the start time and recurrence pattern
6. Choose "Start a program" as the action
7. In the "Program/script" field, enter: `python`
8. In the "Add arguments" field, enter the full path to your script: `C:\path\to\your\license_tracker.py`
9. In the "Start in" field, enter the directory containing your script: `C:\path\to\your\script\directory`
10. Review your settings and click Finish

This will run your script automatically according to the schedule you've set.

**Note:** Ensure that the PC is turned on and logged in at the scheduled time for the task to run. Consider configuring the task to run whether the user is logged in or not, but be aware of the security implications.

## Customization

- Adjust the `expiring_soon` filter to change the number of days for the expiration warning.
- Modify the `email_body` template to customize the content of the reminder emails.

## Security Considerations

- Do not share your `app_password` or include it directly in the script if you plan to share the code.
- Consider implementing additional security measures when dealing with sensitive license information.
- When setting up scheduled tasks, be cautious about running scripts with elevated privileges.

## Contributing

Contributions to improve the script are welcome. Please feel free to submit a pull request or open an issue. I cant really give the full details of what i did, but these basics are enough to help you do something similar


