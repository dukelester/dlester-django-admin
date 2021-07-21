from django.core.mail import send_mail
from django.core.mail import EmailMultiAlternatives

send_mail("Your Subject", "This is a simple text email body.",
  "Yamil Asusta <hello@yamilasusta.com>", ["yamil@sendgrid.com"])

# or
mail = EmailMultiAlternatives(
  subject="Your Subject",
  body="This is a simple text email body.",
  from_email="Yamil Asusta <hello@yamilasusta.com>",
  to=["yamil@sendgrid.com"],
  headers={"Reply-To": "support@sendgrid.com"}
)
# Add template
mail.template_id = 'YOUR TEMPLATE ID FROM SENDGRID ADMIN'

# Replace substitutions in sendgrid template
mail.substitutions = {'%username%': 'elbuo8'}

# Attach file
with open('somefilename.pdf', 'rb') as file:
    mail.attachments = [
        ('somefilename.pdf', file.read(), 'application/pdf')
    ]

# Add categories
mail.categories = [
    'work',
    'urgent',
]

mail.attach_alternative(
    "<p>This is a simple HTML email body</p>", "text/html"
)

mail.send()