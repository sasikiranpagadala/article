from django.shortcuts import render,redirect
from django.http import HttpResponse
from . models import Post
from django.contrib.auth.models import User

def home(request):
	users = Post.objects.all()
	context={
		'users':users,
	}
	return render(request,'newsarticle/home.html',context)
def about(request):
	return render(request,'newsarticle/about.html',{'title':'About'})

def input(request,pk):
	context={
		'id':pk
	}
	return render(request,'newsarticle/input.html',context)

def addcontent(request,pk):
	if(request.method=='POST'):
		t=request.POST['val1']
		c=request.POST['val2']
		user=User.objects.get(id=pk)
		post=Post(title=t,content=c,author=user)
		post.save()
		return redirect("home-page")
		#return HttpResponse("<h1>S</h1>")

def getuser(request,pk,uid):
	post=Post.objects.get(id=pk)
	user=User.objects.get(id=post.author.id)
	if(uid==user.id):
		post.delete()
	return redirect('home-page')

def update(request,pk):
	context={
		'id':pk
	}
	return render(request,'newsarticle/update.html',context)
	
def up(request,pk):
	if(request.method=='POST'):
		t=request.POST['val1']
		c=request.POST['val2']
		post=Post.objects.get(id=pk)
		user=User.objects.get(id=post.author.id)
		if(t!=''):
			post.title=t
		if(c!=''):
			post.content=c
		post.author=user
		post.save()
	return redirect('home-page')