from django.db import models


class Post(models.Model):
    title = models.CharField(
        max_length=150,
        verbose_name="Заголовок",
        help_text="Укажите заголовок записи.",
    )

    content = models.TextField(
        verbose_name="Содержимое", help_text="Напишите текст для записи."
    )

    image = models.ImageField(
        upload_to="images/",
        verbose_name="Превью (Изображение)",
        help_text="Загрузите изображение для записи.",
        blank=True,
    )

    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Дата создания")

    is_active_publication = models.BooleanField(
        default=True, verbose_name="Признак публикации"
    )

    views_counter = models.PositiveIntegerField(
        verbose_name="Количество просмотров", default=0
    )

    class Meta:
        verbose_name = "Запись блога"
        verbose_name_plural = "Записи блога"
        ordering = ["title", "created_at", "views_counter"]

    def __str__(self):
        return f"{self.title}{self.content}{self.created_at}{self.is_active_publication}{self.views_counter}."
