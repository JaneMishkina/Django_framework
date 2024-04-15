from django.contrib import admin
from .models import Category, Product, Client, Order


@admin.action(description="Сбросить количество в ноль")
def reset_quantity(modeladmin, request, queryset):
    queryset.update(quantity=0)


class ProductAdmin(admin.ModelAdmin):
    """Список продуктов."""
    list_display = ['name', 'category', 'quantity']
    ordering = ['category', '-quantity']
    # Сортировка таблиц базы данных с большим количеством значений может значительно замедлить выполнение запроса. Если
    # сортируются не индексированные поля, скорость также снижается. Не стоит злоупотреблять сортировкой данных!
    list_filter = ['date_added', 'price']
    search_fields = ['description']
    search_help_text = 'Поиск по полю Описание продукта (description)'
    actions = [reset_quantity]

    """Отдельный продукт."""
    # fields = ['name', 'description', 'category', 'date_added', 'rating'] #определяет порядок вывода элементов формы
    readonly_fields = ['date_added', 'rating']
    fieldsets = [
        (
            None,
            {
                'classes': ['wide'],
                'fields': ['name'],
            },
        ),
        (
            'Подробности',
            {
                'classes': ['collapse'],
                'description': 'Категория товара и его подробное описание',
                'fields': ['category', 'description'],
            },
        ),
        (
            'Бухгалтерия',
            {
                'fields': ['price', 'quantity'],
            }
        ),
        (
            'Рейтинг и прочее',
            {
                'description': 'Рейтинг сформирован автоматически на основе оценок покупателей',
                'fields': ['rating', 'date_added'],
            }
        ),
    ]


class ClientAdmin(admin.ModelAdmin):
    list_display = ['username', 'email', 'phone_number']
    ordering = ['username']
    search_fields = ['username']
    readonly_fields = ['date_added']
    fieldsets = [
        ('Данные клиента',
         {'classes': ['wide'], 'fields': ['username', 'email', 'phone_number', 'date_added']}),
    ]


class OrderAdmin(admin.ModelAdmin):
    list_display = ('client', 'total', 'date_added')
    filter_horizontal = ('products',)
    search_fields = ('client__username',)
    list_filter = ('date_added',)


admin.site.register(Category)
admin.site.register(Client, ClientAdmin)
admin.site.register(Product, ProductAdmin)
admin.site.register(Order, OrderAdmin)
