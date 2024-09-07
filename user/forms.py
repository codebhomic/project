from django import forms
from user.models import MyUser
from django.contrib.auth.password_validation import validate_password
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import authenticate
from django.contrib.auth.hashers import check_password

class UserRegistrationForm(forms.ModelForm):
    password = forms.CharField(
        label="Password",
        validators=[validate_password],
        widget=forms.PasswordInput(attrs={'placeholder': 'Password'}),
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
    
class LoginForm(forms.Form):
    email = forms.EmailField(
        label="Email Address", help_text="Enter Your Registered Email Address",
        widget=forms.EmailInput(attrs={'placeholder': 'Email Address'})
        )
    password = forms.CharField(
        label="Password", help_text="Enter Your Password",
        widget=forms.PasswordInput(attrs={'placeholder': 'Password'})
        )

    def __init__(self, *args, **kwargs):
        self.request = kwargs.pop('request', None)
        super().__init__(*args, **kwargs)

    def clean(self):
        # getting email and password from user data 
        email = self.cleaned_data.get('email')
        password = self.cleaned_data.get('password')
        if email and password:
            # checking email exist in the database or not 
            user = MyUser.objects.filter(email=email).first()
            if user is None: # if useremail is not registered than error that account does not exist
                raise forms.ValidationError("Account Does not exist.")
            if not user.is_active:
                raise forms.ValidationError("This account is inactive. please activate your account")
            pwd = user.password
            if not check_password(password,pwd):
                raise forms.ValidationError("Wrong Password, please click on forget password if you forget your password")
            self.cleaned_data['user'] = user  # Store the authenticated user
        else:
            raise forms.ValidationError("Some Error occured")
        
        return self.cleaned_data