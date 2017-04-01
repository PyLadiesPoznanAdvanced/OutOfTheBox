from django.contrib import admin

# Register your models here.
from web_scrapper.models import SearchProfile, Hashtag


@admin.register(SearchProfile)
class SearchProfileAdmin(admin.ModelAdmin):
    pass

@admin.register(Hashtag)
class HashtagAdmin(admin.ModelAdmin):
    pass