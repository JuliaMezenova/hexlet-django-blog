from django.shortcuts import render #redirect


#def index(request):
#    return render(request, 'index.html', context={
#        'who': 'World',
#    })

from django.views.generic.base import TemplateView
# from django.urls import reverse
  
class HomePageView(TemplateView):
       
    template_name = "index.html"
           
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['who'] = 'World'
        return context

    def get(self, request, *args, **kwargs):
        return render(request, 'base.html')
       
#return redirect(reverse('article', kwargs={'tags': 'python', 'article_id':42}), permanent=True)


def about(request):
    return render(request, 'about.html')
