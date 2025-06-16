from django.shortcuts import render

from server.models import *


def show_index(req):
    price = Price.objects.all()
    reviews = Reviews.objects.all()
    faq = Faq.objects.all()

    data = {
        'price': price,
        'reviews': reviews[:7],
        'faq': faq[:5]
    }

    return render(req, 'server/index.html', data)

def show_price(req):
    price = Price.objects.all()
    data = {
        'price': price,
    }
    return render(req, 'server/price.html', data)


from django.shortcuts import render, redirect
from .forms import SendMessageForm


def show_contact(req):
    success = False
    if req.method == 'POST':
        form = SendMessageForm(req.POST)
        if form.is_valid():
            form.save()
            success = True
            form = SendMessageForm()  # Очистить форму после отправки
    else:
        form = SendMessageForm()

    context = {
        'form': form,
        'success': success
    }
    return render(req, 'server/contact.html', context)

def show_faq(req):
    faq = Faq.objects.all()
    data = {
        'faq': faq
    }
    return render(req, 'server/faq.html', data)


