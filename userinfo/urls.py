from django.urls import path, include

from userinfo import views as userinfo_views

#app_name = 'userinfo'

urlpatterns = [
    path('', ),
    path('login/', userinfo_views.login_page, name='login'),
    path('logout/', userinfo_views.logout_page, name='logout'),
    #path('/signup', userinfo_views.signup(), name='signup'),
]