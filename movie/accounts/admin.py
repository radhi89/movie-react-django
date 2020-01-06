from django.contrib import admin

# Register your models here.


from .models import Movie, Enquiry, Review


@admin.register(Movie)
class MovieAdmin(admin.ModelAdmin):
    search_fields = ['title', 'genre', 'stars', ]
    list_filter = ['release_date', 'title', 'genre', 'stars', ]
    list_display = ['id', 'title', 'genre', 'release_date', 'director', 'stars']
    readonly_fields = ('created', 'modified')


admin.site.register(Enquiry)
admin.site.register(Review)
