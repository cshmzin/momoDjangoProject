from django import forms
from user.models import Profile

class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = []