from django import forms

class ClientForm(forms.Form):
    name = forms.CharField(
        label="Nombre:",
        required=True,
        widget=forms.TextInput(
            attrs={
                "class": "client-name",
                "placeholder": "Nombre del cliente",
                "required": "True",
            }
        ),
    )

    nit = forms.IntegerField(
        label="Nit:",
        required=True,
        widget=forms.TextInput(
            attrs={
                "class": "client-nit",
                "placeholder": "NIT del cliente",
                "required": "True",
            }
        ),
    )

    email = forms.CharField(
        label="Correo Electrónico:",
        required=True,
        widget=forms.TextInput(
            attrs={
                "class": "client-email",
                "placeholder": "Correo electrónico del cliente",
                "required": "True",
            }
        ),
    )

    address = forms.CharField(
        label="Dirección:",
        required=True,
        widget=forms.TextInput(
            attrs={
                "class": "client-address",
                "placeholder": "Dirección del cliente",
                "required": "True",
            }
        ),
    )

    phone = forms.IntegerField(
        label="Telefono:",
        required=True,
        widget=forms.TextInput(
            attrs={
                "class": "client-phone",
                "placeholder": "Telefono del cliente",
                "required": "True",
            }
        ),
    )
