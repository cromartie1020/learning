from django import forms

class LoginForm(forms.Form):
    username=forms.CharField()
    password=forms.CharField()

    def __str__(self):
        return self.username

class UserForm(forms.Form):
    username=forms.CharField(max_length=25)
    email=forms.EmailField()
    password=forms.CharField() 