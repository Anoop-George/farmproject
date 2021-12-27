from django.shortcuts import render, get_object_or_404
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.contrib.auth.models import User
from django.views.generic import (
    ListView,
    DetailView,
    CreateView,
    UpdateView,
    DeleteView
)
from .models import Post
from django.db.models import Q


def searchview(request):
    
    return render(request,'',context)


def home(request):
    context = {
        'posts': Post.objects.all()
    }
    return render(request, 'blog/home.html', context)


class PostListView(ListView):
    model = Post
    template_name = 'blog/home.html'  # <app>/<model>_<viewtype>.html
    context_object_name = 'posts'
    ordering = ['-date_posted']
    paginate_by = 12


class UserPostListView(ListView):
    model = Post
    template_name = 'blog/user_posts.html'  # <app>/<model>_<viewtype>.html
    context_object_name = 'posts'
    paginate_by = 5

    def get_queryset(self):
        user = get_object_or_404(User, username=self.kwargs.get('username'))
        return Post.objects.filter(author=user).order_by('-date_posted')


class PostDetailView(DetailView):
    model = Post


class PostCreateView(LoginRequiredMixin, CreateView):
    model = Post
    fields = ['title', 'mobile','content','state','district','pincode','image1','image2','image3','image4']
    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)


class PostUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Post
    fields = ['title', 'mobile','content','state','district','pincode','image1','image2','image3','image4']
    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

    def test_func(self):
        post = self.get_object()
        if self.request.user == post.author:
            return True
        return False


class PostDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Post
    success_url = '/'

    def test_func(self):
        post = self.get_object()
        if self.request.user == post.author:
            return True
        return False


def about(request):
    return render(request, 'blog/about.html', {'title': 'About'})


# class SearchView(ListView):
#     model = Post
#     template_name = 'blog/searchresult.html'  
#     context_object_name = 'posts'
#     ordering = ['-date_posted']
#     paginate_by = 5
#     def get_queryset(self):
#         qs = self.model.objects.all()
#         state = self.kwargs['state']
#         district = self.kwargs['district']
#         catagory = self.kwargs['catagory']
#         pin = self.kwargs['pin']
#         searchdata = self.kwargs['searchdata']
        
#         result = Post.objects.filter(Q(state=state)& Q(district=district) & Q(catagory=catagory))
        
#         if pin:
#             result=result.filter(pincode=pin)
#         if searchdata:
#             result=result.filter(Q(title__icontains=searchdata)|Q(content__icontains=searchdata))
       
#         print(result)
#         return result

def SearchView(request):
    if request.method=='POST':
        state=request.POST['state']
        district=request.POST['district']
        catagory=request.POST['catagory']
        pin=request.POST['pin']
        searchdata=request.POST['searchdata']
        buyorsell=request.POST['buyorsell']
        print(state)
        return render(request, 'blog/searchresult.html', {})
    else:
        return render(request, 'blog/searchresult.html', {})     

