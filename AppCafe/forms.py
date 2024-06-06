from django import forms

class ClienteFormulario(forms.Form):
    nombre=forms.CharField(max_length=30)
    mesa=forms.IntegerField()
    email=forms.EmailField()

class MeseroFormulario(forms.Form):
    nombre=forms.CharField(max_length=30)
    mesa=forms.IntegerField()

class CuentaFormulario(forms.Form):
    total=forms.IntegerField()
    mesa=forms.IntegerField()