from django.forms import ModelForm
from .models import Contact
from .models import Register
from django.forms import ModelForm, TextInput, Textarea,EmailInput

from django.contrib.auth.models import User




class ContactForm(ModelForm):
    class Meta:
        model = Contact 
        fields = '__all__'       


