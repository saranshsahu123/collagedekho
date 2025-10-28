# colleges/forms.py
from django import forms
from .models import Review

class ReviewForm(forms.ModelForm):
    # Use RadioSelect widget for star rating styling
    rating = forms.ChoiceField(
        choices=Review.RATING_CHOICES,
        widget=forms.RadioSelect(attrs={'class': 'star-rating-input'}) # Add class for CSS
    )

    class Meta:
        model = Review
        fields = ['name', 'course', 'rating', 'feedback']
        widgets = {
            'feedback': forms.Textarea(attrs={'rows': 4}), # Make feedback box bigger
        }
        labels = {
            'name': 'Your Name',
            'course': 'Your Course (Optional)',
            'rating': 'Overall Website Rating',
            'feedback': 'Your Feedback',
        }