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
                   'Стандартный вид числа': 'standard', 'Степень': 'power',
                   'Тригонометрия': 'periodic', 'Угол': 'angle', 'Уравнения': 'equation', 'Функция': 'function',
                   }
    }  # 'Логарифм': 'log', 'Производная': 'derivative', 'Интеграл': 'integral',
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
            user_answer = float(request.POST.get("answer"))
            if user_answer != self.object.answer:
                if self.object.id == 1:
                    if user_answer == 690:
                        Theme.objects.create(theme_name='Вектор', theme_link='vector', user_id=request.user.id)
                    else:
                        Theme.objects.create(theme_name='Вектор', theme_link='vector', user_id=request.user.id)
                        Theme.objects.create(theme_name='Тригонометрия', theme_link='periodic', user_id=request.user.id)
                if self.object.id == 2:
                    Theme.objects.create(theme_name='Уравнения', theme_link='equation', user_id=request.user.id)
                    Theme.objects.create(theme_name='Арифметика', theme_link='count', user_id=request.user.id)
                if self.object.id == 3:
                    if user_answer == 9.6:
                        Theme.objects.create(theme_name='Угол', theme_link='angle', user_id=request.user.id)
                    else:
                        Theme.objects.create(theme_name='Угол', theme_link='angle', user_id=request.user.id)
                        Theme.objects.create(theme_name='Тригонометрия', theme_link='periodic', user_id=request.user.id)
                        Theme.objects.create(theme_name='Вектор', theme_link='vector', user_id=request.user.id)
                if self.object.id == 4:
                    if abs(user_answer - self.object.answer) < 0.2:
                        Theme.objects.create(theme_name='Округление', theme_link='rounding', user_id=request.user.id)
                    elif user_answer % self.object.answer == 0 or self.object.answer % user_answer == 0:
                        Theme.objects.create(theme_name='Стандартный вид числа', theme_link='standard',
                                             user_id=request.user.id)
                        Theme.objects.create(theme_name='Степень', theme_link='power', user_id=request.user.id)
                    else:
                        Theme.objects.create(theme_name='Округление', theme_link='rounding', user_id=request.user.id)
                        Theme.objects.create(theme_name='Стандартный вид числа', theme_link='standard',
                                             user_id=request.user.id)
                        Theme.objects.create(theme_name='Степень', theme_link='power', user_id=request.user.id)
                        Theme.objects.create(theme_name='Площадь', theme_link='area', user_id=request.user.id)
                        Theme.objects.create(theme_name='Арифметика', theme_link='count', user_id=request.user.id)
                if self.object.id == 5:
                    if abs(user_answer - self.object.answer) < 2:
                        Theme.objects.create(theme_name='Округление', theme_link='rounding', user_id=request.user.id)
                    elif user_answer % self.object.answer == 0 or self.object.answer % user_answer == 0:
                        Theme.objects.create(theme_name='Стандартный вид числа', theme_link='standard',
                                             user_id=request.user.id)
                    else:
                        Theme.objects.create(theme_name='Округление', theme_link='rounding', user_id=request.user.id)
                        Theme.objects.create(theme_name='Стандартный вид числа', theme_link='standard',
                                             user_id=request.user.id)
                        Theme.objects.create(theme_name='Объем', theme_link='volume', user_id=request.user.id)
                        Theme.objects.create(theme_name='Степень', theme_link='power', user_id=request.user.id)
                if self.object.id == 6:
                    if abs(user_answer - self.object.answer) < 0.02:
                        Theme.objects.create(theme_name='Округление', theme_link='rounding', user_id=request.user.id)
                    else:
                        Theme.objects.create(theme_name='Округление', theme_link='rounding', user_id=request.user.id)
                        Theme.objects.create(theme_name='Процент', theme_link='percent', user_id=request.user.id)
                        Theme.objects.create(theme_name='Арифметика', theme_link='count', user_id=request.user.id)
                if self.object.id == 7:
                    if user_answer == 100:
                        Theme.objects.create(theme_name='Уравнения', theme_link='equation', user_id=request.user.id)
                    else:
                        Theme.objects.create(theme_name='Арифметика', theme_link='count', user_id=request.user.id)
                        Theme.objects.create(theme_name='Уравнения', theme_link='equation', user_id=request.user.id)
                        Theme.objects.create(theme_name='Рациональная дробь', theme_link='rational',
                                             user_id=request.user.id)
                        Theme.objects.create(theme_name='Степень', theme_link='power', user_id=request.user.id)
                if self.object.id == 8:
                    Theme.objects.create(theme_name='Арифметика', theme_link='count', user_id=request.user.id)
                    Theme.objects.create(theme_name='Функция', theme_link='function', user_id=request.user.id)
            temp = self.object.id + 1
            counter = temp
            if counter > 8:
                return render(request, 'topic/admission_done.html')
            data = {'id': temp, 'data': self.object}
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

                elif (self.object.theme in ['power', 'count', 'area', 'angle', 'periodic', 'vector']) \
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
                        if self.object.theme == 'angle':
                            if TaskDetailView.counter < 2:
                                n = random.randint(564, 609)
                            elif TaskDetailView.counter < 5:
                                n = random.randint(609, 702)
                        if self.object.theme == 'periodic':
                            if TaskDetailView.counter < 2:
                                n = random.randint(703, 752)
                            elif TaskDetailView.counter < 3:
                                n = random.randint(753, 778)
                            elif TaskDetailView.counter < 5:
                                n = random.randint(778, 832)
                        if self.object.theme == 'vector':
                            if TaskDetailView.counter < 2:
                                n = random.randint(893, 922)
                            elif TaskDetailView.counter < 3:
                                n = random.randint(923, 942)
                            elif TaskDetailView.counter < 5:
                                n = random.randint(943, 982)
                        if self.object.theme == 'equation':
                            if TaskDetailView.counter < 2:
                                n = random.randint(1013, 1042)
                            elif TaskDetailView.counter < 3:
                                n = random.randint(1085, 1114)
                            elif TaskDetailView.counter < 4:
                                n = random.randint(1043, 1054)
                            elif TaskDetailView.counter < 5:
                                n = random.randint(1055, 1084)
                        if self.object.theme == 'function':
                            if TaskDetailView.counter < 2:
                                n = random.randint(1198, 1256)
                            elif TaskDetailView.counter < 3:
                                n = random.randint(1257, 1315)
                            elif TaskDetailView.counter < 4:
                                n = random.randint(1145, 1197)
                            elif TaskDetailView.counter < 5:
                                n = random.randint(1316, 1330)

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


