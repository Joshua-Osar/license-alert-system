import yagmail
import pandas as pd

# Read the Excel file
file_path = 'filelocation'  # File path provided
df = pd.read_excel(file_path)

# Filter the rows where 'Days Left to Expire' is 14
expiring_soon = df[df['Days Left to Expire'] <= 32.00]

# Remove leading/trailing spaces from column names
df.columns = df.columns.str.strip()

def send_email(sender_email, app_password, recipient, subject, email_body):
    try:
        # Initialize the SMTP client
        yag = yagmail.SMTP(sender_email, app_password)
        
        # Send the email
        yag.send(
            to=recipient,
            subject=subject,
            contents=email_body
        )
        print(f"Email sent successfully to {recipient}")
    except Exception as e:
        print(f"Failed to send email: {str(e)}")  

# Remove leading/trailing spaces from column names
df.columns = df.columns.str.strip()

sender_email = "youremail@gmail.com"
app_password = "yourPW"
subject = "License Expiry Reminder"


# Loop through the filtered DataFrame and send emails
for index, row in expiring_soon.iterrows():
    recipient = row['email to send reminder']
    license_name = row['LICENSE NAME']
    vehicle_name = row['Vehicle Name']
    expiry_date = row['EXPIRY DATE']
    
    # Customize the email body
    email_body = f"""
    Dear recipient,

    This is a reminder that the license for {license_name} ({vehicle_name}) will expire on {expiry_date}.

    Please ensure necessary actions are taken before the expiration date.

    Regards,
    License Tracker
    """
    send_email(sender_email, app_password, recipient, subject, email_body)
