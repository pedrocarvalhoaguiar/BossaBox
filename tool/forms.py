from .models import Tool
from django import forms


class FormTool(forms.ModelForm):
    class Meta:
        model = Tool
        exclude = ()