from django.db.models import CharField, TextField, EmailField
from django.forms import ModelForm

from apps.models import Contact


class ContactForm(ModelForm):
    class Meta:
        model = Contact
        fields = ('name', 'email', 'message')
