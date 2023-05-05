from sendgrid import SendGridAPIClient
from userManagementApi import settings
from notification.email_utils import send_email

sg = SendGridAPIClient(settings.SENDGRID_API_KEY)
sg_default_sender = settings.SENDGRID_DEFAULT_SENDER

def send_email_task(emails, subject, message, from_email=sg_default_sender):
    """
    :param list[str] emails: list of email addresses
    :param str subject: Email subject
    :param str message: Email message to be sent to recipients
    :return: void
    """
    send_email(emails, subject, message, from_email)
