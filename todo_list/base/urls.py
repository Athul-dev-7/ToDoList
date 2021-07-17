from django.urls import path
from .views import TaskCreate, TaskDetail, TaskList, TaskUpdate, TaskDelete, LoginView, RegisterView
from django.contrib.auth.views import LogoutView

urlpatterns = [
    path('register/',             RegisterView.as_view(),                name='register'),
    path('login/',                LoginView.as_view(),                   name='login'),
    path('logout/',               LogoutView.as_view(next_page='login'), name='logout'),
    path('',                      TaskList.as_view(),                    name='tasks'),       
    path('task-create/',          TaskCreate.as_view(),                  name='task-create'),
    path('task/<int:pk>/',        TaskDetail.as_view(),                  name='task'),
    path('task-update/<int:pk>/', TaskUpdate.as_view(),                  name='task-update'),
    path('task-delete/<int:pk>/', TaskDelete.as_view(),                  name='task-delete'),
]