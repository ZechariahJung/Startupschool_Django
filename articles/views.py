from django.views.generic import ListView, DetailView
from .models import Article

class ArticleListView(ListView):
    model = Article #정적인 화면이 아니기 때문에 model을 추가
    template_name = "article_list.html"

class ArticleDetailView(DetailView):
    model = Article
    template_name = "article_detail.html"