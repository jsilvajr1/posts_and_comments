from django.shortcuts import render
from .models import Post, Comment

# Create your views here.
def index(request):
    post_list = Post.objects.order_by('id')
    data = {'post_list': post_list}
    return render(request, 'posts/posts.html', data)

def details(request, post_id):
    post_list = Post.objects.get(id = post_id)
    comments = post_list.comments.all()
    data = {
        'post_list': post_list,
        'comments' : comments,        
    }

    print('comments', comments)

    return render(request, 'posts/details.html', data)