from django.db import models
from django.conf import settings
from django.core.validators import RegexValidator

validate_subreddit_name = RegexValidator(
    r"^[a-zA-Z0-9_]+$",
    "Subreddit names can only contain letters, numbers, and underscores.",
)

class Subreddit(models.Model):
    name = models.CharField(max_length=100, unique=True, validators=[validate_subreddit_name])
    description = models.TextField(max_length=500)
    creator = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)

    icon = models.ImageField(upload_to="subreddit_icons/", null=True, blank=True)
    banner = models.ImageField(upload_to="subreddit_banners/", null=True, blank=True)

    members = models.ManyToManyField(
        settings.AUTH_USER_MODEL,
        related_name="joined_subreddits",
        blank=True,
        null=True,
    )

    def __str__(self):
        return self.name
