from django.shortcuts import render, redirect
from datetime import datetime
from .models import News, Category, Comments

def create_base_context():

    return {
        "data" : datetime.now(),
        "endereco": {
            "rua": "Rua das Palmeiras, 123, Centro - Blumenau",
            "telefone": "(47) 33341232",
            "email": "apex.ensino@mail.com"
        },
        "latest_news" : News.objects.all().order_by('-id')[:3],
        "categoy_list": Category.objects.all()
    }

def index(request):

    news_list = News.objects.all()

    context = create_base_context()
    context.update({"news_list" : news_list})

    return render(request, 'index/index.html', context)

def single(request, id):

    context = create_base_context()

    if News.objects.filter(id=id).exists():

        comments = Comments.objects.filter(news__id=id).order_by('-id')

        context.update({
            "news": News.objects.get(id=id),
            "comments_list" : comments,
            "qnt_comments": len(comments) if comments else 0,
        })

        return render(request, 'single/single.html', context)

    return redirect('index')

def category(request, id):

    context = create_base_context()
    if News.objects.filter(category_id=id).exists():

        context.update({
            "news_list": News.objects.filter(category_id=id),
        })


    context.update({
        "category": Category.objects.get(id=id)
    })

    return render(request, 'category/category.html', context)