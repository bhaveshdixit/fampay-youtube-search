from django.db.models import Q, Case, When, IntegerField, Value

from rest_framework import generics as rest_generics

from common import pagination as common_pagination
from search import (models as search_models, serializers as search_serializers)

class VideoListView(rest_generics.ListAPIView):
    """
    API to list videos
    """
    queryset = search_models.Video.objects.order_by('-published_at')
    serializer_class = search_serializers.VideoSerializer
    pagination_class = common_pagination.CustomPagination


class VideoSearchView(rest_generics.ListAPIView):
    """
    API to search videos
    """
    queryset = search_models.Video.objects.order_by('-published_at')
    serializer_class = search_serializers.VideoSerializer
    pagination_class = common_pagination.CustomPagination

    def get_queryset(self):
        queryset = super().get_queryset()
        query = self.request.GET.get('query', None)
        
        # Building multiple filters with Q objects for ordering queryset, decresing order of priority
        title__exact_match_queryset = Q(title=query) if query else Q()  # Exact title match
        description__exact_match_queryset = Q(description=query) if query else Q()  # Exact description match
        
        title_conatins_queryset = Q()   # Title contains query
        description_contains_queryset = Q()   # Description contains query

        # Building contains filters for each word in query
        for word in query.split(' '):
            title_conatins_queryset |= Q(title__icontains=word)
            description_contains_queryset |= Q(description__icontains=word)


        # Annotating queryset with search_type_ordering field to order queryset based on search type
        # search_type_ordering field is based on following priority:
        # 1. Exact title match with value 4
        # 2. Exact description match with value 3
        # 3. Title contains query with value 2
        # 4. Description contains query with value 1
        # 5. Default value 0

        queryset = queryset.filter(
            title__exact_match_queryset | description__exact_match_queryset |
            title_conatins_queryset | description_contains_queryset
        ).annotate(
            search_type_ordering=Case(
                When(title__exact_match_queryset, then=Value(4)),
                When(description__exact_match_queryset, then=Value(3)),
                When(title_conatins_queryset, then=Value(2)),
                When(description_contains_queryset, then=Value(1)),
                default=Value(0),
                output_field=IntegerField(),
            )
        ).order_by('-search_type_ordering', '-published_at')

        return queryset
