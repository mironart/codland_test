from django.shortcuts import render, reverse
from django.views import generic
from .models import Article
from .forms import ArticleForm
from django.http import HttpResponseRedirect


class HomePageView(generic.View):

    def get(self, request):
        articles = Article.objects.all().order_by('-date_created')[:10]
        context = {
            'articles':articles,
        }

        context['test'] = 'test zalupa NICE'

        return render(request, 'home.html', context)


class AddArticleView(generic.View):

    def get(self, request):

        context = {
            'form':ArticleForm(),
        }

        return render(request, 'add_article.html', context)

    def post(self, request):
        if request.POST:
            form = ArticleForm(request.POST)
            if form.is_valid():
                Article.objects.create(
                    title=form.cleaned_data['title'],
                    body=form.cleaned_data['body'],
                )

                print('----------------------- .>>>>>>>>>>>>>>>>>.  ZBS')

                return HttpResponseRedirect(reverse('home_page'))
            else:
                print('----------------------- .>>>>>>>>>>>>>>>>>.  NINE')
                context = {'form':form}
                return render(request, 'add_article.html', context)
