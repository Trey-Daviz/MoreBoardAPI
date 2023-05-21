import ssl
from email.mime.text import MIMEText
from email_handler.modules.dotenv import load_dotenv
import os
import smtplib
import json
from email_handler.python_files.helper_functions import generate_return
from email_handler.python_files.decorators import database_connect


load_dotenv()
password = os.getenv("EMAIL_PASSWORD")
context = ssl.create_default_context()


def send_email_main(body):
    return EmailUser(body["email_to"], body["email_subject"], body["email_body"])


def send_email(email, message):
    with smtplib.SMTP_SSL("smtp.gmail.com", 465, context=context) as server:
        server.login(os.getenv("MOREBOARD_EMAIL"), os.getenv("EMAIL_PASSWORD"))
        server.sendmail(os.getenv("MOREBOARD_EMAIL"), email, message.as_string())
        print("Email sent")


@database_connect
def EmailUser(db, email_to, email_subject, email_body):
    try:
        emails = []
        for user in email_to:
            sql = "SELECT email FROM user WHERE user_id = '%s'" % user
            db.execute(sql)
            email = db.fetchall()

            if email:
                email = email[0]["email"]
                emails.append(email)
            else:
                raise ValueError("That user id is invalid")

        message = MIMEText(email_body)
        message['Subject'] = email_subject
        message['From'] = os.getenv("MOREBOARD_EMAIL")
        message['To'] = ", ".join(emails)
        try:
            send_email(emails, message)
            return generate_return(200, "Email Sent")
        except Exception as e:
            raise e
    except ValueError as v:
        return generate_return(404, str(v))
    except Exception as e:
        return generate_return(500, str(e))
