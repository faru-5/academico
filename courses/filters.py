import django_filters
from django_filters import DateFilter, CharFilter
from .models import *

class CourseFilter(django_filters.FilterSet):
    search = CharFilter(field_name='title', label='course', lookup_expr='icontains' )
    date = DateFilter(field_name='date_created', label='Uploaded Date', lookup_expr='gte')
    class Meta:
        model = Course
        fields = ['search', 'subject','instructor','date']
