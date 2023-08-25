from django import forms


class AdvertisementForm(forms.Form):
    title = forms.CharField(max_length=64, widget=forms.TextInput(attrs={'class' : 'form-control form-control-lg'}))
    description = forms.CharField(max_length=300, widget=forms.Textarea(attrs={'class' : 'form-control form-control-lg'}))
    price = forms.DecimalField(widget=forms.NumberInput(attrs={'class' : 'form-control form-control-lg'}))
    auction = forms.BooleanField(widget=forms.CheckboxInput(attrs={'class' : 'form-check-input'}), required=False)
    image = forms.ImageField(required=False)