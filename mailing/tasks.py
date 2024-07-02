import pytz
from datetime import datetime
from django.conf import settings
from django.core.mail import send_mail
from django_apscheduler.jobstores import DjangoJobStore, register_events, register_job
from apscheduler.schedulers.background import BackgroundScheduler
from .models import Mailing, Attempt


def send_mailing():
    zone = pytz.timezone(settings.TIME_ZONE)
    current_datetime = datetime.now(zone)
    mailings = Mailing.objects.filter(start_datetime__lte=current_datetime, status='created')

    for mailing in mailings:
        for client in mailing.clients.all():
            try:
                send_mail(
                    subject=mailing.message.subject,
                    message=mailing.message.body,
                    from_email=settings.EMAIL_HOST_USER,
                    recipient_list=[client.email],
                    fail_silently=False,
                )
                status = 'success'
                response = 'Email sent successfully'
            except Exception as e:
                status = 'failure'
                response = str(e)

            Attempt.objects.create(
                mailing=mailing,
                status=status,
                server_response=response
            )
        mailing.status = 'completed'
        mailing.save()


def start():
    scheduler = BackgroundScheduler()
    scheduler.add_jobstore(DjangoJobStore(), "default")
    scheduler.start()

    print("Scheduler started...")
