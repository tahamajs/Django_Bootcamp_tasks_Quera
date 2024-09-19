from django import forms
from .models import Seller , Pineapple , Order , Comment , Subscription

class SellerForm(forms.ModelForm):
    class Meta:
        model = Seller
        fields = ["name","address","certificate_code"]

    def clean_address(self):
        address = self.cleaned_data.get("address")
        if len(address) < 10:
            raise forms.ValidationError("این فیلد باید بیشتر از ۱۰ کاراکتر باشد.")
        return address

    def clean_certificate_code(self):
        certificate_code = self.cleaned_data.get("certificate_code")
        if  certificate_code != certificate_code.upper():
            raise forms.ValidationError("حروف گواهینامه باید حروف بزرگ باشد.")
        return certificate_code

class PineappleForm(forms.ModelForm):
    class Meta:
        model = Pineapple
        fields = ["price_toman","seller"]

    def clean_price_toman(self):
        price = self.cleaned_data.get("price_toman")

        if price < 1000 :
            raise forms.ValidationError("قیمت نباید کمتر از هزار تومان باشد.")
        elif price > 1000000 :
            raise forms.ValidationError("قیمت نباید از یک میلیون تومان بیشتر باشد.")
        return price

class OrderForm(forms.ModelForm):
    class Meta:
        model = Order
        fields = ["pineapple","name","weight_kg"]

    def clean_weight_kg(self):
        kk = self.cleaned_data.get("weight_kg")
        if kk > 100 :
            raise forms.ValidationError("۱۰۰ کیلو آناناس میخوای چیکار؟ مشکل داری؟")
        return kk

class SubscriptionForm(forms.ModelForm):
    class Meta:
        model = Subscription
        fields = ["name","phone_number"]

    def clean_phone_number(self):
        phone_num = self.cleaned_data.get("phone_number")
        if len(phone_num) != 11 or not phone_num.startswith("09"):
            raise forms.ValidationError("شماره تلفن اشتباه است. شماره تلفن باید ۱۱ رقم باشد و با ۰۹ شروع شود.")
        return phone_num

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = [ "seller","name","text"]

    def clean_text(self):

        text = self.cleaned_data.get("text")
        if len(text) < 10:
            raise forms.ValidationError("این فیلد باید بیشتر از ۱۰ کاراکتر باشد")
        return text