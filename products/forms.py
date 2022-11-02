from django import forms
from django import forms

class ProductForm(forms.Form):
    name = forms.CharField(
        label="Nombre",
        required=True,
        widget=forms.TextInput(
            attrs={
                "class": "product-name",
                "placeholder": "nombre del producto",
                "required": "True",
            }
        ),
    )
    ref = forms.CharField(
        label="Referencia",
        required=True,
        widget=forms.TextInput(
            attrs={
                "class": "product-ref",
                "placeholder": "ref",
                "required": "True",
            }
        ),
    )
    size = forms.CharField(
        label="Medidas",
        required=True,
        widget=forms.TextInput(
            attrs={
                "class": "product-size",
                "placeholder": "size",
                "required": "True",
            }
        ),
    )
    colors = forms.CharField(
        label="Colores",
        required=True,
        widget=forms.TextInput(
            attrs={
                "class": "product-colors",
                "placeholder": "colors",
                "required": "True",
            }
        ),
    )
    price = forms.DecimalField(
        label="Precio",
        required=True,
        widget=forms.TextInput(
            attrs={
                "class": "product-price",
                "placeholder": "price",
                "required": "True",
            }
        ),
    )
    weight = forms.DecimalField( 
        label="Peso",
        required=True,
        widget=forms.TextInput(
            attrs={
                "class": "product-weight",
                "placeholder": "weight",
                "required": "True",
            }
        ),
    )
    description = forms.CharField(
        label="Descripcion",
        required=True,
        widget=forms.Textarea(
            attrs={
                "class": "product-description",
                "placeholder": "description",
                "required": "True",
            }
        ),
    )