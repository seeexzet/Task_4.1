from django.shortcuts import render

from articles.models import Article


def articles_list(request):
    template = 'articles/news.html'
    article = Article.objects.all()
    # for article_one in article:
    #     print(f'{article_one.title} \n')
    #     for sc in article_one.scopes.all():
    #         print(f'{sc.tag.name}, {sc.is_main} ')
    context = {'object_list': article}

    # используйте этот параметр для упорядочивания результатов
    # https://docs.djangoproject.com/en/3.1/ref/models/querysets/#django.db.models.query.QuerySet.order_by
    # ordering = '-published_at'

    return render(request, template, context)
