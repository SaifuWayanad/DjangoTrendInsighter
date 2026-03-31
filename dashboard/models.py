from django.db import models


class Dashboard(models.Model):
    """Dashboard model to manage dashboard configurations"""
    title = models.CharField(max_length=200, default='Dashboard')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title

    class Meta:
        ordering = ['-updated_at']


class Card(models.Model):
    """Card model for dashboard metrics"""
    CARD_TYPES = [
        ('metric', 'Metric'),
        ('chart', 'Chart'),
        ('list', 'List'),
    ]

    dashboard = models.ForeignKey(Dashboard, on_delete=models.CASCADE, related_name='cards')
    title = models.CharField(max_length=200)
    value = models.CharField(max_length=100, blank=True)
    description = models.TextField(blank=True)
    card_type = models.CharField(max_length=20, choices=CARD_TYPES, default='metric')
    icon = models.CharField(max_length=100, blank=True)
    color = models.CharField(max_length=20, default='primary')
    position = models.IntegerField(default=0)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

    class Meta:
        ordering = ['position']


class Order(models.Model):
    """Order model for sample data"""
    dashboard = models.ForeignKey(Dashboard, on_delete=models.CASCADE, related_name='orders')
    order_id = models.CharField(max_length=100, unique=True)
    customer_name = models.CharField(max_length=200)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    status = models.CharField(max_length=50, default='Pending')
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Order {self.order_id}"


class ChartData(models.Model):
    """Chart data model"""
    dashboard = models.ForeignKey(Dashboard, on_delete=models.CASCADE, related_name='chart_data')
    month = models.CharField(max_length=20)
    series_a = models.IntegerField(default=0)
    series_b = models.IntegerField(default=0)
    series_c = models.IntegerField(default=0)
    position = models.IntegerField(default=0)

    def __str__(self):
        return f"Chart Data - {self.month}"

    class Meta:
        ordering = ['position']
