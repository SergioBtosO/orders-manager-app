from django import forms
from django import forms

class ClientForm(forms.Form):
    name = forms.CharField(
        label="cliente:",
        required=False,
        widget=forms.TextInput(
            attrs={
                "class": "client-name",
                "placeholder": "nombre del cliente",
                "required": "True",
            }
        ),
    )
    id = forms.CharField(
        label="id:",
        required=False,
        widget=forms.TextInput(
            attrs={
                "class": "client-id",
                "placeholder": "id",
                "required": "True",
            }
        ),
    )
