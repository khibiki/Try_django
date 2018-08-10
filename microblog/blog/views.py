from django.urls import reverse_lazy #URLを読み込む
from django.shortcuts import render
from django.views.generic import ListView
from django.views.generic import DetailView
from .models import Blog
from django.views.generic import CreateView,UpdateView,DeleteView
from .forms import BlogForm

class BlogListView(ListView):
	model = Blog

class BlogDetailView(DetailView):
	model = Blog

class BlogCreateView(CreateView):
	model = Blog
	form_class = BlogForm
	# fields = ["content"]
	success_url = reverse_lazy("index") #遷移するURLを指定（ニックネームを使う事が多い）

class BlogUpdateView(UpdateView):
	model = Blog
	form_class = BlogForm
	# fields = ["content"]
	def get_success_url(self):
		blog_pk = self.kwargs['pk']
		return reverse_lazy("detail", kwargs={"pk": self.kwargs["pk"]})

class BlogDeleteView(DeleteView):
	model = Blog
	success_url = reverse_lazy("index") 
# Create your views here.
