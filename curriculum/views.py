from django.contrib.auth import login
from django.contrib.auth.models import User
from django.shortcuts import render, redirect
from django.urls import reverse

from curriculum.forms import TopicForm
from curriculum.models import UserTopic, Topic, RecommendList, Recommend

from curriculum import crawl as curriculum_crawl

from userinfo.models import UserInfo

# Create your views here.


def index(request):

    return render(request, 'index.html', locals())


def topic_add(user_value):
    # Topic에 사용자가 입력한(user_value) topic 유무에 따라
    try:
        data2 = Topic.objects.get(name=user_value)
    except:
        data2 = Topic.objects.create(name=user_value)
    return data2


def recommend_topics(user_value):
    # RecommendList에 추가할 topic(user_value) 유무에 따라
    try:
        topic = Topic.objects.get(name=user_value)
    except:
        topic = Topic.objects.create(name=user_value)
    try:
        data3 = RecommendList.objects.get(topic=topic)
    except:
        data3 = RecommendList.objects.create(topic=topic)
        list1 = curriculum_crawl.crawl(user_value)
        # crawl(user_value) 결과인 list1의 값들 Recommend 모델에 저장
        print(list1)
        for i in range(len(list1)):
            try:
                t2 = Topic.objects.get(name=list1[i][0])
            except:
                t2 = Topic.objects.create(name=list1[i][0])
            try:
                data4 = Recommend.objects.get(topic=t2,
                                              num=list1[i][1])
            except:
                data4 = Recommend.objects.create(topic=t2,
                                                 num=list1[i][1])
            data3.recommend.add(data4)
            data3.recommend.remove()


def my_page(request):
    if request.method == 'POST':
        form = TopicForm(request.POST)
        if form.is_valid():
            user_value = form.cleaned_data.get('value')
            #UserTopic에 로그인된 사용자 객체 생성
            try:
                #print(request.user)
                #print(User.objects.get(username=request.user))
                print(request.user)
                data1 = UserTopic.objects.get(user=request.user)
                #data1 = UserTopic.objects.get(user=UserInfo.objects.get(user=request.user))
                #data1 = UserTopic.objects.get(user=request.user)
            except:
                print(request.user)
                data1 = UserTopic()
                data1.user = request.user
                data1.save()


            # Topic과 로그인한 사용자 topic 테이블에 사용자가 입력한(user_value) 추가
            data2 = topic_add(user_value)
            data1.topic_list.add(data2)



            # Recommend와 RecommendList에 topic(user_value) 추가
            recommend_topics(user_value)

            #########확인#####################################################
            for f in data1.topic_list.all():
                print('TOPIC')
                print(f)
                f_topic = Topic.objects.get(name=f)
                f_recommend = RecommendList.objects.get(topic=f_topic)
                for d in f_recommend.recommend.all():
                    print('RECOMMEND')
                    print(d)
            #print(data1.topic_list.all())
            #####################################################################

            return render(request, 'registration/mypage.html', locals())


    form = TopicForm()
    # try:
    #     user_topic = UserTopic.objects.get(user=request.user)
    #     topics = user_topic.topic_list.all()
    #     print(topics)
    # except:
    #     pass

    return render(request, 'registration/mypage.html', locals())


# def addTopic(request):
#     if request.method == 'POST':
#         form = TopicForm(request.POST)
#         if form.is_valid():
#             user_value = form.cleaned_data.get('value')
#             user_name = request.user.username
#             try:
#                 user = UserTopic.objects.get(username=user_name)
#             except:
#                 user = UserTopic.objects.create(username=user_name)
#             finally:
#                 user.topic_list.add(user_value)
#         return render(request, 'registration/mypage.html', locals())
#
#     form = TopicForm()
#     return render(request, 'registration/mypage.html', locals())


