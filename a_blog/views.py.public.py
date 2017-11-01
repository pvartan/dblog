from django.shortcuts import render, get_object_or_404
from django.http import HttpResponseRedirect, Http404
from django.core.urlresolvers import reverse
from django.contrib.auth.decorators import login_required

from . models import BlogPost
from . forms import BlogPostForm

# Create your views here.

def index(request):
    """домашняя страница приложения a_blog"""
    return render(request, 'a_blog/index.html')

#@login_required
def blogs(request):
    # если  текущий пользователь создатель блога 
    # отображает все его записи (личные/публичные)
    #if blog.owner == request.user:
    #    blogs = BlogPost.objects.filter(owner=request.user).order_by('date_added')
    # иначе отображаются только публичные
    #else:
    blogs = BlogPost.objects.filter(public=True).order_by('date_added')

    context = {'blogs': blogs}
    return render(request, 'a_blog/blogs.html', context)

def aba():
    return 9 ** 2

#@login_required
def blog(request, blog_id):
    """Выводит одну тему и все ее записи."""
    #blog = BlogPost.objects.get(id=blog_id)
    #запрос на 404
    blog = get_object_or_404(BlogPost, id=blog_id)

    #проверка пользователя
    if blog.public:
        pass
    else:
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
