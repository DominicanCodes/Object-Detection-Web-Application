import smtplib
import imghdr
from email.message import EmailMessage

SENDER = "andrescardenas280@gmail.com"
PASSWORD = 'avreucjhpvkjfhqa'
RECEIVER = "andrescardenas280@gmail.com"

def send_email(image_path, receiver=RECEIVER):
    print("send_email function started")
    email_message = EmailMessage()
    email_message["Subject"] = "Motion Detected"
    email_message.set_content("Here is the object detected.")

    with open(image_path, 'rb') as file:
        content = file.read()
    email_message.add_attachment(content, maintype="image", 
                                    subtype=imghdr.what(None, content))

    gmail = smtplib.SMTP("smtp.gmail.com", 587)
    gmail.ehlo()
    gmail.starttls()
    gmail.login(SENDER, PASSWORD)
    gmail.sendmail(SENDER, receiver, email_message.as_string())
    gmail.quit()
    print("Email sent!")
    print("send_email function ended")


if __name__ == "__main__":
    send_email(image_path="images/1.png")