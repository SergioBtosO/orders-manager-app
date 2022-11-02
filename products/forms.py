from django import forms
from django import forms

class ProductForm(forms.Form):
    name = forms.CharField(
        label="Producto:",
        required=False,
        widget=forms.TextInput(
            attrs={
                "class": "product-name",
                "placeholder": "nombre del producto",
                "required": "True",
            }
        ),
    )
    id = forms.CharField(
        label="id:",
        required=False,
        widget=forms.TextInput(
            attrs={
                "class": "product-id",
                "placeholder": "id",
                "required": "True",
            }
        ),
    )
