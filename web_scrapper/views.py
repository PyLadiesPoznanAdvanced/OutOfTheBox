from django.shortcuts import render
from django.views.generic import ListView
from .models import SearchProfile


class SearchProfileListView(ListView):
    template_name = 'web_scrapper/list.html'
    context_object_name = 'search_profile_list'
    model = SearchProfile

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['section'] = 'web_scrapper'
        return context


# Create your views here.
def configure(request):
    return None
