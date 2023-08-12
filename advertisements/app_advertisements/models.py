import datetime

from django.db import models
from django.contrib import admin
from django.utils import timezone
from django.utils.html import format_html
from django.contrib.auth import get_user_model

User = get_user_model()

class Advertisement(models.Model):
    title = models.CharField('заголовок', max_length = 128)
    description = models.TextField('описание')
    price = models.DecimalField('цена', max_digits = 10, decimal_places = 2)
    auction = models.BooleanField('торг', help_text='Отметьте если торг уместен')
    created_date = models.DateTimeField(auto_now_add = True)
    updated_date = models.DateTimeField(auto_now = True)
    user = models.ForeignKey(User, verbose_name = 'пользователь', on_delete = models.CASCADE)
    image = models.ImageField('изображение', upload_to='advertisements/')

    @admin.display(description='дата создания')
    def create_date(self):
        if self.created_date.date() == timezone.now().date():
            created_time = self.created_date.time().strftime('%H:%M:%S')
            return format_html(
                '<span style=color:green; font-weight: bolt>Сегодня в {}</span>',
                created_time
            )
        return self.created_date.strftime('%d.%m.%Y at %H:%M:%S')

    @admin.display(description='дата обновления')
    def update_date(self):
        if self.updated_date.date() == timezone.now().date():
            updated_time = self.updated_date.time().strftime('%H:%M:%S')
            return format_html(
                '<span style=color:green; font-weight: bolt>Сегодня в {}</span>',
                updated_time
            )
        return self.updated_date.strftime('%d.%m.%Y at %H:%M:%S')

    def __str__(self):
        return f'Advertisement(id={self.id}, title={self.title}, price={self.price})'

    class Meta:
        db_table = 'advetisements'