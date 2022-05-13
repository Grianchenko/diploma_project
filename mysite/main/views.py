from django.contrib.auth import logout, login
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.contrib.auth.views import LoginView
from django.shortcuts import render, redirect
from django.views.generic.edit import FormView, CreateView
from django.views.generic import DetailView
# from .models import ProblemTest, Theme
from .forms import RegisterUserForm, LoginUserForm
import random
from django.urls import reverse, reverse_lazy


def index(request):
    data = {
        'title': 'Главная страница'
    }
    return render(request, 'main/index.html', data)


class RegisterUser(CreateView):
    form_class = RegisterUserForm
    template_name = 'main/register.html'
    success_url = reverse_lazy('admission')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # context['form'] = TestForm(initial={'post': self.object})
        return context

    def form_valid(self, form):
        user = form.save()
        login(self.request, user)
        return redirect('admission')


class LoginUser(LoginView):
    form_class = LoginUserForm
    template_name = 'main/login.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # context['form'] = TestForm(initial={'post': self.object})
        return context

    def get_success_url(self):
        return reverse_lazy('study_plan')


def logout_user(request):
    logout(request)
    return redirect('login')


# def study_plan(request):
#     temp = {}
#     for theme in Theme.objects.filter(user_id=request.user.id):
#         temp[theme.theme_name] = theme.theme_link
#     data = {
#         'title': 'Учебный план',
#         'themes': temp,
#     }
#
#     return render(request, 'main/study_plan.html', data)


def admission(request):
    data = {'id': 1}
    return render(request, 'main/admission.html', data)

#
# def test_1(request):
#     data = {'title': '',
#             'condition': '',
#             'answer': '',
#
#             }
#     return render(request, 'main/test/task.html', data)
