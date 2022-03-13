from django.urls import path
from django.conf.urls import handler404, handler500
from users import views as user_views


app_name = 'users'
urlpatterns = [
    path('', user_views.users_list, name='users_list'),
    path('profile/',user_views.my_profile, name='profile'),
	path('<int:phone>/', user_views.profile_view, name='profile_view'),
	path('friends/', user_views.friend_list, name='friend_list'),
    path('friend-request/send/<int:id>/', user_views.send_friend_request, name='send_friend_request'),
    path('friend-request/accept/<int:id>/', user_views.accept_friend_request, name='accept_friend_request'),
    path('search_users/', user_views.search_users, name='search_users'),
    path('search/', user_views.search_api, name='search'),
]