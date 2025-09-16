from django.urls import path
from django.views.generic import TemplateView
from . import views

app_name = 'quotes'

urlpatterns = [
    path('docs/', TemplateView.as_view(template_name='quotes/swagger_docs.html'), name='quotes-docs'),
    path('v1/health/', views.HealthCheckView.as_view(), name='quotes-health'),
    path('v1/random/', views.RandomResponseView.as_view(), name='quotes-random'),
    path('demo/', TemplateView.as_view(template_name='quotes/quotes_demo.html'), name='quotes-demo'),
]
