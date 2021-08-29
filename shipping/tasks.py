"""
Shipping Tasks Celery
"""
from celery import shared_task


@shared_task
def send_notification(list_email_users, text_content):
    """
    Send notification to user with sent an Order
    """
    for email in list_email_users:
        body_notification = f"Sr. {email} {text_content}"
        print('Sent notification', body_notification)