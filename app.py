import os
import smtplib
from email.message import EmailMessage


# configurar email

EMAIL_ADDRESS = 'alessandrohn120@gmail.com'
EMAIL_PASSWORD = 'ogeielibgbukrvzs'
# essa senha de EMAIL_PASSWORD é o proprio  gmail que gera.
#criar um email

msg = EmailMessage()
msg['subject'] = 'o relatorio esta pronto '
msg['from'] = 'alessandrohn120@gmail.com'
msg['to'] = 'alessandrohn120@gmail.com'
msg.set_content('o ralatorios esta pronto segue os dados do email')

#enviar um email

with smtplib.SMTP_SSL('smtp.gmail.com',587) as smtp:
        smtp.login(EMAIL_ADDRESS,EMAIL_PASSWORD)
        smtp.send_message(msg)
