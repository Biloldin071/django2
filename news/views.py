# 🔚🔜
from django.shortcuts import render
from .models import News
from django.urls import reverse_lazy
from django.views.generic import UpdateView, DeleteView


def news_list_view(request):
    news_list = News.published.all()
    top_news = News.published.all()[:5]

    local_one = News.published.filter(category__name='Mahalliy')[0]
    local_news = News.published.filter(category__name='Mahalliy')[1:4]

    fashionn_none = News.published.filter(category__name='Xorij')[0]
    fashin_news = News.published.filter(category__name='Xorij')[1:3]

    technalog_noon = News.published.filter(category__name='Sport')[0]
    technalogiy_news = News.published.filter(category__name='Sport')[1:3]

    iqtisod_game = News.published.filter(category__name='Iqtisodiy')[0]
    iqtisod_gam = News.published.filter(category__name='Iqtisodiy')[1:3]

    # yangilik_lar = News.published.filter(category__name='Yangiliklar')[0]
    #yangilik_larr = News.published.filter(category__name='Yangiliklar')[1:4]


    context = {
        'news_list': news_list,
        'top_news': top_news,
        #Mahalliy
        'local_one': local_one,
        'local_news': local_news,
        #Xorij
        'fashionn_none': fashionn_none,
        'fashin_news': fashin_news,
        #Sport
        'technalog_noon': technalog_noon,
        'technalogiy_news': technalogiy_news,
        #Iqtisod
        'iqtisod_game': iqtisod_game,
        'iqtisod_gam': iqtisod_gam,
        #yangilik
        #'yangilik_lar': yangilik_lar,
        #'yangilik_larr': yangilik_larr,
    }
    return render(request, template_name='home.html', context=context)






def news_detail_view(request, slug):
    news_detail = News.objects.get(slug=slug)
    context = {
        'news_detail': news_detail
    }
    return render(request, 'single_page.html', context)

def contact_view(request):
    context = {

    }

    return render(request, 'contact.html', context)



def about_us_view(request):
    context = {

    }

    return render(request, 'about_us.html', context)






def Mahalliy_view(request):
    news_detail = News.objects.filter(category__name = 'Mahalliy')
    context = {
        'local_news': news_detail

    }

    return render(request, 'Mahalliy.html', context)


def xorij_view(request):
    news_detail = News.objects.filter(category__name = 'Xorij')
    context = {
        'local_news': news_detail

    }

    return render(request, 'xorij.html', context)



def sport_view(request):
    news_detail = News.objects.filter(category__name = 'Sport')
    context = {
        'local_news': news_detail

    }

    return render(request, 'sport.html', context)


def iqtisod_view(request):
    news_detail = News.objects.filter(category__name = 'Iqtisodiy')
    context = {
        'local_news': news_detail

    }

    return render(request, 'iqtisod.html', context)





class NewsUpdateView(UpdateView):
    template_name = 'crud/update.html'
    model = News
    fields = ['title', 'slug', 'body', 'image']


class NewsDeleteView(DeleteView):
    model = News
    template_name = 'crud/delete.html'
    success_url = reverse_lazy('home_page')

