from . import views
from django.urls import path

urlpatterns = [
    path('', views.home, name='home'),
    path('create_post/', views.create_post, name='create_post'),
    path('post/<int:pk>', views.detail_post, name='detail_post'),
    path('post/update/<int:pk>', views.update_post, name='update_post'),
    path('post/delete/<int:pk>', views.delete_post, name='delete_post'),
]
