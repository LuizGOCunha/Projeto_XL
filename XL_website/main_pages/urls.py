from django.conf import settings
from django.conf.urls.static import static
from django.urls import path
from. import views

urlpatterns = [
    path('', views.index, name='index'),
    path('sobre/', views.sobre, name='sobre'),
    path('contato/', views.contato, name='contato'),
    path('projetos/', views.projetos, name='projetos'),
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)