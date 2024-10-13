from celery import shared_task
from django.core.mail import send_mail


@shared_task
def send_contact_with_me_email(user: str) -> None:
    ADMIN_EMAIL = "admin@django.py"
    subject = f'Contact with {user}'
    message = f'{user} want to use your service... or may be not... anyway contact with him at free time'
    # send_email to admin by query
    send_email.delay(ADMIN_EMAIL, subject, message)

    subject = f'Wait message from {ADMIN_EMAIL}'
    message = f'We will contact with you, {user}, just wait a little'
    # send_email to user by query
    send_email.delay(user, subject, message)


@shared_task
def send_email(address: str, subject: str, message: str) -> None:
    # send email to address
    send_mail(
        subject,
        message,
        "website_support@django.py",
        ["address"],
        fail_silently=False,
    )
