from django import forms
from .models import Course


class CreateForm(forms.ModelForm):
    class Meta:
        model = Course
        fields = '__all__'


class UserEmailForm(forms.Form):
    user_email = forms.CharField(label='Enter your email', max_length=100)
