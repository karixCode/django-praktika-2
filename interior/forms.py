from django import forms
from django.core.exceptions import ValidationError
from captcha.fields import CaptchaField
from .models import User, Request, Category

class RegisterForm(forms.ModelForm):
    password = forms.CharField(label='Пароль', widget=forms.PasswordInput)
    password2 = forms.CharField(label='Повтор пароля', widget=forms.PasswordInput)
    captcha = CaptchaField(label='Введите символы с картинки')

    def clean(self):
        super().clean()
        password = self.cleaned_data.get('password')
        password2 = self.cleaned_data.get('password2')
        if password and password2 and password != password2:
            raise ValidationError({'password2': 'Пароли не совпадают'})

    def save(self, commit=True):
        user = super().save(commit=False)
        user.set_password(self.cleaned_data.get('password'))
        if commit:
            user.save()
        return user

    class Meta:
        model = User
        fields = ('name', 'surname', 'patronymic','username', 'email')

class RequestForm(forms.ModelForm):
    title = forms.CharField(
        label="Название заявки",
        max_length=200,
    )

    description = forms.CharField(
        label="Описание",
        widget=forms.Textarea,
    )

    category = forms.ModelChoiceField(
        queryset=Category.objects.all(),
        widget=forms.Select,
        label="Категория",
        help_text="Выберите категорию."
    )

    design_image = forms.ImageField(
        label="Загрузить изображение",
    )

    class Meta:
        model = Request
        fields = ['title', 'description', 'category', 'design_image']