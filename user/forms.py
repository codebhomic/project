from django import forms
from user.models import MyUser
from django.contrib.auth.password_validation import validate_password

class UserRegistrationForm(forms.ModelForm):
    password = forms.CharField(
        label="Password",
        validators=[validate_password],
        help_text = 'Enter the Your Password which should not be less than 8 character and must not match with your email address or name'
    )
    class Meta:
        model = MyUser
        fields = ('first_name','last_name','email','phone_number','password')
        help_texts = {
            'first_name': 'Enter the First Name followed by Middle Name',
            'last_name': 'Enter the Last Name',
            'phone_number': 'Enter the Phone Number',
            'password': 'Enter the Your Password which should not be less than 8 character and must not match with your email address or name',
        }

    def save(self, commit=True):
        user = super().save(commit=False)
        user.set_password(self.cleaned_data["password"])
        if commit:
            user.save()
        return user