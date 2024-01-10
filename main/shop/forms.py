from django import forms

from main.shop.models import Shop, Calculation


class LendingForms(forms.ModelForm):
    class Meta:
        model = Shop
        fields = '__all__'


class ContactForm(forms.Form):
    name = forms.CharField(max_length=100,
                           widget=forms.TextInput(attrs={'class': 'form-control mb-2', 'placeholder': 'Ваше имя'}))
    email = forms.EmailField(widget=forms.EmailInput(attrs={'class': 'form-control mb-2', 'placeholder': 'email'}))
    number = forms.CharField(max_length=12,
                             widget=forms.TextInput(attrs={'class': 'form-control mb-2', 'placeholder': '8-951-*--**'}))
    message = forms.CharField(
        widget=forms.Textarea(attrs={'class': 'form-control mb-2', 'placeholder': 'Дополнительная информация'}))


class CalculationForm(forms.Form):
    service = forms.ModelChoiceField(queryset=Calculation.objects.all())
    quantity = forms.IntegerField()