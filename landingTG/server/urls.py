from tkinter.font import names

from django.urls import path
from django.conf.urls.static import static
from django.conf import settings
from .views import *

urlpatterns = [
    path('', show_index, name='index'),
    path('price', show_price, name='price'),
    path('contact', show_contact, name='contact'),
    path('faq', show_faq, name='faq'),
    path('main', show_main, name='index-main')

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)