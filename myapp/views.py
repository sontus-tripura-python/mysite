from django.shortcuts import render, get_object_or_404
from .models import *
# Create your views here.
def about_list(request):
    abouts = About.objects.all()[:1]
    context = { 'abouts': abouts }
    return render(request, 'blog/about.html', context)

def home(request, category_slug=None):
    category = None
    python_cats = PythonCategory.objects.all()
    python = Python.objects.all()
    if category_slug:
        category = get_object_or_404(PythonCategory, slug=category_slug)
        python = python.filter(category=category)
    context = { 'category': category, 'python_cats': python_cats,
     'python': python, }
    return render(request, 'blog/home.html', context)

def python_detail(request, id, slug):
    post = get_object_or_404(Python, id=id, slug=slug)
    context = {'post': post}
    return render(request, 'blog/post_details.html', context)

def portfolio_list(request, category_slug=None):
    category = None
    portfolio_cats = PortfolioCategory.objects.all()
    portfolio = Portfolio.objects.all()
    if category_slug:
        category = get_object_or_404(PortfolioCategory, slug=category_slug)
        portfolio = portfolio.filter(category=category)
    context = {'category':category, 'portfolio_cats': portfolio_cats, 'portfolio': portfolio }
    return render(request, 'blog/portfolio_list.html', context)

def django(request):
    django = Django.objects.all()
    context = {'django': django }
    return render(request, 'blog/django.html', context)

def javascript(request):
    javascript = JavaScript.objects.all()
    context = {'javascript': javascript }
    return render(request, 'blog/javascript.html', context)

def react(request):
    react = React.objects.all()
    context = {'react': react }
    return render(request, 'blog/react.html', context)
