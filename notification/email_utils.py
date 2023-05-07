from sendgrid import SendGridAPIClient
from sendgrid.helpers.mail import Mail
from userManagementApi import settings

SENDGRID_API_KEY = settings.SENDGRID_API_KEY
SENDER_EMAIL = settings.SENDER_EMAIL

sg = SendGridAPIClient(SENDGRID_API_KEY)

def send_email(emails, subject, message, from_email=SENDER_EMAIL):
    """
    :param list[str] emails: list of email addresses
    :param str subject: Email subject
    :param str message: Email message to be sent to recipients
    :return: void
    """
    message = Mail(
        from_email=from_email,
        to_emails=emails,
        subject=subject,
        html_content=message
    )
    try:
        response = sg.send(message)
    except Exception as e:
        print(e)
