
from cProfile import Profile
from operator import ipow
from django.shortcuts import render,redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from feed.forms import NewPostForm
from feed.models import Post
from account.models import User

@login_required
def create_post(request):
	user = request.user
	if request.method == "POST":
		form = NewPostForm(request.POST, request.FILES)
		if form.is_valid():
			data = form.save(commit=False)
			data.author = user
			data.save()
			return redirect('post:post_list')
	else:
		form = NewPostForm()
	return render(request, 'feed/create_post.html', {'form':form})

def post_list(request):
    posts = Post.objects.all()
    user = User.objects.get(phone = request.user.phone)
    user_friends = user.profile.friends.all()
    friend_list = []
    for friend in user_friends:
        friend_list.append(friend)
        
    print('\n\n', friend_list)
    
    context = {
        'posts' : posts,
        'friend_list':friend_list,
    }
    return render(request, 'feed/post_list.html', context)
def post_details(request, pk):
    post = get_object_or_404(Post, pk=pk)
    
    context = {
        'post' : post,
        
    }
    
    return render(request,'feed/post_details.html', context)
    