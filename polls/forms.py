from django import forms
from .models import Invoice

class InvoiceForm(forms.ModelForm):
    class Meta:
        model = Invoice
        fields = ['customer_id', 'amount', 'parcel_detail', 'delivery_area', 'origin_country']

