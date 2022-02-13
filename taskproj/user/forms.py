from django import forms
from .models import User


class InputForm(forms.ModelForm):
   # is_active = forms.CheckboxInput()

    class Meta:
        model = User
        fields = "__all__"

