import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

def send_email(sender_mail, sender_password, recipient_mail, subject, message):
    smtp_server = smtplib.SMTP_SSL('smtp.gmail.com', 465)
    smtp_server.login(sender_mail, sender_password)
    msg = MIMEMultipart()
    msg['From'] = sender_mail
    msg['To'] = recipient_mail
    msg['Subject'] = subject
    msg.attach(MIMEText(message, 'plain'))
    smtp_server.send_message(msg)
    smtp_server.quit()

def main():
    sender_mail = input("Enter your Gmail address: ")
    sender_password = input("Enter your Gmail password: ")
    recipients = [
        {"name": "Recipient 1", "email": "recipient1@example.com"},
        {"name": "Recipient 2", "email": "recipient2@example.com"},
        {"name": "Recipient 3", "email": "recipient3@example.com"}
    ]

    subject = input("Enter email subject: ")
    message = input("Enter email message: ")


    for recipient in recipients:
        recipient_name = recipient["name"]
        recipient_mail = recipient["email"]

        personalized_message = f"Dear {recipient_name},\n\n{message}"

        send_email(sender_mail, sender_password, recipient_mail, subject, personalized_message)
        print(f"Email sent to {recipient_mail}")

if __name__ == "__main__":
    main()