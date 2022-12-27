from django.urls import path, include
from rest_framework import routers
from .views import (
    todo_list_create,
    todo_home,
    todo_detail,
    Todos,
    TodoDetail,
    TodoMVS,
    )

router = routers.DefaultRouter()
router.register('todo', TodoMVS)

urlpatterns = [
    path('', todo_home),
    # path('list-create/', todo_list_create),
    # path('detail/<int:pk>', todo_detail),
    path('list-create/', Todos.as_view()),
    path('detail/<int:pk>', TodoDetail.as_view()),
    path('', include(router.urls)),

]