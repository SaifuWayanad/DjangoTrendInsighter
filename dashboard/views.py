from django.shortcuts import render
from django.views import View
from .models import Dashboard, Card, Order, ChartData


class DashboardView(View):
    """Main dashboard view"""
    
    def get(self, request):
        dashboard = Dashboard.objects.first()
        
        if not dashboard:
            dashboard = Dashboard.objects.create(title='Main Dashboard')
        
        cards = dashboard.cards.all()
        orders = dashboard.orders.all()[:5]
        chart_data = dashboard.chart_data.all()
        
        # Format chart data for frontend
        chart_labels = [d.month for d in chart_data]
        chart_series_a = [d.series_a for d in chart_data]
        chart_series_b = [d.series_b for d in chart_data]
        chart_series_c = [d.series_c for d in chart_data]
        
        context = {
            'dashboard': dashboard,
            'cards': cards,
            'orders': orders,
            'chart_data': chart_data,
            'chart_labels': chart_labels,
            'chart_series_a': chart_series_a,
            'chart_series_b': chart_series_b,
            'chart_series_c': chart_series_c,
        }
        
        return render(request, 'dashboard/index.html', context)


def home(request):
    """Home view"""
    return render(request, 'dashboard/home.html')


def my_accounts(request):
    """My Accounts view"""
    context = {
        'page_title': 'My Accounts',
        'page_icon': 'fas fa-user',
    }
    return render(request, 'dashboard/my_accounts.html', context)


def trend_insighter(request):
    """Trend Insighter view"""
    context = {
        'page_title': 'Trend Insighter',
        'page_icon': 'fas fa-chart-line',
    }
    return render(request, 'dashboard/trend_insighter.html', context)


def competitor_analysis(request):
    """Competitor Analysis view"""
    context = {
        'page_title': 'Competitor Analysis',
        'page_icon': 'fas fa-crosshairs',
    }
    return render(request, 'dashboard/competitor_analysis.html', context)


def vendor_mapping(request):
    """Vendor Mapping view"""
    context = {
        'page_title': 'Vendor Mapping',
        'page_icon': 'fas fa-map',
    }
    return render(request, 'dashboard/vendor_mapping.html', context)


def generate_plays(request):
    """Generate Plays view"""
    context = {
        'page_title': 'Generate Plays',
        'page_icon': 'fas fa-gamepad',
    }
    return render(request, 'dashboard/generate_plays.html', context)


def stake_holders(request):
    """Stake Holders view"""
    context = {
        'page_title': 'Stake Holders',
        'page_icon': 'fas fa-users',
    }
    return render(request, 'dashboard/stake_holders.html', context)


def our_capabilities(request):
    """Our Capabilities view"""
    context = {
        'page_title': 'Our Capabilities',
        'page_icon': 'fas fa-star',
    }
    return render(request, 'dashboard/our_capabilities.html', context)
