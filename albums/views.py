from django.shortcuts import render
from .models import Album
from .forms import AlbumForm
from django.views.generic import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator

# Create your views here.
@method_decorator(login_required, name='dispatch')
class CreateAlbumView(CreateView):
    model = Album
    form_class = AlbumForm
    template_name = 'albums/form.html'
    success_url = reverse_lazy('create_album')
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['type'] = 'Add Album'
        return context
    
@method_decorator(login_required, name='dispatch')
class EditAlbumView(UpdateView):
    model = Album
    form_class = AlbumForm
    template_name = 'albums/form.html'
    success_url = reverse_lazy('home')
    pk_url_kwarg = 'id'
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["type"] = 'Edit Album'
        return context
    
@method_decorator(login_required, name='dispatch')
class DeleteAlbumView(DeleteView):
    model = Album
    template_name = 'delete.html'
    success_url = reverse_lazy('home')
    pk_url_kwarg = 'id'