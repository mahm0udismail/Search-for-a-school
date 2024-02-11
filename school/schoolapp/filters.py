import django_filters
from .models import School

class SchoolFilter(django_filters.FilterSet):
    class Meta:
        model = School
        fields = '__all__'