from django.contrib import admin
from .models import Subreddit

@admin.register(Subreddit)
class SubredditAdmin(admin.ModelAdmin):
    list_display = ('name', 'creator', 'created_at')
    search_fields = ('name', 'creator__username')
    list_filter = ('created_at',)
    readonly_fields = ('creator', 'created_at')

    fieldsets = (
        ('Subreddit Information', {
            'fields': ('name', 'description', 'creator', 'created_at')
        }),
        ('Appearance', {
            'fields': ('icon', 'banner')
        }),
        ('Membership', {
            'fields': ('members',)
        }),
    )
    filter_horizontal = ('members',)

