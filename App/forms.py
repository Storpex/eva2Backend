
from django import forms
from App.models import Docente
from django.forms import URLInput, TextInput

class FormDocente(forms.ModelForm):
  class Meta:
    model = Docente
    fields = '__all__'