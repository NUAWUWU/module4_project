from django.contrib import admin
from .models import Advertisement
from django.db.models.query import QuerySet

class advertisements_Admin(admin.ModelAdmin):
    list_display = ['id', 'title', 'description', 'price', 'auction', 'created_date', 'create_date', 'update_date']
    list_filter = ['created_date', 'price', 'auction']
    actions = ['make_auction_as_false', 'make_auction_as_true']
    fieldsets = (
        ('Общее', {
            'fields' : (
                'title', 'description'
            ),
                'classes' : ['collapse']

        }),
        ('Финансы', {
            'fields' : (
                'price', 'auction'
            ),
                'classes' : ['collapse']
        })
    )

    @admin.action(description='Убрать возможность торга')
    def make_auction_as_false(self, request, queryset:QuerySet):
        queryset.update(auction = False)

    @admin.action(description='Добавить возможность торга')
    def make_auction_as_true(self, request, queryset:QuerySet):
        queryset.update(auction = True)

admin.site.register(Advertisement, advertisements_Admin)