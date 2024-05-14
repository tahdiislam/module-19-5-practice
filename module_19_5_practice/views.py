from django.views.generic import TemplateView
from albums.models import Album

class AllAlbumView(TemplateView):
    template_name = 'home.html'
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        albums = Album.objects.all()
        context['albums'] = albums
        return context