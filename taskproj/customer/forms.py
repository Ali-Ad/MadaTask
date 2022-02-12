
from django import forms
from .models import Customer ,CustomerService


class InputForm(forms.ModelForm):

    class Meta:
        model = Customer
        fields = "__all__"

class CustomerServicesForm(forms.ModelForm):

    class Meta:
        model=CustomerService
        fields = "__all__"


