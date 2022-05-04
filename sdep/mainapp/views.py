from django.http import HttpResponse, HttpResponseNotFound, Http404
from django.shortcuts import render, redirect, get_object_or_404
from .models import *


def index(request):
    posts = Mainapp.objects.filter(cat_id=2)[:3]
    hposts = Mainapp.objects.filter(cat_id=1)[:1]
    iposts = Mainapp.objects.filter(cat_id=3)[:3]
    cats = Category.objects.all()
    context = {
        'posts': posts,
        'hposts': hposts,
        'iposts': iposts,
        'cats': cats,
        'title': 'Головна сторінка',
        'cat_selected': 0,
    }
    return render(request, 'mainapp/index.html', context=context)


def about(request):
    return render(request, 'mainapp/about.html', {'title': 'Про сайт'})


def credit_union(request):
    return render(request, 'mainapp/about_us/credit_union.html', {'title': 'Про кредитну спілку'})


def structure(request):
    return render(request, 'mainapp/about_us/structure.html', {'title': 'Структура кредитної спілки'})


def contacts(request):
    return render(request, 'mainapp/about_us/contacts.html', {'title': 'Контакти'})


def news(request):
    posts = Mainapp.objects.filter(cat_id=2)[:9]
    cats = Category.objects.all()
    context = {
        'posts': posts,
        'cats': cats,
        'title': 'Новини',
        'cat_selected': 0,
    }

    return render(request, 'mainapp/news_more.html', context=context)


def information(request):
    iposts = Mainapp.objects.filter(cat_id=3)[:9]
    cats = Category.objects.all()
    context = {
        'iposts': iposts,
        'cats': cats,
        'title': 'Інформація',
        'cat_selected': 0,
    }

    return render(request, 'mainapp/information_more.html', context=context)


def charter(request):
    return render(request, 'mainapp/documents/charter.html', {'title': 'Статут'})


def agreements(request):
    return render(request, 'mainapp/documents/agreements.html', {'title': 'Угоди'})


def pageNotFound(request, exception):
    return HttpResponseNotFound('<h1>Сторінки не існує</h1>')


def show_post(request, post_slug):
    post = get_object_or_404(Mainapp, slug=post_slug)

    context = {
        'post': post,
        'title': post.title,
        'cat_selected': post.cat_id,
    }

    return render(request, 'mainapp/post.html', context=context)


def show_category(request, cat_id):
    posts = Mainapp.objects.filter(cat_id=cat_id)
    cats = Category.objects.all()

    if len(posts) == 0:
        raise Http404()

    context = {
        'posts': posts,
        'cats': cats,
        'title': 'Відображення за категоріями',
        'cat_selected': cat_id,
    }
    return HttpResponse(f"Відображення категорії з ID = {cat_id}")


# def categories(request, catid):
#    if(request.POST):
#        print(request.POST)

#    return HttpResponse(f"<h1>Дописи за категоріями</h1><p>{catid}</p>")


# def archive(request, year):
#    if int(year) > 2022:
#        return redirect('home', permanent=True)
#    return HttpResponse(f"<h1>Архів за роками</h1><p>{year}</p>")


