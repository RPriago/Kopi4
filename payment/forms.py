from django import forms
from .models import ShippingAddress

class ShippingForm(forms.ModelForm):
    full_name = forms.CharField(
        max_length=100,
        label="Full Name",
        widget=forms.TextInput(attrs={'placeholder': 'Enter your full name'}),
    )
    address = forms.CharField(
        widget=forms.Textarea(attrs={'placeholder': 'Enter your address', 'rows': 3}),
        label="Address",
    )
    city = forms.CharField(
        max_length=100,
        label="City",
        widget=forms.TextInput(attrs={'placeholder': 'Enter your city'}),
    )
    postal_code = forms.CharField(
        max_length=20,
        label="Postal Code",
        widget=forms.TextInput(attrs={'placeholder': 'Enter your postal code'}),
    )
    country = forms.CharField(
        max_length=50,
        label="Country",
        widget=forms.TextInput(attrs={'placeholder': 'Enter your country'}),
    )

    class Meta:
        model = ShippingAddress
        fields = ['full_name', 'address', 'city', 'postal_code', 'country']
        exclude = ['user',]
