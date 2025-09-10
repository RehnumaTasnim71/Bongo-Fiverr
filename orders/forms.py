
from django import forms
from .models import Order
from services.models import Review

class OrderForm(forms.ModelForm):
    class Meta:
        model = Order
        fields = []

class ReviewForm(forms.ModelForm):
    class Meta:
        model = Review
        fields = ['rating', 'comment']
        widgets = {
            'rating': forms.NumberInput(attrs={'class':'form-control','min':1,'max':5}),
            'comment': forms.Textarea(attrs={'class':'form-control', 'rows':3}),
        }

class OrderCompletionForm(forms.ModelForm):
    class Meta:
        model = Order
        fields = ["delivery_file"]

class DeliveryForm(forms.ModelForm):
    class Meta:
        model = Order
        fields = ['delivery_file']