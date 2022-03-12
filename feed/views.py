
from django.shortcuts import render,redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from feed.forms import NewPostForm
from feed.models import Post

@login_required
def create_post(request):
	user = request.user
	if request.method == "POST":
		form = NewPostForm(request.POST, request.FILES)
		if form.is_valid():
			data = form.save(commit=False)
			data.author = user
			data.save()
			return redirect('home')
	else:
		form = NewPostForm()
	return render(request, 'feed/create_post.html', {'form':form})

def post_list(request):
    posts = Post.objects.filter(display_post='everyone')
    
    context = {
        'posts' : posts
    }
    return render(request, 'feed/post_list.html', context)
def post_details(request, pk):
    post = get_object_or_404(Post, pk=pk)
    
    context = {
        'post' : post
    }
    
    return render(request,'feed/post_details.html', context)
    