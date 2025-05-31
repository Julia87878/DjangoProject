from django.db import models

from users.models import CustomUser


class Category(models.Model):
    name = models.CharField(
        max_length=150,
        verbose_name="Наименование",
        help_text="Введите наименование категории",
    )
    description = models.TextField(
        blank=True, verbose_name="Описание", help_text="Введите описание категории"
    )

    class Meta:
        verbose_name = "категория"
        verbose_name_plural = "категории"
        ordering = ["name"]

    def __str__(self):
        return self.name


class Product(models.Model):
    name = models.CharField(
        max_length=150,
        verbose_name="Наименование",
        help_text="Введите наименование продукта.",
    )
    description = models.TextField(blank=True, verbose_name="Описание")
    category = models.ForeignKey(
        Category,
        on_delete=models.CASCADE,
        related_name="products",
        verbose_name="Категория",
        help_text="Введите категорию продукта.",
    )
    owner = models.ForeignKey(
        CustomUser,
        on_delete=models.CASCADE,
        related_name="products",
        verbose_name="Владелец",
        blank=True,
        null=True,
    )
    price = models.FloatField(verbose_name="Цена", help_text="Введите цену продукта.")
    image = models.ImageField(
        upload_to="images/",
        verbose_name="Изображение",
        help_text="Загрузите изображение продукта.",
        blank=True,
    )

    is_active_publication = models.BooleanField(
        default=False, verbose_name="Статус публикации"
    )
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Дата создания")
    updated_at = models.DateTimeField(
        auto_now=True, verbose_name="Дата последнего изменения"
    )

    class Meta:
        verbose_name = "продукт"
        verbose_name_plural = "продукты"
        ordering = ["name", "category", "price"]
        permissions = [
            ("can_unpublish_product", "Сan unpublish product"),
        ]

    def __str__(self):
        return f"{self.name} {self.category} {self.price}."
