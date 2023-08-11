import datetime

from django.db import models
from django.contrib import admin
from django.utils import timezone
from django.utils.html import format_html

class Advertisement(models.Model):
    title = models.CharField('заголовок', max_length = 128)
    description = models.TextField('описание')
    price = models.DecimalField('цена', max_digits = 10, decimal_places = 2)
    auction = models.BooleanField('торг', help_text='Отметьте если торг уместен')
    created_date = models.DateTimeField(auto_now_add = True)
    updated_date = models.DateTimeField(auto_now = True)

    @admin.display(description='дата создания')
    def create_date(self):
        if self.created_date.date() == timezone.now().date():
            created_time = self.created_date.time().strftime('%H:%M:%S')
            return format_html(
                '<span style=color:green; font-weight: bolt>Сегодня в {}</span>',
                created_time
            )
        else:
            return self.created_date.strftime('%D.%M.%Y at %H:%M:%S')

    def __str__(self):
        return f'Advertisement(id={self.id}, title={self.title}, price={self.price})'

    class Meta:
        db_table = 'advetisements'