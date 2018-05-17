from django.shortcuts import render,redirect,HttpResponse
from app01.models import *
from django.http import JsonResponse
import os
from myblog import settings

# Create your views here.
def login(request):
    if request.method=='GET':
        return render(request,'login.html')
    user=request.POST.get('user')
    pwd=request.POST.get('pwd')
    user=User.objects.filter(username=user,password=pwd).first()
    if not user:
        return redirect('/login/')
    request.session['username']=user.username
    request.session['uid']=user.id
    request.session['type']=user.role.type
    if user.role.type==1:
        return redirect('/write/')
    return redirect('/index/')

def index(request,**kwargs):
    if request.method=='GET':
        cate_list = Category.objects.all()
        if not kwargs :
            article=Article.objects.all().first()
            tag_list=Category.objects.all().first().tag.all()
            return render(request,'index.html',{'cate_list':cate_list,'article':article,'tag_list':tag_list})
        id = kwargs.get('id')
        if kwargs.get('name')=='article':
            article=Article.objects.filter(id=id).first()
            tag_list=Category.objects.filter(tag__article__id=id).first().tag.all()
        else:
            tag_list=Category.objects.filter(id=id).first().tag.all()
            if not tag_list.first():
                article = Article.objects.all().first()
                return render(request, 'index.html', {'cate_list': cate_list, 'article': article, 'tag_list': tag_list})
            article=tag_list.first().article.first()
        return render(request, 'index.html',{'cate_list': cate_list, 'article': article, 'tag_list': tag_list})


def write(request):
    if request.method=='GET':
        if not request.session.get('username') or request.session['type']!=1:
            return redirect('/login/')
        cate_list=Category.objects.all()
        tag_list=Tag.objects.all()
        return render(request, 'write.html',{'cate_list':cate_list,'tag_list':tag_list})
    content=request.POST.get('content')
    tag=request.POST.get('tag')
    title=request.POST.get('title')
    result=Article.objects.create(title=title,content=content,tag_id=tag)
    if not result:
        return HttpResponse('有错误')
    else:
        return redirect('/article_list/')

def article_list(request):
    if request.method=='GET':
        if not request.session.get('username') or request.session['type']!=1:
            return redirect('/login/')
        article_list=Article.objects.all()
        return render(request, 'article_list.html',{'article_list':article_list})
def edit(request,id):
    if request.method=='GET':
        if not request.session.get('username') or request.session['type']!=1:
            return redirect('/login/')
        tag_list = Tag.objects.all()
        ad=Article.objects.filter(id=id).first()
        return render(request,'edit.html',{'tag_list':tag_list,'ad':ad})
    else:
        content = request.POST.get('content')
        tag = request.POST.get('tag')
        title = request.POST.get('title')
        try:
            Article.objects.filter(id=id).update(title=title, content=content,tag_id=tag)
            return redirect('/article_list/')
        except Exception:
            return HttpResponse('编辑失败')
def add_tag(request):
    if request.method=='POST':
        ret={'status':1,'msg':'添加成功'}
        tag=request.POST.get('tag')
        cate=request.POST.get('cate')
        result=Tag.objects.create(title=tag,cate_id=cate)
        if not result:
            ret['status']=2
            ret['msg']='添加失败'
        return JsonResponse(ret)
def delete(request,id):
    if request.method=='GET':
        article=Article.objects.filter(id=id).first()
        article.delete()
        return redirect('/article_list/')
def search(request):
    if request.method=='POST':
        ret={"status":1}
        data=request.POST.get('data')
        article=Article.objects.filter(title__icontains=data).first()
        if not article:
            ret['status']=2
            return JsonResponse(ret)
        ret['aid']=article.id
        return JsonResponse(ret)
def notfound(request):
    if request.method=='GET':
        cate_list = Category.objects.all()
        return render(request,'notfound.html',{'cate_list':cate_list})

def upload_img(request):
    file_obj=request.FILES.get("article_img")

    path=os.path.join(settings.MEDIA_ROOT,"img",file_obj.name)

    with open(path,"wb") as f:
        for line in file_obj:
            f.write(line)

    import json

    res={
        "error":0,
        "url":"/media/img/"+file_obj.name
    }

    return HttpResponse(json.dumps(res))
def symoon(request):
    return render(request,'symoon.html')
