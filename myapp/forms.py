from django import forms
from .models import Contact

class Myform(forms.ModelForm):
    class Meta:
        model = Contact
        fields = ('Fname', 'Lname', 'Email', 'Queries')