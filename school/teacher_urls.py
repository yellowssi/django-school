from django.urls import path, include
from django.views.generic import TemplateView


urlpatterns = [
    path('', TemplateView.as_view(template_name='teacher.html'), name='teacher'),
    path('api/', include('jwc.teacher_urls')),
]
