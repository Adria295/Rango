from django.urls import path
from rango import views

app_name = 'rango'

urlpatterns = [
    path('', views.cover, name='cover'),
    path('index/', views.index, name='index'),
    path('about/', views.about, name='about'),
    path('category/<slug:category_name_slug>/', views.show_category, name='show_category'),
    path('add_category/', views.add_category, name='add_category'),
    path('category/<slug:category_name_slug>/add_page/', views.add_page, name='add_page'),
    path('restricted/', views.restricted, name='restricted'),
    path('profile/<username>/', views.ProfileView.as_view(), name='profile'),
    path('search/', views.search, name='search'),
]
