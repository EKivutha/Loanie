from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Loan


class NewUserForm(UserCreationForm):
    email = forms.EmailField(required=True)

    class Meta:
        model = User
        fields = ("username", "email", "password1", "password2")

    def save(self, commit=True):
        user = super(NewUserForm, self).save(commit=False)
        user.email = self.cleaned_data["email"]
        if commit:
            user.save()
        return user
        
class PostForm(forms.ModelForm):
    	class Meta:
            model = Loan
            fields = [
                
                "reason",
                "gurrantor_1",
                "gurrantor_1_ID",
                "gurrantor_2",
                "gurrantor_2_ID",
            ]        