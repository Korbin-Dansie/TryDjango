from django import forms
from .models import Product

class ProductForm(forms.ModelForm):
    title = forms.CharField(label="Your Awesome Title") # Override what comes by default
    description = forms.CharField(
        required=False, 
        widget=forms.Textarea(attrs={
            "class": "new-class-name",
            "rows": 10,
            "placeholder": "Your description"
        }))
    
    class Meta:
        model = Product
        fields = [
            'title',
            'description',
            'price'
        ]

    # clean_<attribute>
    def clean_title(self, *args, **kargs):
        title = self.cleaned_data.get("title")
        # Add validation(s) here for the title must pass all of them to pass
        # Muse contain a vowel
        print(len(title))
        if len(title) < 4:
            raise forms.ValidationError("Title must be longer than 3 characters")
        else:
            return title

        
# Used in views as an alternative way to create a form for products
class RawProductForm(forms.Form):
    title = forms.CharField(label="Your Awesome Title")
    description = forms.CharField(
        required=False, 
        widget=forms.Textarea(attrs={
            "class": "new-class-name",
            "rows": 10,
            "placeholder": "Your Other description"
        })) # Can set custom attributes here
    price = forms.DecimalField()
