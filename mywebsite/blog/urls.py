from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('post/<slug:slugInput>/', views.detailPost, name='detail_post'),
    path('category/<str:categoryInput>/', views.categoryPost, name='category_post'),
]

# urlpatterns = [
#     path('', views.blog, name='blog'),
#     path('Bola/', views.Bola, name='bola'),
# ]
