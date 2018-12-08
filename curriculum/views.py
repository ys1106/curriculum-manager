from django.shortcuts import render, redirect
from django.urls import reverse

from curriculum.forms import TopicForm

# Create your views here.
def index(request):

    return render(request, 'index.html', locals())


def mypage(request):

    return render(request, 'registration/mypage.html', locals())


def addTopic(request):
    if request.method == 'POST':
        form = TopicForm(request.POST)
        if form.is_valid():
            pass
        return redirect(reverse('index'))
    #else:

    return render(request, 'registration/mypage.html', locals())