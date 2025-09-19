from django.contrib import admin

from .models import Rule, Subreddit


class RuleInline(admin.TabularInline):
    model = Rule
    extra = 1


@admin.register(Subreddit)
class SubredditAdmin(admin.ModelAdmin):
    list_display = ("name", "created_by", "created_at")
    search_fields = ("name", "created_by__username")
    list_filter = ("created_at",)
    readonly_fields = ("created_by", "created_at")

    fieldsets = (
        (
            "Subreddit Information",
            {"fields": ("name", "description", "created_by", "created_at")},
        ),
        ("Appearance", {"fields": ("icon", "banner")}),
        ("Membership", {"fields": ("members",)}),
    )
    filter_horizontal = ("members",)
    inlines = [RuleInline]


@admin.register(Rule)
class RuleAdmin(admin.ModelAdmin):
    list_display = ("title", "subreddit")
    search_fields = ("title", "subreddit__name")
    list_filter = ("subreddit",)

    fieldsets = (
        ("Rule Information", {"fields": ("subreddit", "title", "description")}),
    )
