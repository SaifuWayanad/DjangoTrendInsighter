import os
import django
from django.core.management.base import BaseCommand
from dashboard.models import Dashboard, Card, Order, ChartData
from decimal import Decimal

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'trendinsighter.settings')
django.setup()


class Command(BaseCommand):
    help = 'Populate database with sample data'

    def handle(self, *args, **options):
        # Create or get main dashboard
        dashboard, created = Dashboard.objects.get_or_create(
            title='Main Dashboard',
            defaults={'title': 'Main Dashboard'}
        )

        if created:
            self.stdout.write(self.style.SUCCESS('Created main dashboard'))
        else:
            self.stdout.write('Dashboard already exists')

        # Clear existing data
        Card.objects.filter(dashboard=dashboard).delete()
        Order.objects.filter(dashboard=dashboard).delete()
        ChartData.objects.filter(dashboard=dashboard).delete()

        # Add metric cards
        cards_data = [
            {
                'title': 'Orders',
                'value': '1,235',
                'description': 'Last 30 days',
                'card_type': 'metric',
                'icon': 'shopping-cart',
                'color': 'primary',
                'position': 0,
            },
            {
                'title': 'Revenue',
                'value': '$35,723',
                'description': '12% increase',
                'card_type': 'metric',
                'icon': 'dollar-sign',
                'color': 'success',
                'position': 1,
            },
            {
                'title': 'Average Price',
                'value': '$16.2',
                'description': 'Per item',
                'card_type': 'metric',
                'icon': 'tag',
                'color': 'info',
                'position': 2,
            },
            {
                'title': 'Growth',
                'value': '67%',
                'description': 'vs last month',
                'card_type': 'metric',
                'icon': 'chart-pie',
                'color': 'warning',
                'position': 3,
            },
        ]

        for card_data in cards_data:
            Card.objects.create(dashboard=dashboard, **card_data)

        self.stdout.write(self.style.SUCCESS(f'Created {len(cards_data)} metric cards'))

        # Add sample orders
        orders_data = [
            {
                'order_id': '#ORD-001',
                'customer_name': 'John Smith',
                'amount': Decimal('250.00'),
                'status': 'Completed',
            },
            {
                'order_id': '#ORD-002',
                'customer_name': 'Sarah Johnson',
                'amount': Decimal('320.50'),
                'status': 'Completed',
            },
            {
                'order_id': '#ORD-003',
                'customer_name': 'Michael Brown',
                'amount': Decimal('189.99'),
                'status': 'Pending',
            },
            {
                'order_id': '#ORD-004',
                'customer_name': 'Emily Davis',
                'amount': Decimal('450.00'),
                'status': 'Completed',
            },
            {
                'order_id': '#ORD-005',
                'customer_name': 'David Wilson',
                'amount': Decimal('275.75'),
                'status': 'Pending',
            },
        ]

        for order_data in orders_data:
            Order.objects.create(dashboard=dashboard, **order_data)

        self.stdout.write(self.style.SUCCESS(f'Created {len(orders_data)} sample orders'))

        # Add chart data
        chart_data_list = [
            {'month': 'Jan', 'series_a': 40, 'series_b': 25, 'series_c': 10, 'position': 0},
            {'month': 'Feb', 'series_a': 65, 'series_b': 15, 'series_c': 20, 'position': 1},
            {'month': 'Mar', 'series_a': 50, 'series_b': 30, 'series_c': 15, 'position': 2},
            {'month': 'Apr', 'series_a': 45, 'series_b': 35, 'series_c': 20, 'position': 3},
            {'month': 'May', 'series_a': 55, 'series_b': 20, 'series_c': 25, 'position': 4},
            {'month': 'Jun', 'series_a': 60, 'series_b': 25, 'series_c': 15, 'position': 5},
            {'month': 'Jul', 'series_a': 40, 'series_b': 38, 'series_c': 22, 'position': 6},
            {'month': 'Aug', 'series_a': 50, 'series_b': 28, 'series_c': 22, 'position': 7},
            {'month': 'Sep', 'series_a': 35, 'series_b': 20, 'series_c': 45, 'position': 8},
            {'month': 'Oct', 'series_a': 45, 'series_b': 15, 'series_c': 40, 'position': 9},
            {'month': 'Nov', 'series_a': 55, 'series_b': 25, 'series_c': 20, 'position': 10},
            {'month': 'Dec', 'series_a': 70, 'series_b': 30, 'series_c': 0, 'position': 11},
        ]

        for data in chart_data_list:
            ChartData.objects.create(dashboard=dashboard, **data)

        self.stdout.write(self.style.SUCCESS(f'Created {len(chart_data_list)} chart data points'))

        self.stdout.write(self.style.SUCCESS('Successfully populated database with sample data!'))
