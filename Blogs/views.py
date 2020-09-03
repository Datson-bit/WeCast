
from django.views.generic import ListView, DetailView, CreateView

from Blogs.models import Post, Sport, Comment


class HomeView(ListView):
    model = Post
    template_name = 'home.html'


class SportView(ListView):
    model = Sport
    template_name = 'sport.html'


class ArticleDetailView(DetailView):
    model = Post
    template_name = 'article_details.html'



class SportDetailsView(DetailView):
    model = Sport
    template_name = 'sportview.html'


class AddPostView(CreateView):
    model = Post
    template_name = 'add_post.html'
    fields = '__all__'


class AddSportArticles(CreateView):
    model = Post
    template_name = 'add_sport.html'
    fields = '__all__'