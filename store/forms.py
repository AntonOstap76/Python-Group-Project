# forms.py

from django import forms
from .models import Review
from .models import Product  # Import the Product model

class ReviewForm(forms.ModelForm):
    product = forms.ModelChoiceField(queryset=Product.objects.all(), empty_label="Select a product")

    rating = forms.IntegerField(
        label='Rating',
        min_value=1,
        max_value=5,
        help_text='Enter a rating between 1 and 5.'
    )

    class Meta:
        model = Review
        fields = ['product', 'rating', 'title', 'content']
