from django import forms
from .models import Order,Subscription,Comment, Seller, Pineapple


class SellerForm(forms.ModelForm):
    class Meta:
        model = Seller
        fields = '__all__'

    def clean_address(self):
        address = self.cleaned_data['address']
        if len(address) < 10:
            raise forms.ValidationError('این فیلد باید بیشتر از ۱۰ کاراکتر باشد.')
        return address

    def clean_certificate_code(self):
        certificate_code = self.cleaned_data['certificate_code']
        if not certificate_code.isupper():
            raise forms.ValidationError('حروف گواهینامه باید حروف بزرگ باشد.')
        return certificate_code


class PineappleForm(forms.ModelForm):
    class Meta:
        model = Pineapple
        fields = '__all__'

    def clean_price_toman(self):
        price = self.cleaned_data['price_toman']
        if price < 1000:
            raise forms.ValidationError('قیمت نباید کمتر از هزار تومان باشد.')
        elif price > 1000000:
            raise forms.ValidationError('قیمت نباید از یک میلیون تومان بیشتر باشد.')
        return price


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


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = '__all__'

    def clean_text(self):
        text = self.cleaned_data['text']

        if len(text) < 10:
            raise forms.ValidationError('این فیلد باید بیشتر از ۱۰ کاراکتر باشد.')
        return text
