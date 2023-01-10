from django.contrib import admin

from admin_panel.telebot.models import Manager, Client


class ManagerAdmin(admin.ModelAdmin):
    list_display = (
        'pk',
        'name',
        'username',
        'phone'
    )

    list_display_links = ('pk', 'name', 'phone')
    empty_value_display = '-пусто-'
    search_fields = ('name',)

    class Meta:
        verbose_name_plural = 'Менеджеры'


class ClientAdmin(admin.ModelAdmin):
    list_display = (
        'pk',
        'name',
        'phone'
    )

    list_display_links = ('pk', 'name', 'phone')
    empty_value_display = '-пусто-'
    search_fields = ('phone',)

    class Meta:
        verbose_name_plural = 'Клиенты'


admin.site.register(Manager, ManagerAdmin)
admin.site.register(Client, ClientAdmin)
admin.site.site_title = 'Управление БД'
