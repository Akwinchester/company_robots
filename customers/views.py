from django.contrib.auth.models import Group
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

        # Добавление нового пользователя в группу "Клиенты"
        buyers_group = Group.objects.get(name='Клиенты')
        user.groups.add(buyers_group)

        login(self.request, user)

        return super().form_valid(form)


class LoginUser(LoginView):
    template_name = 'login.html'
    redirect_authenticated_user = True

    def get_success_url(self):
        user = self.request.user

        if user.groups.filter(name='Клиенты').exists():
            return reverse_lazy('create_order')

        if user.groups.filter(name='Менеджмент').exists():
            return reverse_lazy('get_report')

        if user.groups.filter(name='Технические специалисты').exists():
            return reverse_lazy('create_robot')

        return reverse_lazy('create_order')


def logout_user(request):
    logout(request)
    return redirect('login')