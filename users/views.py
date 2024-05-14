from django.contrib.auth.views import LoginView, LogoutView
from django.urls import reverse_lazy
from django.contrib import messages
from django.views.generic import CreateView, TemplateView
from django.contrib.auth.models import User
from .forms import UserForm
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator

class CreateUserView(CreateView):
    model = User
    form_class = UserForm
    template_name = 'users/form.html'
    success_url = reverse_lazy('add_musician')
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['type'] = 'Register'
        return context

# Create your views here.
class LoginUserView(LoginView):
    template_name = 'users/form.html'
    def get_success_url(self):
        return reverse_lazy('profile')
    def form_valid(self, form):
        messages.success(self.request, "Logged in successfully")
        return super().form_valid(form)
    def form_invalid(self, form):
        messages.warning(self.request, "Logged information incorrect")
        return super().form_invalid(form)
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['type'] = 'Login'
        return context

@method_decorator(login_required, name='dispatch')
class UserLogoutView(LogoutView):
    next_page = reverse_lazy('login')

@method_decorator(login_required, name='dispatch')
class ProfileView(TemplateView):
    template_name = 'users/profile.html'