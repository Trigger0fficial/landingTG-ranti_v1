from django.contrib import admin
from .models import *

class FaqAdmin(admin.ModelAdmin):
    list_display = ['title']

class PriceAdmin(admin.ModelAdmin):
    list_display = ['name', 'price', 'is_done']

class SendMessageAdmin(admin.ModelAdmin):
    list_display = ['name_user', 'email']

class ReviewsAdmin(admin.ModelAdmin):
    list_display = ['id', 'user']


admin.site.register(Faq, FaqAdmin)
admin.site.register(Price, PriceAdmin)
admin.site.register(SendMessage, SendMessageAdmin)
admin.site.register(Reviews, ReviewsAdmin)
