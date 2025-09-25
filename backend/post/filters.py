import django_filters as filters
from .models import Post

class PostFilter(filters.FilterSet):
    order = filters.OrderingFilter(
        fields=(
            ('created_at', 'created_at'),
            ('upvote_count', 'upvote_count'),
            ('downvote_count', 'downvote_count'),
            ('net_score', 'net_score'),
        ),
    )
    class Meta:
        model = Post
        fields = {
            'title': ['icontains'],
            'description': ['icontains'],
            'created_by': ['exact'], 
            'created_at': ['date__gte', 'date__lte'],
        }
