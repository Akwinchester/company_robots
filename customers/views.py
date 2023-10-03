from django.contrib.auth.views import LoginView
from django.shortcuts import redirect
from django.views.generic import CreateView
from .forms import SignUpForm
from django.urls import reverse_lazy
from django.contrib.auth import login, logout


class SignUpView(CreateView):
    form_class = SignUpForm
    template_name = 'registration.html'
    success_url = reverse_lazy('create_order')

    def form_valid(self, form):
        user = form.save(commit=False)
        user.set_password(form.cleaned_data['password'])
        user.save()

        login(self.request, user)

        return super(SignUpView, self).form_valid(form)


class LoginUser(LoginView):
    template_name = 'login.html'
    redirect_authenticated_user = True

    def get_success_url(self):
        return reverse_lazy('create_order')


def logout_user(request):
    logout(request)
    return redirect('login')