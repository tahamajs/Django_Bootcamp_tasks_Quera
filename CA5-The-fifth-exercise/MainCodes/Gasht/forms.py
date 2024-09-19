
from django import forms
from .models import Order
from .models import Subscription


class SellerForm:
    pass

class PineappleForm:
    pass


class OrderForm(forms.ModelForm):
    class Meta:
        model = Order
        fields = ['pineapple', 'name', 'weight_kg']

    def clean_weight_kg(self):
        weight_kg = self.cleaned_data.get('weight_kg')
        if weight_kg > 100:
            raise forms.ValidationError('۱۰۰ کیلو آناناس میخوای چیکار؟ مشکل داری؟')
        return weight_kg


class SubscriptionForm(forms.ModelForm):
    class Meta:
        model = Subscription
        fields = ['name', 'phone_number']

    def clean_phone_number(self):
        phone_number = self.cleaned_data.get('phone_number')
        if not (phone_number.startswith('09') and len(phone_number) == 11 and phone_number.isnumeric()):
            raise forms.ValidationError('شماره تلفن اشتباه است. شماره تلفن باید ۱۱ رقم باشد و با ۰۹ شروع شود.')
        return phone_number


class CommentForm:
    pass