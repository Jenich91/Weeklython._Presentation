import smtplib
import ssl
import config
from email.mime.text import MIMEText


def send_email(receiver_email, code):
    res = 'Auth code successfully sent'

    message = MIMEText(f"Your auth code is: {code}")
    message['Subject'] = "Auth code"
    message['From'] = config.sender_email
    message['To'] = receiver_email

    context = ssl.create_default_context()
    with smtplib.SMTP_SSL(config.smtp_server,
                          config.port, context=context) as server:
        try:
            server.login(config.sender_email, config.pswd)
            server.sendmail(config.sender_email,
                            receiver_email, message.as_string())
        except Exception as error:
            res = error
    return res


if __name__ == '__main__':
    print(send_email("example@yandex.ru", 435934))
