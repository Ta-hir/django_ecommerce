from django import forms
from .models import ShippingAdress

class ShippingForm(forms.ModelForm):
    shipping_full_name = forms.CharField(label="", widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':'fullname'}), required=True)
    shipping_email = forms.CharField(label="", widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':'email'}), required=True)
    shipping_address1 = forms.CharField(label="", widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':'address1'}), required=True)
    shipping_address2 = forms.CharField(label="", widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':'address2'}), required=False)
    shipping_city = forms.CharField(label="", widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':'city'}), required=True)
    shipping_country = forms.CharField(label="", widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':'country'}), required=True)
    shipping_state= forms.CharField(label="", widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':'state'}), required=False)
    shipping_zip = forms.CharField(label="", widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':'zipcode'}), required=False)
    
    class Meta:
        model = ShippingAdress
        fields = ['shipping_full_name', 'shipping_email', 'shipping_address1','shipping_address2','shipping_city','shipping_country','shipping_state','shipping_zip']
        exclude = ['user',]