from django.urls import path
from . import views

urlpatterns = [
    path('',views.home, name="HomePage"),
    path('login/',views.loginPage, name="LoginPage"),
    path('task/',views.task, name="TaskPage"),
    path('createtask/',views.createtask, name="CreateTaskPage"),
    path('edit/<int:id>',views.edittask, name="EditTaskPage"),
    path('taskdetail/<int:id>',views.taskdetail, name="TaskDetailPage"),
]
