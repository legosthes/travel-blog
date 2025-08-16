from django.contrib.auth.models import User
from django.forms import ModelForm, TextInput, PasswordInput

class UserForm(ModelForm):
    class Meta:
        model = User
        fields = ["username","password"]
        labels = {"username":"Username","password":"Password"}
        widgets = {
            "username": TextInput(attrs={"class":"input","placeholder":"samuelchang@gmail.com"}), 
            "password": PasswordInput(attrs={"class":"input"})
        }