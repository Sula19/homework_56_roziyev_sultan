from django import forms
from django.forms import widgets
from django.core.exceptions import ValidationError
from webapp.models import ProductsChoice


class Forms(forms.Form):
    name = forms.CharField(max_length=100, required=True, label='Название')
    description = forms.CharField(max_length=2000, required=True, widget=widgets.Textarea, label='Описание')
    img = forms.CharField(max_length=300, required=True, label='Фото')
    category = forms.ChoiceField(choices=ProductsChoice.choices, required=True, label='Категория')
    remainder = forms.IntegerField(min_value=0, required=True, label='Остаток')
    price = forms.DecimalField(max_digits=7, decimal_places=2, required=True, label='Стоимость')


    def clean_name(self):
        name = self.cleaned_data.get('name')
        if len(name) < 2:
            raise ValidationError('Поле name должен иметь не менее 3 символов')
        return name

    def clean_description(self):
        description = self.cleaned_data.get('description')
        if len(description) < 6:
            raise ValidationError('Поле text должен иметь не менее 3 символов')
        return description



    # class Meta:
    #     model = Products
    #     fields = ('name', 'description', 'img', 'category', 'remainder', 'price')
    #     labels = {
    #         'name': 'Name',
    #         'description': 'Description',
    #         'img': 'Img',
    #         'remainder': 'Remainder',
    #         'price': 'Price',
    #         'created_at': 'Created_at'
    #     }
