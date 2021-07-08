from django.urls import path

from .views import TaskList, TaskCreate, TaskDetail, TaskEdit

urlpatterns = [
    path('', TaskList.as_view(), name='tasks'),
    path('create-task/', TaskCreate.as_view(), name='create-task'),
    path('detail-task/<int:pk>', TaskDetail.as_view(), name='detail-task'),
    path('edit-task/<int:pk>', TaskEdit.as_view(), name='edit-task'),

]