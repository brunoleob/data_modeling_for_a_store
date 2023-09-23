from django.contrib import admin

from .models import Customer


@admin.register(Customer)
class CustomerAdmin(admin.ModelAdmin):
    # Personalize os campos que deseja exibir na lista de clientes
    list_display = ('customer_id', 'name', 'email')
    list_filter = ('name', 'email')  # Adicione filtros se desejar
