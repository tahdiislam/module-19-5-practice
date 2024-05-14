from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('musician/', include('musicians.urls')),
    path('user/', include('users.urls')),
    path('album/', include('albums.urls')),
    path('', views.AllAlbumView.as_view(), name='home')
]
