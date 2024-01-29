from django.shortcuts import render
# from django.http import HttpResponse
# Create your views here.

#def index(request):
#    return render(request, 'articles/index.html', context={'name': 'Article'})

from django.http import HttpResponse
from django.views import View
 
  
class IndexView(View):
       
    def get(self, request):
        return HttpResponse('Article')

