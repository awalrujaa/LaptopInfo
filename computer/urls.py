from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

app_name = 'computer'

urlpatterns = [
    path('', views.index, name = 'index'),
    path('home', views.index, name = 'home'),
    # path('brand',views.brand_main_page, name='brand'),
    path('add_computer',views.add_computer, name='add_computer'),
    path('update_computer/<int:id>/',views.update_computer, name='update_computer'),
    path('view_computer/',views.view_computer, name='view_computer'),
    path('add_brand',views.add_brand, name='add_brand'),
    path('view_brand',views.view_brand, name='view_brand'),
    path('update_brand/<int:id>/',views.update_brand, name='update_brand'),
    path('delete_brand/<int:id>/',views.delete_brand, name='delete_brand'),
    path('delete_computer/<int:id>/',views.delete_computer, name='delete_computer'),
    path('delete_specification/<int:id>/',views.delete_specification, name='delete_specification'),
    
    path('add_specification',views.add_specification, name='add_specification'),
    path('view_specification',views.view_specification, name='view_specification'),
    path('update_specification/<int:id>/',views.update_specification, name='update_specification'),
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

