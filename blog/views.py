from django.shortcuts import render
from .models import Post
from django.utils import timezone
# Create your views here

def posts_list(request):
	posts = Post.objects.filter(Published_date__lte=timezone.now()).order_by('pusblished_date')
	return render(request, 'blog/post_list.html',{'posts':posts})
