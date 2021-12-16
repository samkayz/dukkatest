from django.urls import path, include
from django.conf import settings
from django.contrib import admin
from django.conf.urls.static import static
from django.views.generic import TemplateView
from rest_framework.schemas import get_schema_view

urlpatterns = [
    path('api_schema', get_schema_view(title="Dukka Test Documentation", description="Good"), name="api_schema"),
    path('docs/', TemplateView.as_view(
        template_name='docs.html',
        extra_context={'schema_url':'api_schema'}
        ), name='swagger-ui'),
    path('api/v1/', include('dukkaapp.urls')),
    path('admin/', admin.site.urls),
    
]+static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
