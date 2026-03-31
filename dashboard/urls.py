from django.urls import path
from . import views

app_name = 'dashboard'

urlpatterns = [
    path('', views.home, name='home'),
    path('dashboard/', views.DashboardView.as_view(), name='main'),
    path('my-accounts/', views.my_accounts, name='my_accounts'),
    path('trend-insighter/', views.trend_insighter, name='trend_insighter'),
    path('competitor-analysis/', views.competitor_analysis, name='competitor_analysis'),
    path('vendor-mapping/', views.vendor_mapping, name='vendor_mapping'),
    path('generate-plays/', views.generate_plays, name='generate_plays'),
    path('stake-holders/', views.stake_holders, name='stake_holders'),
    path('our-capabilities/', views.our_capabilities, name='our_capabilities'),
]
