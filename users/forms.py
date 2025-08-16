from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.forms import ModelForm, TextInput, PasswordInput
from django.core.exceptions import ValidationError

class UserForm(UserCreationForm):
    class Meta:
        model = User
        fields = ["username","password1","password2"]
        labels = {"username":"Username","password":"Password"}
        widgets = {
            "username": TextInput(attrs={"class":"input","placeholder":"samuelchang@gmail.com"}), 
            "password1": PasswordInput(attrs={"class":"input","placeholder":"Password here."}),
            "password2": PasswordInput(attrs={"class":"input"}),
        }
    def clean_username(self):
        username = self.cleaned_data['username']

        if '@' not in username:
            raise ValidationError("Username must be an email.")
        
        return username
        
 