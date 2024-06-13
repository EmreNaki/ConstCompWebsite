from django import forms
from .models import Message

class MessageForm(forms.ModelForm):
    class Meta:
        model = Message
        fields = ['namesurname', 'email', 'bodytext']
        labels = {
            "namesurname": "Ad & Soyad",
            "email": "Email",
            "bodytext": "Mesajınızı yazın"
        }

        widgets = {
            'namesurname' : forms.TextInput(attrs={'class': 'form-control'}),
            'email': forms.TextInput(attrs={'class': 'form-control'}),
            'bodytext': forms.Textarea(attrs={'class': 'form-control'}),
        }