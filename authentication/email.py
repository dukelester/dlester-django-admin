from django.core.mail import send_mail
send_mail('Subject here', 'Here is the message.', 'dukelester4@gmail.com', ['lester.dlester200@gmail.com'], fail_silently=False)