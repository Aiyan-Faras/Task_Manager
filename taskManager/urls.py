from taskManager import views
from django.urls import  path

app_name = "taskManager"

urlpatterns = [
    path("", views.index, name="index"),
    path("add", views.addTask, name="add")
]