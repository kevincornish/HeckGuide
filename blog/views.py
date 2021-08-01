from django.views import generic
from .models import Post

class PostList(generic.ListView):
    queryset = Post.objects.filter(status=1).order_by('-created_on')
    template_name = 'blog/blog.html'
    paginate_by = 3

class PostDetail(generic.DetailView):
    model = Post
    template_name = 'blog/post_detail.html'