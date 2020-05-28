from django import forms

class RegisterCustommer(forms.Form):
        idCustommer = forms.CharField(required=True, label="ID DEL PROVEEDOR",
                                    min_length=4, max_length=8,
                                    widget=forms.TextInput(attrs={
                                        'class': 'form-control',
                                        'id': 'idProduct',
                                        'placeholder': 'EJEMPLO: 001'
                                    }))
        nameCustommer = forms.CharField(required=True, label="NOMBRE DEL PROVEEDOR",
                                      min_length=1, max_length=15,
                                      widget=forms.TextInput(attrs={
                                        'class': 'form-control',
                                        'id': 'nameProducto',
                                        'placeholder': 'EJEMPLO:EDWIN BARRERA'
                                      }))
        direcctionCustommer = forms.CharField(required=True, label="DIRECCION DEL PROVEEDOR",
                                             min_length=10, max_length=50,
                                             widget=forms.TextInput(attrs={
                                                 'class': 'form-control',
                                                 'id': 'idProduct',
                                                 'placeholder': '4 CALLES, 10 Y 11 AVENIDA, GUATEMALA'
                                             }))
        cantNit = forms.IntegerField(required=True, label="NIT DEL PROVEEDOR",
                                         widget=forms.TextInput(attrs={
                                             'class': 'form-control',
                                             'id': 'idProduct',
                                             'placeholder': '4565315-9'
                                         }))

