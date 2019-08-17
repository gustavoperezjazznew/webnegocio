from django.shortcuts import render, redirect
from django.urls import reverse
from django.core.mail import EmailMessage
from .forms import ContactForm
# Create your views here.
def contact(request):
    # esto nos da los valores como otro lenjuage en consola
    # print("Tipo de peticion: {}".format(request.method))
    contact_form = ContactForm()
    if request.method == "POST":
            # devuelve los valores enviados anteriores
        contact_form = ContactForm(data=request.POST)
        if contact_form.is_valid():
            name=request.POST.get('name','')
            email=request.POST.get('email','')
            content=request.POST.get('content','')
            # se supone que todo esta bien redireccionamos 
            # reverser para saber el nombre de la plantilla
            # ahora enviamos el correo y redireccionamos 
            # email=EmailMessage(
            #     asunto,
            #     cuerpo,
            #     email_origen,
            #     email_destino,
            #     reply_to=[email]
            # ) formato a hacer para llevar el correo al destino
            #https://mailtrap.io
            email=EmailMessage(
                "La Caffettiera: Nuevo mensaje de contacto",
                "De {} <{}>\n\nEscribio:\n\n{}".format(name,email,content),
                "no-contestar@inbox.mailtrap.io",
                ["gustavoperezjazznew@gmail.com"],
                reply_to=[email]
            )
                        
            try:
                email.send()
                return redirect(reverse('contact')+"?ok")    
            except:
                # si pasa por aca es que no envio el msg 
                return redirect(reverse('contact')+"?fail")    

    return render(request, "contact/contact.html",{'form':contact_form})