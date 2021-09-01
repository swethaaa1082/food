from django.urls import path
from test1_app import views
urlpatterns = [
    path('',views.index,name='index'),
    path('home',views.home,name='home'),
    path('<slug:c_slug>/', views.home, name='products_by_category'),
    path('<slug:c_slug>/<slug:product_slug>/', views.ProdCatDetail, name='ProdCatDetail'),
    path('search', views.searchResult, name='searchResult')
]