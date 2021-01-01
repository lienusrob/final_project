from django import forms 
from .models import CartItem, Cart

class AddToCartForm (forms.ModelForm): 
    cart = forms.ModleChoiceField(query_set = Cart.objects.filter(curent = True))