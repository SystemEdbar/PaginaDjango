from django import forms

class RegisterUser(forms.Form):
        username = forms.CharField(required=True, label="INGRESE SU USUARIO",
                                    min_length=4, max_length=15,
                                    widget=forms.TextInput(attrs={
                                        'class': 'form-control',
                                        'id': 'username',
                                        'type': 'text',
                                        'name': 'username',
                                        'placeholder': 'Admin'
                                    }))
        email = forms.EmailField(required=True, label="INGRESE SU CORREO",
                                      min_length=4, max_length=25,
                                      widget=forms.TextInput(attrs={
                                        'class': 'form-control',
                                        'id': 'email',
                                        'type': 'email',
                                        'name': 'email',
                                        'placeholder': 'correo@ejemplo.com'
                                      }))
        password = forms.CharField(required=True, label="INGRESE SU CONTRASEÑA",
                                             min_length=4, max_length=25,
                                             widget=forms.TextInput(attrs={
                                                 'class': 'form-control',
                                                 'id': 'password',
                                                 'type': 'password',
                                                 'name': 'password',
                                                 'placeholder': 'Contraseña'
                                             }))
