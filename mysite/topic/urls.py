from django.urls import path
from . import views


urlpatterns = [
    path('', views.all_topics, name='all_topics'),
    path('study_plan', views.study_plan, name='study_plan'),
    path('admission/<int:pk>', views.AdmissionTaskDetailView.as_view(), name='admission_task'),
    path('<int:pk>', views.TaskDetailView.as_view(), name='task'),
    path('standard', views.standard, name='standard'),
    path('power', views.power, name='power'),
    path('rounding', views.rounding, name='rounding'),
    path('count', views.count, name='count'),
    path('equation', views.equation, name='equation'),
    path('function', views.function, name='function'),
    path('rational', views.rational, name='rational'),
    path('angle', views.angle, name='angle'),
    path('periodic', views.periodic, name='periodic'),
    # path('triangle', views.triangle, name='triangle'),
    path('area', views.area, name='area'),
    path('volume', views.volume, name='volume'),
    path('vector', views.vector, name='vector'),
    path('percent', views.percent, name='percent'),
    # path('log', views.log, name='log'),
    # path('derivative', views.derivative, name='derivative'),
    # path('integral', views.integral, name='integral'),
]
