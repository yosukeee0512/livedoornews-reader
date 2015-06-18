# -*- coding: utf-8 -*-
from django.shortcuts import render
from news.models import Article,Category
from django.shortcuts import render_to_response, get_object_or_404
from django.core.exceptions import ObjectDoesNotExist
from django.http import Http404
from django.template import Context,RequestContext
from django.views.decorators.vary import vary_on_headers
from django.views.decorators.cache import cache_control
from django.views.decorators.cache import cache_page
from django.core.cache import cache
from django.db.models import Q

@cache_page(60 * 120)
def index(request):
    article = None
    try:
        category = list(Category.objects.all())
        article_list = []
        for cat in category:
		    article = list(Article.objects.filter(category=cat).order_by('pub_date')[:20])
		    articles = {"cat_name":cat.name, "objects":article}
		    article_list.append(articles)
    except Article.DoesNotExist:
		raise Http404
    return render_to_response('news/index.html',{'article_list':article_list},context_instance=RequestContext(request))
    
@cache_page(60 * 120)
def article(request, article_id):
    article = None
    try:
        article = Article.objects.get(pk=article_id)
        tags = article.tag.all()
        q_objects = Q()
        for t in tags:
            q_objects |= Q(tag=t)
        relatedarticles = (Article.objects.filter(q_objects).exclude(pk=article_id)[:3],"Tag")
        
        if int(relatedarticles[0].count()) <3 :
            relatedarticles = (Article.objects.filter(category=article.category).exclude(pk=article_id).order_by('pub_date')[:3],"Category")
		
    except Article.DoesNotExist:
		raise Http404
    return render_to_response('news/article.html',{'article':article,'relatedarticles':relatedarticles},context_instance=RequestContext(request))