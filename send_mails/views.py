from django.shortcuts import render
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import encoders
from django.conf import settings
from django.template.loader import get_template
from django.contrib import messages

def send_mail(request, nombre, mail, asunto, mensaje):

    context = {'nombre': nombre, 
               'mail': mail,
               'asunto': asunto,
               'mensaje': mensaje}
    
    remitente = settings.EMAIL_HOST_USER
    destinatario = mail
    mensaje = mensaje

    email = MIMEMultipart()
    email["From"] = remitente
    email["To"] = destinatario
    email["Subject"] = asunto

    template = get_template('plantilla_mail.html')
    content = template.render(context)

    email.attach(MIMEText(content, 'html'))
    smtp = smtplib.SMTP_SSL(settings.EMAIL_HOST)
    smtp.login(remitente, settings.EMAIL_HOST_PASSWORD)
    try:
        smtp.sendmail(remitente, destinatario, email.as_string())
        messages.success(request, 'Correo enviado...')
    except IOError:
        messages.error(request, 'Error al enviar el correo...')

    smtp.quit()
