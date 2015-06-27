from django.contrib import admin
from .models import Rockinfo, Rockvids
from .models import Feat
from .models import Navers
from .models import Feedback
from .models import Genre, Genrevids

class ChoiceInline(admin.TabularInline):
    model = Rockvids
    extra = 10
    max_num = 10
	
class RockinfoAdmin(admin.ModelAdmin):
    fieldsets = [
        ('The Band',               {'fields': ['rock_name']}),
        ('Image', {'fields': ['rock_img']}),
		('Rank', {'fields': ['rank']}),
		('About The Band', {'fields': ['about']}),
    ]
    inlines = [ChoiceInline]	
    list_display = ('rock_name', 'rock_img')
    list_filter = ['rank']
    search_fields = ['rock_name']
	
class ItemInline(admin.TabularInline):
    model = Genrevids
    extra = 20
	
class GenreAdmin(admin.ModelAdmin):
    fieldsets = [
        ('The Genre',               {'fields': ['genre_name']}),
        ('Image', {'fields': ['genre_img']}),
		('About The Genre', {'fields': ['genre_about']}),
    ]
    inlines = [ItemInline]	
    list_display = ('genre_name', 'genre_img')
    search_fields = ['genre_name']
	
class FeedbackAdmin(admin.ModelAdmin):
    fieldsets = [
        (None, {'fields': ['fname']}),
        (None, {'fields': ['fmail']}),
        (None, {'fields': ['msg']}),
    ]
    list_display = ('fname', 'fmail')

admin.site.register(Rockinfo, RockinfoAdmin)
admin.site.register(Genre, GenreAdmin)
admin.site.register(Feat)
admin.site.register(Navers)
admin.site.register(Feedback, FeedbackAdmin)