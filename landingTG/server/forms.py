from django import forms
from .models import SendMessage

class SendMessageForm(forms.ModelForm):
    class Meta:
        model = SendMessage
        fields = ['name_user', 'email', 'ask']
        widgets = {
            'name_user': forms.TextInput(attrs={
                'placeholder': 'Ваше имя',
                'class': 'form-control'
            }),
            'email': forms.EmailInput(attrs={
                'placeholder': 'Ваша электронная почта',
                'class': 'form-control'
            }),
            'ask': forms.Textarea(attrs={
                'placeholder': 'Напишите ваш вопрос',
                'class': 'form-control',
                'rows': 4
            }),
        }