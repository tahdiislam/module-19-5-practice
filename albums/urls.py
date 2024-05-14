from django.urls import path
from . import views

urlpatterns = [
    path('add/', views.CreateAlbumView.as_view(), name='create_album'),
    path('edit/<int:id>', views.EditAlbumView.as_view(), name='edit_album'),
    path('delete/<int:id>', views.DeleteAlbumView.as_view(), name='delete_album')
]
