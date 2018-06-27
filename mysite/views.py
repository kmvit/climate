from .forms import ContactForm
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import redirect
from django.core.mail import send_mail, BadHeaderError
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, redirect

def email(request):
    if request.method == 'GET':
        form = ContactForm()
        return redirect('/')
    else:
        form = ContactForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data['name']
            phone = form.cleaned_data['phone']
            from_email = 'info@climatim.ru'
            try:
                send_mail(name, phone, from_email, ['info@climatim.ru'])
            except BadHeaderError:
                return HttpResponse('Invalid header found.')
    return render(request, "email.html", {'form': form})
