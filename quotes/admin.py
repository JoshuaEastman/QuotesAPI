from django.contrib import admin
from .models import Quote

# Register your models here.
@admin.register(Quote)
class QuoteAdmin(admin.ModelAdmin):
    list_display = ('short_text', 'author', 'tag', 'year', 'language')
    search_fields = ('text', 'author', 'tag', 'source')

    def short_text(self, obj):
        # truncate quotes to 50 characters in admin list
        return (obj.text[:50] + '...') if len(obj.text) > 50 else obj.text

    short_text.short_description = 'Quote'