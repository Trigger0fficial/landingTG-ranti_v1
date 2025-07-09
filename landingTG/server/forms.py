from django import forms
from .models import SendMessage

class SendMessageForm(forms.ModelForm):
    class Meta:
        model = SendMessage
        fields = ['name_user', 'email', 'ask']
        widgets = {
            'name_user': forms.TextInput(attrs={
                'placeholder': 'Имя',
                'class': 'form-control'
            }),
            'email': forms.EmailInput(attrs={
                'placeholder': 'Электронная почта',
                'class': 'form-control'
            }),
            'ask': forms.Textarea(attrs={
                'placeholder': 'Напишите вопрос',
                'class': 'form-control',
                'rows': 4
            }),
        }