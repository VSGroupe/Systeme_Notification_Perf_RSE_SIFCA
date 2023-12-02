import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart


def sendMail(subject, bodyHtml, to_email):
    try:
        from_email = "ne-pas-repondre-visionstrategie@outlook.fr"
        password = "MailVSH2023"

        message = MIMEMultipart()
        message["Subject"] = subject
        message["From"] = from_email
        message["To"] = to_email

        # Attach HTML content
        body_html = MIMEText(bodyHtml, "html")
        message.attach(body_html)

        with smtplib.SMTP("smtp-mail.outlook.com", 587) as server:
            server.starttls()
            server.login(from_email, password)
            server.sendmail(from_email, to_email, message.as_string())
        print(f"Mail sent successfully to {to_email}")
        return True
    except Exception as e:
        print(f"An error occurred: {e}")
        return False