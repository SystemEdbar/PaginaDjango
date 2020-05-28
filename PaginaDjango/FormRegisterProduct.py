from django import forms

class FormRegisterProduct(forms.Form):
        idProduct = forms.CharField(required=True, label="ID DEL PRODUCTO",
                                    min_length=4, max_length=8,
                                    widget=forms.TextInput(attrs={
                                        'class': 'form-control',
                                        'id': 'idProduct',
                                        'placeholder': 'EJEMPLO: 001'
                                    }))
        nameProduct = forms.CharField(required=True, label="NOMBRE DEL PRODUCTO",
                                      min_length=1, max_length=15,
                                      widget=forms.TextInput(attrs={
                                        'class': 'form-control',
                                        'id': 'nameProducto',
                                        'placeholder': 'EJEMPLO: JUGO MARCA PROPIA'
                                      }))
        descriptionProduct = forms.CharField(required=True, label="DESCRIPCION DEL PRODUCTO",
                                             min_length=10, max_length=50,
                                             widget=forms.TextInput(attrs={
                                                 'class': 'form-control',
                                                 'id': 'idProduct',
                                                 'placeholder': 'EJEMPLO: AQUI SE DETALLA LAS ESPECIFICACIONES DEL '
                                                                'PRODUCTO'
                                             }))
        cantProduct = forms.IntegerField(required=True, label="CANTIDAD DEL PRODUCTO",
                                         widget=forms.TextInput(attrs={
                                             'class': 'form-control',
                                             'id': 'idProduct',
                                             'placeholder': 'EJEMPLO: 10'
                                         }))

