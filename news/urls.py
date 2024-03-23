from django.contrib import admin
from django.urls import path
# from django.views.generic import CreateView, UpdateView, DeleteView

from .views import news_list_view, news_detail_view,  contact_view, about_us_view, \
Mahalliy_view, xorij_view, sport_view, iqtisod_view,  NewsUpdateView, NewsDeleteView

urlpatterns = [
    path('', news_list_view, name='home_page'),
    path('news/<slug>/', news_detail_view, name='detail_link'),
    path('contact-us/', contact_view, name='contact_link'),
    path('about/', about_us_view, name='about_us_link'),
    path('Mahalliy/', Mahalliy_view, name='Mahalliy_link'),
    path('Xorij/', xorij_view, name='xorij_link'),
    path('Sport/', sport_view, name='sport_link'),
    path('Iqtisodiy/', iqtisod_view, name='iqtisod_link'),
    path('news/<slug>/update/', NewsUpdateView.as_view(), name='create_news'),
    path('news/<slug>/delete/', NewsDeleteView.as_view(), name='delete_news'),

]

