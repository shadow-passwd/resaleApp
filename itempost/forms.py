from django import forms
from product.models import Product

class ItemPostForm(forms.ModelForm):
    class Meta:
        model=Product
        fields=['name','owner','description','condition','category','brand','price','image']
