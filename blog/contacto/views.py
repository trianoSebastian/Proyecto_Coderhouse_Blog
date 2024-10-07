from django.shortcuts import render
from django.core.mail import send_mail
import requests
from .forms import FormularioContacto

def contacto(request):
    if request.method == 'POST':
        form = FormularioContacto(request.POST)
        if form.is_valid():
            # nombre = form.cleaned_data['nombre']
            # email = form.cleaned_data['email']
            # mensaje = form.cleaned_data['mensaje']
            # send_mail('Nuevo mensaje de contacto',mensaje,email,['trianotech2024@gmail.com'],fail_silently=False)
            form.save()
            response = requests.post('https://hooks.zapier.com/hooks/catch/20094901/2maeihr/',data=form.cleaned_data)
            return render(request, 'contacto/gracias.html')
        else:
            form = FormularioContacto()
    else:
        form = FormularioContacto()
    return render(request,'contacto/contacto.html',{'form':form})