from django import forms
from django.core.exceptions import ValidationError

from .models import Product

FORBIDDEN_WORDS = [
    "казино",
    "криптовалюта",
    "крипта",
    "биржа",
    "дешево",
    "бесплатно",
    "обман",
    "полиция",
    "радар",
]


class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = [
            "name",
            "description",
            "category",
            "price",
            "image",
            "is_active_publication",
        ]

    def __init__(self, *args, **kwargs):
        super(ProductForm, self).__init__(*args, **kwargs)
        self.fields["name"].widget.attrs.update(
            {"class": "form-control", "placeholder": "Укажите наименование"}
        )
        self.fields["description"].widget.attrs.update(
            {"class": "form-control", "placeholder": "Напишите описание"}
        )
        self.fields["category"].widget.attrs.update({"class": "form-control"})
        self.fields["price"].widget.attrs.update(
            {"class": "form-control", "placeholder": "Введите цену"}
        )
        self.fields["image"].widget.attrs.update(
            {"class": "form-control", "placeholder": "Загрузите изображение"}
        )
        self.fields["is_active_publication"].widget.attrs.update(
            {"class": "form-check-input"}
        )

    def clean_name(self):
        name = self.cleaned_data.get("name", "")
        if any(word in name.lower() for word in FORBIDDEN_WORDS):
            raise ValidationError(
                "Наименование продукта не может содержать запрещенные слова."
            )
        return name

    def clean_description(self):
        description = self.cleaned_data.get("description", "")
        if any(word in description.lower() for word in FORBIDDEN_WORDS):
            raise ValidationError(
                "Описание продукта не может содержать запрещенные слова."
            )
        return description

    def clean_price(self):
        price = self.cleaned_data.get("price", 0)
        if price < 0:
            raise ValidationError("Цена не может быть отрицательной.")
        return price
