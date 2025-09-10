
from django.urls import path
from . import views
from .views import submit_review

urlpatterns = [
    path('<int:pk>/place/', views.place_order, name='place_order'),
    path('<int:pk>/detail/', views.order_detail, name='order_detail'),
    path('buyer/', views.buyer_dashboard, name='buyer_dashboard'),
    path('seller/', views.seller_dashboard, name='seller_dashboard'),
    path("<int:pk>/mark-inprogress/", views.order_mark_inprogress, name="order_mark_inprogress"),
    path("<int:order_id>/complete/", views.complete_order, name="complete_order"),
    path('order/<int:order_id>/review/', submit_review, name='submit_review'),
]
