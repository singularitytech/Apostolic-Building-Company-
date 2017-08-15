from django.shortcuts import render, get_object_or_404
from django.utils import timezone
from .models import Blog

def index(request):
    posts = Blog.objects.filter(published_date__lte=timezone.now()).order_by('-published_date')[:6]
    return render(request, 'blog/post_list.html', {'posts': posts})

def about(request):
	return render(request, 'blog/about.html')

def policy(request):
	return render(request, 'blog/policy.html')

def post_list(request):
    posts = Blog.objects.filter(published_date__lte=timezone.now()).order_by('-published_date')[:5]
    return render(request, 'blog/base.html', {'posts': posts})

def post_detail(request, pk):
    post = get_object_or_404(Blog, pk=pk)
    return render(request, 'blog/detail.html', {'post': post})

def lazy_load_posts(request):
	page = request.POST.get('page')
	posts = Blog.objects.filter(published_date__lte=timezone.now()).order_by('-published_date')[:5] # get just 5 posts

	results_per_page = 5
	paginator = Paginator(posts, results_per_page)
	try:
		posts = paginator.page(page)
	except PageNotAnInteger:
		posts = paginator.page(2)
	except EmptyPage:
		posts = paginator.page(paginator.num_pages)

	# build a html posts list with the paginated posts
	posts_html = loader.render_to_string('blog/post.html', {'posts': posts})
	output_data = {'post_html': posts_html, 'has_next': posts.has_next()}
	return JsonResponse(output_data)

