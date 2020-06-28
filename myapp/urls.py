from django.urls import path
from .import views
app_name = 'myapp'
urlpatterns = [
     path('', views.home, name='home'),
     path('<slug:category_slug>', views.home, name='post_list_by_slug'),
     path('guide/<slug:category_slug>/', views.home, name='guide_by_slug'),
     path('about/', views.about_list, name='about_list'),
     path('portfolio/', views.portfolio_list, name='portfolio_list'),

     path('portfolio/<slug:category_slug>/', views.portfolio_list, name='portfolio_list_by_category'),
     path('<int:id>/<slug:slug>/', views.python_detail, name='python_detail'),
     path('django/', views.django, name='django-list'),
     path('javascript/', views.django, name='javascript-list'),
      path('React-js/', views.react, name='react-list'),
]
