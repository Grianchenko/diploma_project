from django.shortcuts import render
from django.views.generic.edit import FormView
from django.views.generic import DetailView
from .models import Problem, Theme, ProblemTest
from .forms import ProblemForm
import random
from django.urls import reverse


def study_plan(request):
    temp = {}
    for theme in Theme.objects.filter(user_id=request.user.id).order_by('theme_name'):
        temp[theme.theme_name] = theme.theme_link
    data = {
        'title': 'Учебный план',
        'themes': temp,
    }
    return render(request, 'main/study_plan.html', data)


def all_topics(request):
    data = {
        'title': 'Все доступные темы',
        'themes': {'Арифметика': 'count', 'Вектор': 'vector', 'Объем': 'volume', 'Округление': 'rounding',
                   'Площадь': 'area', 'Процент': 'percent', 'Рациональная дробь': 'rational',
                   'Стандартный вид числа': 'standard', 'Степень': 'power', 'Треугольник': 'triangle',
                   'Тригонометрия': 'periodic', 'Угол': 'angle', 'Уравнение': 'equation', 'Функция': 'function',
                   }
    }  # 'Логарифм': 'log', 'Производная': 'derivative', 'Интеграл': 'integral'
    return render(request, 'topic/all_topics.html', data)


class AdmissionTaskDetailView(DetailView, FormView):
    model = ProblemTest
    form_class = ProblemForm
    template_name = 'topic/test.html'
    context_object_name = 'problem'
    counter = 1

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.object = None

    def get_success_url(self):
        return reverse('task', kwargs={'pk': self.object.id})

    def get_context_data(self, **kwargs):
        context = super(AdmissionTaskDetailView, self).get_context_data(**kwargs)
        context['form'] = ProblemForm(initial={'post': self.object})
        return context

    def post(self, request, *args, **kwargs):
        self.object = self.get_object()
        if request.method == 'POST':
            if float(request.POST.get("answer")) != self.object.answer:
                Theme.objects.create(theme_name='Рациональная дробь', theme_link='rational', user_id=request.user.id)
                Theme.objects.create(theme_name='Округление', theme_link='rounding', user_id=request.user.id)
                Theme.objects.create(theme_name='Процент', theme_link='percent', user_id=request.user.id)
            n = self.object.id + 1
            counter = n
            if counter > 10:
                return render(request, 'topic/admission_done.html')
            data = {'id': n, 'data': self.object}
            return render(request, 'topic/admission_next.html', data)


class TaskDetailView(DetailView, FormView):
    model = Problem
    form_class = ProblemForm
    template_name = 'topic/test.html'
    context_object_name = 'problem'
    counter = 0

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.object = None

    def get_success_url(self):
        return reverse('task', kwargs={'pk': self.object.id})

    def get_context_data(self, **kwargs):
        context = super(TaskDetailView, self).get_context_data(**kwargs)
        context['form'] = ProblemForm(initial={'post': self.object})
        return context

    def post(self, request, *args, **kwargs):
        self.object = self.get_object()
        if request.method == 'POST':
            if float(request.POST.get("answer")) == self.object.answer:
                if (self.object.theme == 'rounding' or self.object.theme == 'standard' or
                        self.object.theme == 'rational' or self.object.theme == 'percent' or
                        self.object.theme == 'volume') and TaskDetailView.counter < 2:
                    TaskDetailView.counter += 1
                    n = self.object.id
                    while n == self.object.id:
                        if self.object.theme == 'rounding':
                            n = random.randint(1, 40)
                        elif self.object.theme == 'rational':
                            n = random.randint(41, 89)
                        elif self.object.theme == 'percent':
                            n = random.randint(90, 187)
                        elif self.object.theme == 'standard':
                            n = random.randint(188, 237)
                        elif self.object.theme == 'volume':
                            n = random.randint(509, 549)
                    data = {
                        'data': self.object,
                        'id': n
                    }
                    return render(request, 'topic/next.html', data)
                elif (self.object.theme == 'power' or self.object.theme == 'count' or self.object.theme == 'area') \
                        and TaskDetailView.counter < 4:
                    TaskDetailView.counter += 1
                    n = self.object.id
                    while n == self.object.id:
                        if self.object.theme == 'power':
                            if TaskDetailView.counter < 2:
                                n = random.randint(238, 271)
                            elif TaskDetailView.counter < 5:
                                n = random.randint(272, 315)
                        if self.object.theme == 'count':
                            if TaskDetailView.counter < 3:
                                n = random.randint(316, 394)
                            elif TaskDetailView.counter < 5:
                                n = random.randint(394, 434)
                        if self.object.theme == 'area':
                            if TaskDetailView.counter < 2:
                                n = random.randint(454, 468)
                            elif TaskDetailView.counter < 4:
                                n = random.randint(469, 493)
                            elif TaskDetailView.counter < 5:
                                n = random.randint(494, 508)

                    data = {
                        'data': self.object,
                        'id': n
                    }
                    return render(request, 'topic/next.html', data)
                else:  # Если тема пройдена, показать страницу "тема изучена"
                    TaskDetailView.counter = 0
                    Theme.objects.filter(theme_link=self.object.theme, user_id=request.user.id).delete()
                    return render(request, 'topic/done.html')
            else:
                TaskDetailView.counter = 0
                wrong_answer = float(request.POST.get("answer"))

                if round(wrong_answer, 0) == wrong_answer:
                    wrong_answer = int(wrong_answer)

                data = {
                    'data': self.object,
                    'wrong_answer': wrong_answer,
                }
                return render(request, 'topic/incorrect.html', data)


