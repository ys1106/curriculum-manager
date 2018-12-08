from django.urls import path

from curriculum import views as curriculum_views

#app_name = 'curriculum'

urlpatterns = [
    path('', ),
    path('mypage/', curriculum_views.mypage(), name='mypage'),
]