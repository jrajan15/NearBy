import django_filters
from .models import Events
from django_filters import CharFilter


class EventFilter(django_filters.FilterSet):
    location = CharFilter(field_name="location", lookup_expr='icontains')

    class Meta:
        model = Events
        fields = ['location']