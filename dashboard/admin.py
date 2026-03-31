from django.contrib import admin
from .models import Dashboard, Card, Order, ChartData


@admin.register(Dashboard)
class DashboardAdmin(admin.ModelAdmin):
    list_display = ('title', 'created_at', 'updated_at')
    search_fields = ('title',)


@admin.register(Card)
class CardAdmin(admin.ModelAdmin):
    list_display = ('title', 'dashboard', 'card_type', 'value', 'position')
    list_filter = ('card_type', 'dashboard')
    search_fields = ('title',)


@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ('order_id', 'customer_name', 'amount', 'status', 'created_at')
    list_filter = ('status', 'created_at')
    search_fields = ('order_id', 'customer_name')


@admin.register(ChartData)
class ChartDataAdmin(admin.ModelAdmin):
    list_display = ('month', 'dashboard', 'series_a', 'series_b', 'series_c', 'position')
    list_filter = ('dashboard',)
    search_fields = ('month',)
