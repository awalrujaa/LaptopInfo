from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

app_name = 'computer'

urlpatterns = [
    path('', views.index, name = 'index'),
    path('home', views.index, name = 'home'),
    # path('brand',views.brand_main_page, name='brand'),
    path('createList',views.createList, name='createList'),
    path('updateList/<int:id>/',views.updateList, name='updateList'),
    path('updateSuccess/<int:id>/',views.updated, name='updateSuccess'),
    path('viewList/',views.viewList, name='viewList'),
    # path('delete_image/<int:pk>/',views.delete_image, name='delete_image'),
    path('create_brand',views.create_brand, name='create_brand'),
    path('view_brand',views.view_brand, name='view_brand'),
    path('update_brand/<int:id>/',views.update_brand, name='update_brand'),
    
    path('add_specification',views.add_specification, name='add_specification'),
    path('view_specification',views.view_specification, name='view_specification'),
    path('update_specification/<int:id>/',views.update_specification, name='update_specification'),
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

