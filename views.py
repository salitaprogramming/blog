from rest_framework import viewsets
from django.shortcuts import render, redirect
from .models import Post, Category, Comment, User
from .forms import CommentsForm, LoginForm
from .serializer import PostSerializer, UserSerializer, CategorySerializer, CommentSerializer
from rest_framework.response import Response
from django.contrib.auth.hashers import make_password

class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer

    def list(self, request, *args, **kwargs):
        us = User.objects.all()
        serializer = UserSerializer(us, many=True)
        return Response(serializer.data)

class CategoryViewSet(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer

    '''def list(self, request, *args, **kwargs):
        cat = Category.objects.all()
        serializer = CategorySerializer(cat, many=True)
        return Response(serializer.data)'''

class CommentViewSet(viewsets.ModelViewSet):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer

class PostViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer

    def list(self, request, *args, **kwargs):
        ps = Post.objects.all()
        serializer = PostSerializer(ps, many=True)
        return Response(serializer.data)

def posts(request, category_id):
    posts = Post.objects.filter(cat__id=category_id).order_by('date')
    return render(request, 'blogposts.html', {'posts':posts})

def categories(request):
    categories = Category.objects.all()
    return render(request, 'blogcategories.html', {'categories':categories})

def article(request, post_id):
    posts = Post.objects.filter(id=post_id).order_by('date')
    if request.method == 'POST':
        form = CommentsForm(request.POST)
        if form.is_valid():
            comment = Comment()
            username_entered = request.POST.get('name')
            email_entered = request.POST.get('email')
            try:
                User.objects.get(username=username_entered)
            except User.DoesNotExist:
                new_user = User()
                new_user.username = username_entered
                new_user.save()

            comment.username = User.objects.filter(username=username_entered).first()
            comment.comment = request.POST.get('message')
            comment.save()
            return render(request, 'article.html', {'posts':posts, 'form': CommentsForm})
    else:
        return render(request, 'article.html', {'posts':posts, 'form':CommentsForm()})
def comments(request):
    comments = Comment.objects.all()
    return render(request,'comments.html', {'comments':comments})