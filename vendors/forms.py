from django import forms

class VendorForm(forms.Form):
    name = forms.CharField(
        label="Nombre",
        required=True,
        widget=forms.TextInput(
            attrs={
                "class": "vendor-name",
                "placeholder": "Nombre Vendedor",
                "required": "True",
            }
        ),
    )
    document = forms.IntegerField(
        label="Documento",
        required=True,
        widget=forms.TextInput(
            attrs={
                "class": "vendor-document",
                "placeholder": "Documento Vendedor",
                "required": "True",
            }
        ),
    )
    phone = forms.IntegerField(
        label="Teléfono",
        required=True,
        widget=forms.TextInput(
            attrs={
                "class": "vendor-phone",
                "placeholder": "Teléfono Vendedor",
                "required": "True",
            }
        ),
    )
    address = forms.CharField(
        label="Dirección",
        required=True,
        widget=forms.TextInput(
            attrs={
                "class": "vendor-address",
                "placeholder": "Dirección Vendedor",
                "required": "True",
            }
        ),
    )
    email = forms.CharField(
        label="Correo Electrónico",
        required=True,
        widget=forms.TextInput(
            attrs={
                "class": "vendor-email",
                "placeholder": "Correo electrónico Vendedor",
                "required": "True",
            }
        ),
    )
