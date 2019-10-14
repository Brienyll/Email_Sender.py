import smtplib
from email.message import EmailMessage
from string import Template
from pathlib import Path

html = Template(Path('index.html').read_text())
email = EmailMessage()
email['from'] = 'Brix Pyth'
email['to'] = 'brienyll29@gmail.com'
email['subhect'] = 'You won 1,000,000 dollars!'

email.set_content(html.substitute({'name': 'Brielle'}), 'html')
with smtplib.SMTP(host='smtp.gmail.com', port=587) as smtp:
    smtp.ehlo()
    smtp.starttls()
    smtp.login('brix.python@gmail.com', 'pythonhello1010!')
    smtp.send_message(email)
    print('email sent!')
