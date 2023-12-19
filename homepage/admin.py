from django.contrib import admin
from .models import Subscriber, Message, News

admin.site.register(Subscriber)
admin.site.register(Message)

@admin.register(News)
class NewsAdmin(admin.ModelAdmin):
    list_display = ('title', 'publication_date')
    search_fields = ('title', 'publication_date')

    def image_display(self, obj):
        return '<img src="%s" width="50px" />' % obj.image.url

    image_display.allow_tags = True