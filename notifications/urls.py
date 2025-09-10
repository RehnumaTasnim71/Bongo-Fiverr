from django.urls import path
from . import views

urlpatterns = [
    path('', views.notifications_list, name='notifications_list'),
    path('<int:pk>/read/', views.mark_notification_read, name='mark_notification_read'),
]
