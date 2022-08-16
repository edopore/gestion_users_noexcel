from django import forms


class HardwareForm(forms.Form):
    vendorName = forms.CharField(label='Vendor Name',max_length=50)
    hardwareName = forms.CharField(label='Hardware Name',max_length=50)
