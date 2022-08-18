from django.shortcuts import render
from django.http import HttpResponse


def index(request):
    template = 'posts/index.html'
    return render(request, template)

def group_posts(request, any_slug):
    template = 'posts/group_list.html'
    return render(request, template) #HttpResponse(f'Страница с постами {pk}')

