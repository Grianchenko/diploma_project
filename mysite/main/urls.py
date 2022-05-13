from django.urls import path
from . import views
# from .views import TaskDetailView

urlpatterns = [
    path('', views.index, name='home'),
    # path('<int:pk>', TaskDetailView.as_view(), name='test1'),
    path('login', views.LoginUser.as_view(), name='login'),
    path('register', views.RegisterUser.as_view(), name='register'),
    path('logout', views.logout_user, name='logout'),
    # path('study_plan', views.study_plan, name='study_plan'),
    path('admission', views.admission, name='admission'),
    # path('admission/taks_1', views.test_1, name='test_1'),
    # path('admission/task_2', views.test_2, name='test_2'),
    # path('admission/task_3', views.test_3, name='test_3'),
    # path('admission/task_4', views.test_4, name='test_4'),
    # path('admission/task_5', views.test_5, name='test_5'),
    # path('admission/task_6', views.test_6, name='test_6'),
    # path('admission/task_7', views.test_7, name='test_7'),
    # path('admission/task_8', views.test_8, name='test_8'),
    # path('admission/task_9', views.test_9, name='test_9'),
    # path('admission/task_10', views.test_10, name='test_10'),
]
