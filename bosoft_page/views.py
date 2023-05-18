from django.shortcuts import render
from send_mails.views import send_mail

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

