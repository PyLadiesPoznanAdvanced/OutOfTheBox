from django.contrib import messages
from django.shortcuts import render
from django.views.generic import ListView

from web_scrapper.forms import SearchForm
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


def search(request):
    if request.method == "POST":
        form = SearchForm(request.POST)
        if form.is_valid():
            pass
            messages.error(request, 'Not working yet')
            # TODO magic start here
    else:
        form = SearchForm()
    return render(request, 'web_scrapper/search.html', {'form': form, 'section': 'web_scrapper'})
