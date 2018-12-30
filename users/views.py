from django.urls import reverse_lazy
from django.views.generic import CreateView, edit, ListView
from django.shortcuts import render
from django.contrib.auth import authenticate, login

from users.forms import CustomUserCreationForm, LoginForm
from users.models import CustomUser as Users


class SignUpView(CreateView):
    form_class = CustomUserCreationForm
    success_url = reverse_lazy('login')
    template_name = 'users/signup.html'


class LoginView(edit.FormView):
    template_name = 'users/login.html'
    form_class = LoginForm
    success_url = '/users/'

    def form_valid(self, form):
        username = form.cleaned_data['username']
        password = form.cleaned_data['password']
        user = authenticate(self.request, username=username, password=password)
        if user is not None:
            login(self.request, user)
        return super().form_valid(form)


class UserListView(ListView):
    queryset = Users.objects.order_by('-username')
    context_object_name = 'user_list'
    template_name = 'users/index.html'
