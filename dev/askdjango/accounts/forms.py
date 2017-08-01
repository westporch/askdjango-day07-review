from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm


class SignupForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        fields = UserCreationForm.Meta.fields + ('email',)


def answer_validator(value):
    if value != 6:
        raise forms.ValidationError('올바른 값을 입력해주세요.')


class LoginForm(AuthenticationForm):
    answer = forms.IntegerField(help_text='3 + 3 = ?', validators=[answer_validator])