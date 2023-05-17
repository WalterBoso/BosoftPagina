from django.shortcuts import render
from django.template.loader import get_template
#from django.core.mail import EmailMultiAlternatives
from django.conf import settings
from email.message import EmailMessage
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import encoders

def index(request):
    return render(request, 'index.html', {})

def conocenos(request):
    return render(request, 'conocenos.html', {})

def servicios(request):
    return render(request, 'servicios.html', {})

def contacto(request):
    if request.method == "POST":
        nombre = request.POST.get('nombre')
        mail = request.POST.get('mail')
        asunto = request.POST.get('asunto')
        mensaje = request.POST.get('mensaje')

        send_mail(nombre, mail, asunto, mensaje)

    return render(request, 'contacto.html', {})

def send_mail(nombre, mail, asunto, mensaje):

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
    except IOError:
        print("Debe completar los campos")

    smtp.quit()

    """     context = {'nombre': nombre, 
               'mail': mail,
               'asunto': asunto,
               'mensaje': mensaje}
    
    template = get_template('plantilla_mail.html')
    content = template.render(context)

    email = EmailMultiAlternatives(
        asunto,
        mensaje,
        settings.EMAIL_HOST_USER,
        [mail],
    )

    email.attach_alternative(context, 'text/html')
    email.send() """
