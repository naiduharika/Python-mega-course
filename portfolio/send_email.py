import smtplib
import ssl

from config import Config


def send_email(message):
    email_config = Config()

    host = email_config.host
    port = email_config.port

    username = email_config.username
    password = email_config.password

    receiver = email_config.username
    context = ssl.create_default_context()

    with smtplib.SMTP_SSL(host, port, context=context) as server:
        server.login(username, password)
        server.sendmail(username, receiver, message)
