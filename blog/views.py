from django.shortcuts import render
from django.http import (Http404, HttpResponseNotFound,
                         HttpResponseRedirect)

# Create your views here.
def starting_page(request):
    return render(request, "blog/index.html")

def posts(request):
    return render(request, "blog/posts.html")

def post_detail(request):
    return render(request, "blog/post-detail.html")