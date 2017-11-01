from django.shortcuts import render, get_object_or_404
from django.http import HttpResponseRedirect, Http404, HttpResponse
from django.core.urlresolvers import reverse
from django.contrib.auth.decorators import login_required

from . models import BlogPost
from . forms import BlogPostForm
import datetime

# Create your views here.

def index(request):
    """домашняя страница приложения a_blog"""
    return render(request, 'a_blog/index.html')

@login_required
def blogs(request):
    blogs = BlogPost.objects.filter(owner=request.user).order_by('date_added')

    # отображает чужие публичные посты
    pub_blogs = BlogPost.objects.exclude(owner=request.user).filter(public=True).order_by('date_added')

    context = {'blogs': blogs, 'pub_blogs': pub_blogs}
    return render(request, 'a_blog/blogs.html', context)


@login_required
def blog(request, blog_id):
    """Выводит одну тему и все ее записи."""
    #blog = BlogPost.objects.get(id=blog_id)
    #запрос на 404
    blog = get_object_or_404(BlogPost, id=blog_id)

    #проверка пользователя
    if blog.owner != request.user:
        raise Http404

    context = {'blog': blog}
    return render(request, 'a_blog/blog.html', context)

@login_required
def new_blog(request):
    """Определяет новую тему."""
    if request.method != 'POST':
        # Данные не отправлялись; создается пустая форма.
        form = BlogPostForm()

    else:
        # Отправлены данные POST; обработать данные.
        form = BlogPostForm(request.POST)
        if form.is_valid():

            #проверка пользователя
            new_blog = form.save(commit=False)
            new_blog.owner = request.user
            new_blog.save()
            return HttpResponseRedirect(reverse('a_blog:blogs'))

    context = {'form': form}
    return render(request, 'a_blog/new_blog.html', context)

@login_required
def edit_blog(request, blog_id):
    """Редактирует существующую запись."""
    #blog = BlogPost.objects.get(id=blog_id)
    blog = get_object_or_404(BlogPost, id=blog_id)

    #проверка пользователя
    if blog.owner != request.user:
        raise Http404

    if request.method != 'POST':
        # Исходный запрос; форма заполняется данными текущей записи.
        form = BlogPostForm(instance=blog)

    else:
        # Отправка данных POST; обработать данные.
        form = BlogPostForm(instance=blog, data=request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('a_blog:blog',  args=[blog.id]))

    context = {'blog': blog, 'form': form}
    return render(request, 'a_blog/edit_blog.html', context)


###########################
def mymy(request):
    a = 2
    b = 3
    x = a + b
    context = {'x': x, 'req': request}
    return render(request, 'a_blog/mymy.html', context)

def me(request):
    #now = datetime.datetime.now()
    blogs = BlogPost.objects.get(id=7)
    blogs.title = 'hacked by API'
    blogs.save()
    ok = blogs.title

    html = "<a href='http://127.0.0.1:8000/me'>bid</a></br>"

    html += "<html><body>It {}.</body></html>".format(ok)
    return HttpResponse(html)
