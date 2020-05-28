from django import forms

class RegisterClient(forms.Form):
        idClient = forms.CharField(required=True, label="ID DEL CLIENTE",
                                    min_length=4, max_length=8,
                                    widget=forms.TextInput(attrs={
                                        'class': 'form-control',
                                        'id': 'idProduct',
                                        'placeholder': 'EJEMPLO: 001'
                                    }))
        nameClient = forms.CharField(required=True, label="NOMBRE DEL CLIENTE",
                                      min_length=1, max_length=15,
                                      widget=forms.TextInput(attrs={
                                        'class': 'form-control',
                                        'id': 'nameProducto',
                                        'placeholder': 'EJEMPLO:EDWIN BARRERA'
                                      }))
        direcctionClient = forms.CharField(required=True, label="DIRECCION DEL CLIENTE",
                                             min_length=10, max_length=50,
                                             widget=forms.TextInput(attrs={
                                                 'class': 'form-control',
                                                 'id': 'idProduct',
                                                 'placeholder': '10 CALLE, 2 Y 3 AVENIDA'
                                             }))
        cantNit = forms.IntegerField(required=True, label="NIT DEL CLIENTE",
                                         widget=forms.TextInput(attrs={
                                             'class': 'form-control',
                                             'id': 'idProduct',
                                             'placeholder': '4565315-9'
                                         }))

