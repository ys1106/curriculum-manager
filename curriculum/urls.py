from django.urls import path

from curriculum import views as curriculum_views

app_name = 'curriculum'

urlpatterns = [
    #path('', ),
    path('mypage/', curriculum_views.my_page, name='mypage'),
    #path('add_topic/', curriculum_views.addTopic, name='add_topic')
]