def count(request):
    data = {'id': random.randint(316, 394)}
    return render(request, 'topic/count/theory.html', data)


def equation(request):
    data = {'id': random.randint(983, 1012)}
    return render(request, 'topic/equation/theory.html', data)


def function(request):
    data = {'id': random.randint(1115, 1144)}
    return render(request, 'topic/function/theory.html', data)


def rational(request):
    data = {'id': random.randint(41, 89)}
    return render(request, 'topic/rational/theory.html', data)


def angle(request):
    data = {'id': random.randint(550, 563)}
    return render(request, 'topic/angle/theory.html', data)


def periodic(request):
    data = {'id': random.randint(703, 752)}
    return render(request, 'topic/periodic/theory.html', data)


#     def triangle(request):
#     data = {'id': random.randint(90, 187)}
#     return render(request, 'topic/triangle/theory.html', data)


def area(request):
    data = {'id': random.randint(435, 453)}
    return render(request, 'topic/area/theory.html', data)


def volume(request):
    data = {'id': random.randint(509, 549)}
    return render(request, 'topic/volume/theory.html', data)


def vector(request):
    data = {'id': random.randint(833, 892)}
    return render(request, 'topic/vector/theory.html', data)


def percent(request):
    data = {'id': random.randint(90, 187)}
    return render(request, 'topic/percent/theory.html', data)

# def log(request):
#     data = {'id': random.randint()}
#     return render(request, 'topic/log/theory.html', data)
#
#
# def derivative(request):
#     data = {'id': random.randint()}
#     return render(request, 'topic/derivative/theory.html', data)
#
#
# def integral(request):
#     data = {'id': random.randint()}
#     return render(request, 'topic/integral/theory.html', data)