def standard(request):
    data = {'id': random.randint(188, 237)}
    return render(request, 'topic/standard/theory.html', data)


def power(request):
    data = {'id': random.randint(238, 271)}
    return render(request, 'topic/power/theory.html', data)


def rounding(request):
    data = {'id': random.randint(1, 40)}
    return render(request, 'topic/rounding/theory.html', data)


# def rounding_task(request):
#
#     # if request.method == 'POST':
#     #     instance = Problem.objects.get(id=int(request.POST['my_id']))
#     #     # form = ProblemForm(request.POST, instance=instance)
#     #     if float(request.POST.get("answer")) == instance.answer:
#     #         data = {
#     #             'data': Problem.objects.get(id=int(request.POST['my_id'])),
#     #         }
#     #     else:
#     #         data = {
#     #             'data': Problem.objects.get(id=1)
#     #         }
#     #     return render(request, 'topic/rounding/task.html', data)
#
#     form = ProblemForm()
#     n = random.randint(1, 40)
#     data = {
#         'data': Problem.objects.get(id=n),
#         'form': form
#     }
#     return render(request, f'topic/{Problem.objects.get(id=n).id}', data)


def count(request):
    data = {'id': random.randint(316, 394)}
    return render(request, 'topic/count/theory.html', data)


def equation(request):
    data = {'id': random.randint(90, 187)}
    return render(request, 'topic/equation/theory.html', data)


def function(request):
    data = {'id': random.randint(90, 187)}
    return render(request, 'topic/function/theory.html', data)


def rational(request):
    data = {'id': random.randint(41, 89)}
    return render(request, 'topic/rational/theory.html', data)


def angle(request):
    data = {'id': random.randint(90, 187)}
    return render(request, 'topic/angle/theory.html', data)


def periodic(request):
    data = {'id': random.randint(90, 187)}
    return render(request, 'topic/periodic/theory.html', data)


def triangle(request):
    data = {'id': random.randint(90, 187)}
    return render(request, 'topic/triangle/theory.html', data)


def area(request):
    data = {'id': random.randint(435, 453)}
    return render(request, 'topic/area/theory.html', data)


def volume(request):
    data = {'id': random.randint(509, 549)}
    return render(request, 'topic/volume/theory.html', data)


def vector(request):
    data = {'id': random.randint(90, 187)}
    return render(request, 'topic/vector/theory.html', data)


def percent(request):
    data = {'id': random.randint(90, 187)}
    return render(request, 'topic/percent/theory.html', data)

# def log(request):
#     data = {'id': random.randint(90, 187)}
#     return render(request, 'topic/log/theory.html', data)
#
#
# def derivative(request):
#     data = {'id': random.randint(90, 187)}
#     return render(request, 'topic/derivative/theory.html', data)
#
#
# def integral(request):
#     data = {'id': random.randint(90, 187)}
#     return render(request, 'topic/integral/theory.html', data)
