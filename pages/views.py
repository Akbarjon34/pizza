from django.shortcuts import render 
from pages.models import MainScrollModel


def home_page_view(request):
    
    scrolls = MainScrollModel.objects.all().order_by('-pk')
    context = {
        'scrolls': scrolls
    }

    return render(request, template_name= 'index.html', context=context)