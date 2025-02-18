from django.urls import path
from . import views

urlpatterns = [
    path('add/', views.AddMusicianView.as_view(), name='add_musician'),
    path('edit/<int:id>', views.EditMusicianView.as_view(), name='edit_musician')
]
