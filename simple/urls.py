from django.urls import path

from rest_framework.urlpatterns import format_suffix_patterns

from .views import TodoList, TodoDetail


urlpatterns = {

    path('', TodoList.as_view(), name='todo_list'),
    path('<int:pk>/', TodoDetail.as_view(), name='todo_detail'),

}

urlpatterns = format_suffix_patterns(urlpatterns)
