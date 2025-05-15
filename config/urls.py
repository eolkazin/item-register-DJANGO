
from django.contrib import admin
from django.urls import path
from core import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.login_view, name='login'),
    path('register/', views.register_view, name='register'),
    path('home/lista/', views.lista_view, name='lista'),
    path('home/register_item/', views.register_item_view, name='register_item'),
    path('deletar/<int:item_id>/', views.deletar_item, name='deletar_item'),
    path('home/fav', views.lista_view, name='fav'),



]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)