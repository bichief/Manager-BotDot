from django.contrib.auth import get_user_model
from django.db import models

User = get_user_model()


class CreatedModel(models.Model):
    """Абстрактная модель. Добавляет дату создания."""
    created = models.DateTimeField(
        'Дата создания',
        auto_now_add=True
    )
    updated = models.DateTimeField(
        auto_now=True,
        verbose_name="Дата изменения")

    class Meta:
        abstract = True


class Manager(CreatedModel):
    telegram_id = models.BigIntegerField(
        help_text='Telegram ID менеджера',
        verbose_name='Telegram ID'
    )

    username = models.CharField(
        max_length=70,
        help_text='Username менеджера',
        verbose_name='Username'
    )

    name = models.CharField(
        max_length=70,
        help_text='Имя менеджера',
        verbose_name='Имя'
    )

    phone = models.CharField(
        max_length=50,
        help_text='Номер менеджера',
        verbose_name='Номер'
    )

    is_working = models.BooleanField(
        default=False,
        help_text='Состояние менеджера (работает/не работает)',
        verbose_name='Состояние'
    )

    class Meta:
        verbose_name = 'менеджера'
        verbose_name_plural = 'Менеджеры'
        ordering = ('-created',)

    def __str__(self):
        return self.username


class Client(CreatedModel):
    name = models.CharField(
        max_length=70,
        help_text='Имя клиента',
        verbose_name='Имя клиента'
    )

    phone = models.CharField(
        max_length=70,
        unique=True,
        help_text='Номер клиента',
        verbose_name='Номер клиента'
    )

    username = models.CharField(
        max_length=70,
        null=True,
        help_text='Telegram Username клиента',
        verbose_name='Username'
    )

    status = models.CharField(
        max_length=50,
        null=True,
        help_text='Статус клиента',
        verbose_name='Статус'
    )

    manager = models.ForeignKey(
        Manager,
        on_delete=models.CASCADE,
        related_name='client',
        blank=True,
        null=True,
        help_text='Ответственный менеджер',
        verbose_name='Ответственный менеджер'
    )

    information = models.CharField(
        max_length=500,
        null=True,
        help_text='Дополнительная информация о клиенте',
        verbose_name='Дополнительная информация о клиенте'
    )

    class Meta:
        verbose_name = 'клиента'
        verbose_name_plural = 'Клиенты'
        ordering = ('-created',)