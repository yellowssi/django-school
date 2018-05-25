from django.urls import path, include
from django.views.generic import TemplateView


urlpatterns = [
    path('', TemplateView.as_view(template_name='admin.html'), name='admin'),
    path('api/', include('jwc.admin_urls')),
]
