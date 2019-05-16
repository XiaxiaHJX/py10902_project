from django.shortcuts import render
from django.http import HttpResponse,HttpResponseRedirect
from django.template import loader,RequestContext
from .models import BookInfo,HeroInfo
# Create your views here.

def index(request):
    # return HttpResponse('index首页')
    # #加载模板
    # template=loader.get_template('booktest/index.html')
    #
    # context={}
    # #渲染
    # result=template.render(context=context)
    # return HttpResponse(result)
    return render(request,'booktest/index.html')

def list(request):
    # template=loader.get_template('booktest/list.html')
    booklist=BookInfo.objects.all()
    # #渲染
    # result=template.render({'booklist':booklist})
    # return HttpResponse(result)
    return render(request,'booktest/list.html',{'booklist':booklist})

def detail(request,id):
    # template=loader.get_template('booktest/detail.html')
    # book=None
    try:
        book=BookInfo.objects.get(pk=id)

    except Exception as e:
        return HttpResponse('没有当前书籍')

    #渲染
    # result=template.render({'book':book})
    # return HttpResponse(result)
    return render(request,'booktest/detail.html',{'book':book})

def delebook(request,id):
    BookInfo.objects.get(pk=id).delete()
    return HttpResponseRedirect('/booktest/list/')

def delehero(request,id):
    hero=HeroInfo.objects.get(pk=id)
    bookid=hero.book.id
    hero.delete()
    return HttpResponseRedirect('/booktest/detail/%s/'%(bookid,))