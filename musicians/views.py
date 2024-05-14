from django.shortcuts import render
from .forms import MusicianForm
from .models import Musician
from django.views.generic import CreateView, UpdateView
from django.urls import reverse_lazy
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator

# Create your views here.

@method_decorator(login_required, name='dispatch')
class AddMusicianView(CreateView):
    model = Musician
    form_class = MusicianForm
    template_name = 'musicians/form.html'
    success_url = reverse_lazy('add_musician')
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["type"] = 'Add Musician'
        return context
    
@method_decorator(login_required, name='dispatch')
class EditMusicianView(UpdateView):
    model = Musician
    form_class = MusicianForm
    template_name = 'musicians/form.html'
    pk_url_kwarg = 'id'
    success_url = reverse_lazy('home')
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["type"] = 'Edit Musician'
        return context