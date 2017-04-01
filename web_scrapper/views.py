from django.shortcuts import render
from django.views.generic import ListView
from .models import SearchProfile

class SearchProfileListView(ListView):
    template_name = 'web_scrapper/list.html'
    context_object_name = 'search_profile_list'
    model = SearchProfile

# Create your views here.
def configure(request):
    return None