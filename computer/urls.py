from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

app_name = 'computer'

urlpatterns = [
    path('', views.index, name = 'index'),
    path('createList',views.createList, name='createList'),
    path('updateList/<int:id>/',views.updateList, name='updateList'),
    path('updateSuccess/<int:id>/',views.updated, name='updateSuccess'),
    path('viewList/',views.viewList, name='viewList'),
    path('delete_image/<int:pk>/',views.delete_image, name='delete_image'),
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

