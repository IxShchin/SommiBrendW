from django.contrib import admin
from .models import *


class SubscriberAdmin (admin.ModelAdmin):
    list_display = ['email', "password"]
    # inlines = [FieldMappingInline]
    # field = []
    # search_fields = ['catagory', 'subCategory', 'suggestKeyword']

    class Meta:
        model = Subscriber

admin.site.register(Subscriber, SubscriberAdmin)
