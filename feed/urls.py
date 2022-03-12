from django.urls import path
from django.conf.urls import handler404, handler500
from feed.views import create_post, post_list, post_details


app_name = 'post'
urlpatterns = [
    path('',post_list, name='post_list'),
    path('<int:pk>/',post_details,name='post_detail'),
    path('create/',create_post,name='create_post'),

]