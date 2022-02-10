
from django import forms
from .models import Customer


class InputForm(forms.ModelForm):

    class Meta:
        model = Customer
        fields = "__all__"
